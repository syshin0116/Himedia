## 연속형 데이터 수치 비교 방법
## 비율척도(나이, 몸무게, 키)

korea.com.time <-  5.2

one_sample <- read.csv("~/Desktop/Himedia/Himedia_rworkspace/csv/one_sample.csv")
View(one_sample)

time <- one_sample$time
print(time)

mean(time, na.rm = T) 
# mean(time, na.rm = T)
# [1] 5.556881

time2 <- na.omit(time) ## NA를 포함한 row를 제거!
time2

## 1. 정규성 검증
shapiro.test(time2)
# Shapiro-Wilk normality
# test
# 
# data:  time2
# W = 0.99137, p-value =0.7242
# => p-value가 0.05이상 나오면 정규분포임!!
# => 정규분포를 따른다!(평균!!! => 모수검정(t-test))

## 2. t-test검증
t.test(time2, mu=5.2, alternative = 'two.side', conf.level = 0.95)
## 대립(연구가설) : 
##     A회사의 노트북 사용시간과 한국의 노트북 사용시간은 차이가 있다. 
## 귀무(영가설) :
##      A회사의 노트북 사용시간과 한국의 노트북 사용시간은 차이가 없다. 
# One Sample t-test
# 
# data:  time2
# t = 3.9461, df = 108,
# p-value = 0.0001417
# alternative hypothesis: true mean is not equal to 5.2
# 95 percent confidence interval:
#   5.377613 5.736148 ==> 구간 추정
# sample estimates:
#   mean of x 
# 5.556881 ==> 점추정

## => 대립가설 채택, 귀무가설 기각
## => A회사의 노트북 사용시간과 한국의 노트북 사용시간은 차이가 있다. 

## 한국의 노트북 평균 사용시간보다 A회사의 노트북 평균 사용시간이 더 큰가?
## t-test검증해보세요.
t.test(time2, mu=5.2, alternative = 'greater', conf.level = 0.95)
# One Sample t-test
# 
# data:  time2
# t = 3.9461, df = 108,
# p-value = 7.083e-05
# alternative hypothesis: true mean is greater than 5.2
# 95 percent confidence interval:
#   5.406833      Inf
# sample estimates:
#   mean of x 
# 5.556881 
## => 대립가설 채택, 귀무가설 기각
## => A회사의 노트북 사용시간이 한국의 노트북 사용시간보다 크다.

#단계1: 데이터셋 가져오기
student_height <- read.csv('~/Desktop/Himedia/Himedia_rworkspace/csv/student_height.csv')

height <- student_height$height
height

korea.woman.height <-  148.5
our.height <- student_height$height

length(our.height)
summary(our.height)
print(our.height)
mean(our.height)

hist(our.height)

## 정규성 검정
shapiro.test(our.height)
# Shapiro-Wilk normality test
# 
# data:  our.height
# W = 0.88711, p-value = 0.0001853
# p-value가 0.0001853으로 정규성을 따르지 않는다
#
#비모수검정
wilcox.test(our.height, mu=korea.woman.height, alternative = 'two.side', conf.int = 0.95 )
# Wilcoxon signed rank test
# with continuity correction
# 
# data:  our.height
# V = 826, p-value = 0.067
# alternative hypothesis: true location is not equal to 148.5
# 95 percent confidence interval:
#   148.5000 150.0001
# sample estimates:
#   (pseudo)median 
# 149.5 
# p-value= 0.067이므로.
# 대립가설 기각, 영가설이 채택
# 차이가 없다