my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # 深拷贝还是浅拷贝

print("My favorite foods are:")
my_foods[1] = 'apple'
print(my_foods)
print(friend_foods)