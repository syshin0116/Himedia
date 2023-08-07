#단계1: 실습파일 가져오기
twomethod <- read.csv("~/Desktop/Himedia/Himedia_rworkspace/csv/twomethod.csv")
# 교유방법에 따라 시험성적에 차이가 있는지검정하시오
View(twomethod)

summary(twomethod)
#단계2: 두 집단 subset작성(데이터 정제, 전처리)
result <- subset(twomethod, !is.na(score), c(method, score))

#단꼐3: 데이터 분리
a <- subset(result, method==1)
a1 <- a$score

b <- subset(result, method==2)
b1 <- b$score

length(a1) # 22
length(b1) # 35

hist(a1)
hist(b1)
# 단계4: 분포모양 검정

#동질성 비교
var.test(a1,b1)
# 
# F test to compare two variances
# 
# data:  a1 and b1
# F = 1.0648, num df = 21, denom df = 34, p-value = 0.8494
# alternative hypothesis: true ratio of variances is not equal to 1
# 95 percent confidence interval:
#   0.502791 2.427170
# sample estimates:
#   ratio of variances 
# 1.06479 

#p-value=0.8494 => 0.05보다 크므로 분포의 차이가 없다, 정규 분포이다



# 단계5: 가설검정

#두 집단 평균 차이 검정
t.test(a1,b1)
# Welch Two Sample t-test
# 
# data:  a1 and b1
# t = -5.6056, df = 43.705, p-value = 1.303e-06
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -17.429294  -8.209667
# sample estimates:
#   mean of x mean of y 
# 16.40909  29.22857 

t.test(a1,b1,alternative = "greater",conf.level=0.95)
# Welch Two Sample t-test
# 
# data:  a1 and b1
# t = -5.6056, df = 43.705, p-value = 1
# alternative hypothesis: true difference in means is greater than 0
# 95 percent confidence interval:
#   -16.66255       Inf
# sample estimates:
#   mean of x mean of y 
# 16.40909  29.22857 

t.test(a1,b1,alternative = "less",conf.level=0.95)
# Welch Two Sample t-test
# 
# data:  a1 and b1
# t = -5.6056, df = 43.705, p-value = 6.513e-07
# alternative hypothesis: true difference in means is less than 0
# 95 percent confidence interval:
#   -Inf -8.976413
# sample estimates:
#   mean of x mean of y 
# 16.40909  29.22857 

