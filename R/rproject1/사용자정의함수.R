## 내장된 함수(built-in)
jumsu = c(1, 7, 4, 2, 3, 9)

print(sort(jumsu)) ## 비파괴 함수
# > print(sort(jumsu))
# [1] 1 2 3 4 7 9

print(jumsu)
# > print(jumsu)
# [1] 1 7 4 2 3 9


jumsu.2 = sort(jumsu) ##오름차순 정렬  
print(jumsu.2)
jumsu.3 = sort(jumsu, decreasing = TRUE) 
##내림차순 정렬  
print(jumsu.3)

jumsu.4 = sort(jumsu, TRUE) 
print(jumsu.4)

str <- paste('굿', '모닝', sep = ' ')
print(str)
str.2 <- paste('굿', '모닝', '굿', '나잇', sep = ' ')
print(str.2)
## 파이썬에서는 브로드캐스팅! 
str.3 <- paste(1:12,'월',sep = '')
print(str.3)

## 사용자 정의 함수(user-defined) => ppt(409)
mysum <- function(x){
  result <-  x + 100
  return(result)
}

sum1 <- mysum(1000)
cat('100을 더한 결과는 ', sum1)

## 두 수를 더해서 결과값을 받아오는 함수를 정의
mysum2 <- function(x, y){
  result = x + y
  return(result)
}
## 200, 300 => 더한 결과값 출력(1) 
sum2 <- mysum2(200, 300)
print(sum2)
## 5555, 3333 => 더한 결과값 출력(2)
sum3 <- mysum2(5555, 3333)
print(sum3)
## 1과 2번을 더해서 다시 출력(3)
sum4 <- mysum2(sum2, sum3)
print(sum4)

install.packages('svDialogs')
library(svDialogs) # import!역할 

data.1 <-  dlgInput('숫자1입력 ')$res
data.2 <-  dlgInput('숫자2입력 ')$res
n1 <- as.numeric(data.1)
n2 <- as.numeric(data.2)
print(n1 + n2) ##위에서 만들었던 함수를 적용해서 구해보세요.
print(mysum2(n1, n2))
print(mysum2(x = n1, y = n2))

mysum3 <- function(x, y=1000){ #default값!
  #함수를 호출할 때 넣지 않으면, default값을 사용
  result = x + y
  return(result)
}
print(mysum3(555,666))
print(mysum3(555))

mysum.minus <- function(x, y){
  s1 <- x + y
  m1 <- x - y
  return(list(s = s1, m = m1))
}

result1 <- mysum.minus(888, 111)
print(result1)
cat('두 수의 더한값은 ', result1$s)
cat('두 수의 뺀 값은 ', result1$m)

# class(result1)
# [1] "list"

## 사용자 이름 입력
## 사용자 키 입력
## 사용자 "적정 몸무게와 비율(0.9)" 구하는 함수를 정의
## 사용자 몸무게 입력
## 적정 몸무게와 사용자 몸무게 비교 결과 다음과 같이 
## 프린트 
## '홍길동의 몸무게는 0.9를 곱한 결과 
## 초과(또는 미달)입니다.
## 적정 몸무게 = (신장 - 100) × 0.9



weight.for.height <- function(height){
  result <- (height-100)*0.9
  return(result)
}
you.are <- function(name){
  data.weight <-  dlgInput('몸무게입력 ')$res
  data.height <-  dlgInput('키 입력 ')$res
  weight <- as.numeric(data.weight)
  height <- as.numeric(data.height)
  result <- weight.for.height(height)
  if (weight>result){
    cat(name,'의 몸무게는 0.9를 곱한 결과 초과입니다')
  }else if(weight==result){
    cat(name,'의 몸무게는 0.9를 곱한 결과 정상입니다')
  }else{
    cat(name,'의 몸무게는 0.9를 곱한 결과 미만입니다')
  }
}

you.are('홍')
