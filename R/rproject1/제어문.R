result2[1:2] <- 55:66
print(result2)

## 각각의 값들이 짝수인지 판별해서, 'even', 'odd'

values = c(99, 22, 44, 55, 88, 77, 11, 33)
result3=c()
length(values) # vector의 개수

for (x in values){
  if (x%%2==0){
    result3 <- c(result3,'even')
  }else{# 홀수
    result3 <- c(result3,'odd')
  }
}

print(result3)

# 입력값 받아서 names3에 누적시켜보세요.
install.packages('scan')
library(scan) # import!역할 

names3 <- c()
# library(svDialogs) # import!역할 
# name <-  dlgInput('이름입력 ')$res

for (x in 1:length(values)){
  n <- readline('name input>> ')
  names3 <- c(names3,n)
}
print(names3)

df <- data.frame(names3, values, result3)
print(df)
print(class(df))#자료구조 학인
print(class(values))
str(df)
dim(df)
head(df,3)
tail(df,2)
df[1,]
df[1,1]
df[1:2,1:2]

#행(1,3,5), 열(1,3)
df[c(1,3,5),c(1,3)]

df2 <- subset(df,result3 =='even')
print(df2)
# df에서 values가 50이상
subset(df,values>=50)

# df에서values가 50미만이면서 result3가 even인것을 찾아서 df3에 저장
df3 <- subset(df,(values<50) & (result3=='even'))
print(df3)

df
df$names3
df.names3 <- df$names3 ### !!!!
str(df.names3)
df.names33 <- df['names3']
typeof(df.names33)
str(df.names33)
mode(df.names3)
table(df$names3)

df
df[1,1] <-  'kim'
df

df3 <- table(df$names3)
df3

library(ggplot2)
ggplot(df,aes(x=names3,y=values)) + geom_point()

## 5명의 정보를 데이터프레임에 넣어서, 그래프로 그려주세요
names <- c('kim', 'lee', 'park', 'song', 'shin')
age <- c()
computer <- c()
english <- c()
for (x in 1:length(names)){
  n <- readline('age input>> ')
  age <- c(age,as.integer(n))
}
for (x in 1:length(names)){
  n <- readline('computer score input>> ')
  computer <- c(computer,as.integer(n))
}
for (x in 1:length(names)){
  n <- readline('english score input>> ')
  english <- c(english,as.integer(n))
}
df <- data.frame(names, age, computer, english)

##df에서 추출(각 항목을 추출하여 프린트)
df$names
df$age
df$computer
df$english
## 이름에 해당하는 나이를 그래프로 그려보세요.

ggplot(df,aes(x=names,y=age)) + geom_point()

## df에서 추출한 나이의 평균을 구해보세요.
age <- as.integer(age)
english <- as.integer(english)
computer <- as.integer(computer)
print(age)
df.age <- df['age']
print(df.age)
typeof(df.age)
mean(age)
age.avg <- mean(age)
print(age.avg)
## df에서 추출한 영어점수의 최고 점수를 구해보세요.e
english <- as.integer(english)
max(english)
## df의 3번째 행, 3번째 열의 값을 프린트
df[3,3]
## df의 1~3행, (2,4)열 값들을 프린트
df[1:3,c(2,4)]
## 영어점수가 평균보다 높은 사람들만 새로운 df_new로 저장
english.avg <- mean(english)
print(english.avg)
df['english']
df_new <- subset(df, english>=english.avg)
df_new
## ————————————————————————
## 컴퓨터점수와 영어점수를 합해서 total컬럼 생성
total <- computer+english
print(total)
df <- data.frame(names, age, computer, english, total)
df
## total이 150점 이상이면 우수, 100점 이상이면 보통, 아니면 미달의
## 값이 들어가는 result컬럼을 추가.
total.avg <- mean(total)
result <- c()
for(x in 1:length(df['total'])){
  if(df[x,'total']>150){
    df[x,'result'] <- '우수!'
  }else if(df[x,'total']==100){
    df[x,'result'] <- '보통!'
  }else{
    df[x,'result'] <- '미달!'
    }
}
df
## 최종 df의 내용과 행과 열의 개수 프린트
## 최종 만들어진 df를 csv(df_csv.csv)로 저장
## 저장된 csv를 읽어와서 프린트

