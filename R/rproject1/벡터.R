name.list = c('hong', 'kim', 'song')
print(name.list)
age.list = c(100,200,50)
print(age.list)
cat(age.list)

weight.list =100:200
print(weight.list)

print(weight.list[0])
print(weight.list[1])
print(weight.list[1:5])
print(weight.list[c(1,3,5)])

# 9,11~15,25,30~33
run.list <- c(9, 11:15, 25, 30:33)

# 전체 index의 시작~끝 번호 확인
print(run.list)
# index: start(1), end(11)
# 첫번쨰 값, 마지막 값의 차이를 구해보세요.
start = run.list[1]
end = run.list[11]
diff = end-start
cat('달리기 속도는', diff)
# age, wieght, run평균
cat('age평균:', mean(age.list),'weight평균:', mean(weight.list),'run평균:', mean(run.list))

s5 <- seq(1,6,2)
print(s5)
v5 <- rep(1,times=5)
print(v5)
v8 <- rep(c(a,b,c) each=a,b,c)

term.1 <-  c(90,100,80,75)
print(term.1)
names(term.1) <- c('국어', '영어', '수학', '컴퓨터')
print(term.1[1])
print(term.1['국어'])

### 수정해보세요
### 국어점수 99
### 수학점수 88
### 국어, 수학 점수 프린트

term.1['국어'] <- 99
term.1['수학'] <- 88
cat(term.1['국어'], term.1['수학'])
