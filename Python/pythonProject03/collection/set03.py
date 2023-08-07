title = ['영어', '수학', '국어', '컴퓨터']
term1 = [100, 99, 88, 77]
# 2학기 점수는 1학기와 거의 동일하다.
# 국어점수만 66점으로 됨.
# 1학기보다 성적이 떨어진 과목은?
# 1, 2학기 점수가 동일한 과목은?
term2 = term1.copy()
term2[2] = 66
print(term1)
print(term2)

# 1학기보다 성적이 떨어진 과목은?
for i in range (len(term1)): #index
    if term1[i] > term2[i]:
        print(title[i])

# 1, 2학기 점수가 동일한 과목은?
for i in range (len(term1)): #index
    if term1[i] == term2[i]:
        print(title[i], end=' ')

dict1 = dict()
#dict1 = dict(zip(title, term1))

for i in range (len(title)):
     dict1[title[i]] = term1[i]

print(dict1)