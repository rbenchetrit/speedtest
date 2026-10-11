library(highcharter)
library(dplyr)

movies <- read_csv("https://raw.githubusercontent.com/hadley/ggplot2movies/master/data-raw/movies.csv")


kubrickdat <- data.frame(
    title = c("Fear and Desire","Killer's Kiss","Killing, The","Paths of Glory","Spartacus","Lolita","Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb", "2001: A Space Odyssey","Clockwork Orange, A","Barry Lyndon","Shining, The", "Full Metal Jacket","Eyes Wide Shut"),
    year = c(1953,1955,1956,1957,1960,1962,1964,1968,1971,1975,1980,1987,1999)
)

kubrick <-
    movies %>%
    filter(title %in% kubrickdat$title & year %in% kubrickdat$year) %>%
    select(title, year, budget, rating, length) %>%
    arrange(desc(year))
