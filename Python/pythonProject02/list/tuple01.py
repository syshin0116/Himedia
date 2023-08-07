# tuple은 read_only한 리스트를 만들때 사용

food_list = ['커피', '물', 'orange']
food_list2 = tuple(food_list)
# food_list2[0] = 'icecream'
print(food_list2)


def yes():
    x = 100
    y = 200
    return x, y


result = yes()
result2 = list(result)
print(result2)

