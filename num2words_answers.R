library(data.table)
setDTthreads(6)

# add 1 to 19 -------------------------------------------------------------
num_words <- data.table(
  num = c(1:19, seq(20, 90, by = 10)), 
  words = c(
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "evelven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", 
    "seventeen", "eighteen", "nineteen", "twenty", "thirty", "fourty", "fifty",
    "sixty", "seventy", "eighty", "ninety"
  )
)
setkey(num_words, num)

# add tens ----------------------------------------------------------------
for (i in seq(20, 90, by = 10)) {
    s <- 1:9
    n <- i + s
    w <- paste(num_words[num == i, words], num_words[num %in% s, words])
    num_words <- rbind(num_words, data.table(num = n, words = w))
}


# add hundreds ------------------------------------------------------------
num_words <- rbind(num_words, data.table(
  num = seq(100, 900, by = 100),
  words = paste(num_words[num %in% 1:9, words], "hundred")
))

for (i in seq(100, 900, by = 100)) {
  s <- 1:99
  n <- i + s
  w <- paste(num_words[num == i, words], "and", num_words[num %in% s, words])
  num_words <- rbind(num_words, data.table(num = n, words = w))
}


# add thousands -----------------------------------------------------------
num_words <- rbind(num_words, data.table(
  num = seq(1000, 999000, by = 1000),
  words = paste(num_words[num %in% 1:999, words], "thousand")
))

for (i in seq(1000, 999000, by = 1000)) {
  s <- 1:999
  n <- i + s
  w <- paste(num_words[num == i, words], num_words[num %in% s, words])
  num_words <- rbind(num_words, data.table(num = n, words = w))
}


# add millions ------------------------------------------------------------

msg <- paste(
  paste("---------------------", "---------------------", "---------------------", sep = "-"),
  paste("---------------------", "PROCEED WITH CAUTION!", "---------------------"), 
  paste("---------------------", "---------------------", "---------------------", sep = "-"),
  sep = "\n"
)
msg <- paste(msg, 
             paste("\nThe size of the file so far is", 
             round(object.size(num_words) / 1024^2, 1), "Mb."),
             sep = "\n")
msg <- paste(msg, 
             "The next few lines will produce the desired outcome but will also", 
             paste0("but will also make the file 999 times larger or ~",
             round(object.size(num_words) * 999 / 1024^3, 1), " Gb.\n"),
             sep = "\n")

msg <- paste(msg,
  paste("---------------------", "---------------------", "---------------------", sep = "-"),
  paste("---------------------", "PROCEED WITH CAUTION!", "---------------------"), 
  paste("---------------------", "---------------------", "---------------------", sep = "-"),
  sep = "\n"
)

message(msg)

# num_words <- rbind(num_words, data.table(
#   num = seq(1000000, 999000000, by = 1000000),
#   words = paste(num_words[num %in% 1:999, words], "million")
# ))
# 
# for (i in seq(1000000, 999000000, by = 1000000)) {
#   s <- 1:999999
#   n <- i + s
#   w <- paste(num_words[num == i, words], num_words[num %in% s, words])
#   num_words <- rbind(num_words, data.table(num = n, words = w))
# }

num_words <- rbind(num_words, data.table(
  num = seq(1000000, 999000000, by = 1000000),
  words = paste(num_words[num %in% 1:999, words], "million")
))

for (i in seq(1000000, 999000000, by = 1000000)) {
  s <- 1:999999
  n <- i + s
  w <- paste(num_words[num == i, words], num_words[num %in% s, words])
  temp_dt <- data.table(num = n, words = w)[sample(.N, round(0.01*999999))]
  num_words <- rbind(num_words, temp_dt)
}
