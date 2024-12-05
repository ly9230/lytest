"""
#practice 4.1
pisas = ['bige','dameile','bishengke']
for pisa in pisas:
    print(f'i like {pisa.title()} pisa.')
print('i really love pisa!')

# practice 4.3
for value in range(1,21):
    print(value)

#practice 4.4
nums = []
for num in range(1,1000001):
    nums.append(num)
print(nums)

#practice 4.5
nums = []
for num in range(1,1000001):
    nums.append(num)
print(min(nums))
print(max(nums))
print(sum(nums))

#practice 4.6
nums = []
for num in range(1,20,2):
    nums.append(num)
print(nums)

#practice 4.7
nums = []
for num in range(3,30,3):
    nums.append(num)
print(nums)

#practice 4.8
nums = []
for num in range(1,11):
    num = num**3
    nums.append(num)
print(nums)

#practice 4.9
nums = [num**3 for num in range(1,11)]
print(nums)

#practice 4.10
my_food = ['pizza','falafel','carrot cake','hongshao paigu']
friend_food = my_food[:]
my_food.append('ice cream')
print('The first three items in the list are:')
print(my_food[:3])
print("Three items from the middle in the list are:")
print(my_food[1:4])
print("The last three items in the list are:")
print(my_food[-3:])

#practice 4.11
my_pizza = ['bige','dameile','bishengke']
friend_pizza = my_pizza[:]
my_pizza.append('buzhidao')
friend_pizza.append('meiyoule')
print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

#practice 4.13
foods = ('jiaozi','baozi','miaotiao','gaifan','huoguo')
for food in foods:
    print(food)
foods = ('jiaozi','baozi','miaotiao','liangpi','roujiamo')
for food in foods:
    print(food)
"""
# practice 4.13
