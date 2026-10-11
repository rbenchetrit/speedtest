#!/usr/bin/env Rscript
library(R2HTML)
HTMLStart(outdir="/var/www/html", file="stats", extension="html", echo=FALSE, HTMLframe=TRUE)
HTML.title("My Report", HR=1)

HTML.title("Description of my data", HR=3)
mydata <- c(100, 200, 300)
summary(mydata)

HTML.title("X Y Scatter Plot", HR=2)
plot(sin, -pi, 2*pi, main="Sinus")
HTMLplot()

HTMLStop()
