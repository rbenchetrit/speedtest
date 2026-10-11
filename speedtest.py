import os
import re
import shutil
import subprocess
import time
import json
import logging

speedtest_bin = shutil.which('speedtest-cli') or os.path.expanduser('~/.local/bin/speedtest-cli')
if not os.path.exists(speedtest_bin):
    raise FileNotFoundError("speedtest-cli not found. Install it with: python -m pip install --break-system-packages speedtest-cli")

logging.basicConfig(level=logging.INFO)

# Try getting JSON output (preferred) so numeric values aren't corrupted by locale
proc = subprocess.run([speedtest_bin, '--json', '--secure'], capture_output=True, text=True)
if proc.returncode != 0:
    raise RuntimeError(f"speedtest-cli failed: {proc.stderr.strip()}")
response = proc.stdout
print("RAW OUTPUT:")
print(response)

download_mbps = None
upload_mbps = None
ping_ms = None

try:
    data = json.loads(response)
    if 'download' in data:
        download_mbps = float(data['download']) / 1e6
    if 'upload' in data:
        upload_mbps = float(data['upload']) / 1e6
    if 'ping' in data:
        ping_ms = float(data['ping'])
except Exception as e:
    logging.info('JSON parse failed: %s', e)

# Fallback: human-readable parsing
if download_mbps is None or upload_mbps is None:
    logging.info('Falling back to human-readable parsing')
    human = subprocess.run([speedtest_bin, '--secure'], capture_output=True, text=True, check=True).stdout
    print('HUMAN OUTPUT:')
    print(human)
    d = re.findall(r'Download:\s*(\d+[.,]?\d*)', human)
    u = re.findall(r'Upload:\s*(\d+[.,]?\d*)', human)
    p = re.findall(r'Ping:\s*(\d+[.,]?\d*)', human)
    if d:
        download_mbps = float(d[0].replace(',', '.'))
    if u:
        upload_mbps = float(u[0].replace(',', '.'))
    if p:
        ping_ms = float(p[0].replace(',', '.'))

if download_mbps is None or upload_mbps is None:
    raise RuntimeError('Could not parse download/upload from speedtest output')

download = '{:.3f}'.format(download_mbps)
upload = '{:.3f}'.format(upload_mbps)
ping = '{:.3f}'.format(ping_ms) if ping_ms is not None else ''

csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'speedtest.csv')
try:
    f = open(csv_path, 'a+', newline='')
    if os.path.getsize(csv_path) == 0:
        f.write('Date,Time,Ping (ms),Download (Mbit/s),Upload (Mbit/s)\r\n')
except OSError:
    raise RuntimeError(f'Cannot write CSV output to {csv_path}')

#f.write('{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), ping, download, upload))
f.write('{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), download, upload))
f.close()

