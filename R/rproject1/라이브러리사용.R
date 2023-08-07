# packages install
install.packages('')

#package use!
# java default import 
# import java.lang.*;
# System, String
# library(base)

library(cowsay)

say('안녕!!나는 고양이야.', by = 'cat')
say('안녕!! 좋은 아침...', by='snowman')

library(ggplot2)

ggplot(date=iris, aes(x =Petal.Length, y= Petal.Width))


a <- 10
b <- 20
print(a+b)

salt <- 50
water <- 50
result <- 50/(50+50)*100
cat("소금=",salt,",물=",water,":농도=",result,"%")
