#!/usr/bin/env Rscript
library(R2HTML)
data(iris)
data <- iris[sample(1:nrow(iris),size=30),]

HTMLInitFile(outdir='/var/www/html', filename='grid', useGrid=TRUE,useLaTeX=FALSE)
HTML.title("Iris dataset (again)",1)  
HTML(as.title("20 random observations displayed with HTMLgrid"),HR=3)
HTML("Try to click on columns headers to sort them")
HTMLgrid_inline(data)
HTML(as.title("A summary of those observations displayed with HTMLgrid"),HR=3)
 
describe(data)
summary(data)
HTMLgrid(data,file=HTMLGetFile(),append=TRUE,asDF=TRUE,showimages=TRUE)
HTMLgrid_inline(data,file=HTMLGetFile(),append=TRUE,asDF=TRUE,showimages=TRUE)
HTMLgrid_summary(data,file=HTMLGetFile(),append=TRUE)

HTMLEndFile()
