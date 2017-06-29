require(ggplot2)
library(scales)
data <- read.table("dates.txt", col.names = c("Date", "Count"))
data = data[order(data$Date),]
data$Date = as.Date(data$Date, format = "%Y-%m-%d")
#data$Date = as.Date(paste(data$Date, "-01", sep=""), format = "%Y-%m-%d")
data

ggplot(data, aes(data$Date, data$Count, group = 1)) + 
  #geom_point() +
  geom_line() + 
  labs(x="Date", y="Count") +
  #stat_smooth(aes(data$Date, data$Count), method = "lm", formula = y ~ poly(x, 20), se = FALSE) +
  scale_x_date(breaks = date_breaks("3 months"), expand = c(0,0))

hdata <- read.table("hours.txt", col.names = c("Hour_raw", "Count"))
hdata = hdata[order(hdata$Hour_raw),]
hdata$Hour = as.POSIXct(hdata$Hour_raw, format = "%H:%M") + 3 * 60 * 60

ggplot(hdata, aes(hdata$Hour, hdata$Count, group = 1)) + 
  #geom_point() +
  #geom_line() + 
  labs(x="Hour", y="Count", title="Total messages at minutes over 6 years") +
  stat_smooth(aes(hdata$Hour, hdata$Count), method = "lm", formula = y ~ poly(x, 20), se = FALSE) +
  scale_x_datetime(breaks = date_breaks("1 hours"), labels = date_format("%H:%M", tz="-3"), expand = c(0,0))
  

