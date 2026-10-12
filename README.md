# Speedtest

This repository contains a small Python-based speed test project that collects network performance data and stores it in CSV format.

## Purpose

The project is intended to:
- run a speed test from the command line,
- capture output from the test,
- store the results in a CSV file for later analysis,
- provide a lightweight way to inspect and compare network performance over time.

## Files

- `speedtest.py` — main Python script that runs the speed test and processes the results.
- `speedtest.sh` — shell wrapper for easier execution.
- `speedtest.csv` — output data generated from the speed test.
- `speedtest.log` — log output from the test run.

## Usage

Run the project with:

```bash
python3 speedtest.py
```

or:

```bash
./speedtest.sh
```

## Notes

This project is a small local utility for measuring internet performance and storing results for further review. It is not a full production monitoring service.
