"""
# practice 5.2
str1 = 'l love motocyble'
str2 = 'l love car'
if str1 == str2:
    print(True)
else:
    print(False)

# practice 5.3
alien_color = 'green'
if alien_color == 'green':
    print("you scored 5 point")

# practice 5.4
alien_color = 'red'
if alien_color == 'green':
    print("you scored 5 point")
else:
    print("you scored 10 point")

# practice 5.5
alien_color = 'red'
if alien_color == 'green':
    print("you scored 5 point")
elif alien_color == 'yellow':
    print("you scored 10 point")
elif alien_color == 'red':
    print("you scored 15 point")

# practice 5.6
favorite_fruits = ['apple', 'banana', 'watermelon']
if 'banana' in favorite_fruits:
    print('you really like banana')

# practice 5.8
guest_list = ['wusi', 'niu dongcui', 'han leilei', 'shankun', 'admin']
for guest in guest_list:
    if guest == 'admin':
        print(f'Hello {guest},would you like to see a status report?')
    else:
        print(f'Hello {guest},thank you for logging in again.')

# practice 5.9
guest_list = ['wusi', 'niu dongcui', 'han leilei', 'shankun', 'admin']
# guest_list = []
if guest_list:
    for guest in guest_list:
        if guest == 'admin':
            print(f'Hello {guest},would you like to see a status report?')
        else:
            print(f'Hello {guest},thank you for logging in again.')
else:
    print('We need find some users!')

# practice 5.10
current_users = ['Wusi', 'niu dongcui', 'Han leilei', 'shankun', 'Admin']
current_users_lower = [cur_user.lower for cur_user in current_users]

new_users = ['liuyang', 'Niu Dongcui', 'xie yuyuan', 'liuyan', 'admin']
for user in new_users:
    if user.lower() in current_users_lower:
        print(f'{user} has been used')
    else:
        print(f'{user} is not been used')
"""
# practice 5.11
num_list = list(range(1,10))  # 学到了
for num in num_list:
    if num == 1:
        print(f'{num}st')
    elif num == 2:
        print(f'{num}nd')
    elif num == 3:
        print(f'{num}rd')
    else:
        print(f'{num}th')
