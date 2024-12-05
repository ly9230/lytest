"""
# practice 10.1
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text(encoding='utf-8')
print(contents.rstrip())

lines = contents.splitlines()
for line in lines:
    print(line)

# practice 10.2
from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text(encoding='utf-8')
for line in contents.splitlines():
    line = line.replace('Python', 'C')
    print(line)

# practice 10.4
from pathlib import Path
name = input("Please enter your name: ")
path = Path('guest.txt')
path.write_text(name)

# practice 10.5
from pathlib import Path

path = Path("guest_book.txt")
name = ''
while True:
    names = input("Please enter your name:\nyou can enter 'q' to exit: ")
    if names != 'q':
        name += f"{names}\n"
    else:
        break
path.write_text(name)

# practice 10.6 and 7
print("Please give me two number:")
print("enter 'q' to exit")
while True:
    try:
        first_num = input("\nfirst number: ")
        if first_num == 'q':
            break
        else:
            first_num = int(first_num)
        second_num = input("\nsecond number: ")
        if second_num == 'q':
            break
        else:
            second_num = int(second_num)
    except ValueError:
        print("please enter a number")
    else:
        sums = first_num + second_num
        print(f"The sum of {first_num} and {second_num} is {sums}")

# practice 10.8 and 9
from pathlib import Path

anomals_file = ['cats.txt', 'dogs.txt']
for anomal in anomals_file:
    path = Path(anomal)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print("The file is not exist")
        pass
    else:
        print(contents)

# practice 10.10
from pathlib import Path

books_list = ['A Book of Christmas Verse.txt', 'Guatemala.txt']
for book in books_list:
    path = Path(book)
    contents = path.read_text(encoding='utf-8')
    the_count = contents.lower().count('the ')
    print(the_count)

# practice 10.11
from pathlib import Path
import json

path = Path('like_num.txt')
if path.exists():
    contents = path.read_text(encoding='utf-8')
    num = json.loads(contents)
    print(f"I know your favorite number! It's {num}")
else:
    num = input("please enter a number you like: ")
    contents = json.dumps(num)
    path.write_text(contents)
    print(f"I know your favorite number! It's {num}")

# practice 10.12
from pathlib import Path
import json


def get_sorted_username(path):
    """"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None


def get_new_username(path):
    """"""
    username = input("what is your name? ")
    age = input("what is your age? ")
    gender = input("what is your gender? ")
    user_dict = {
        'username': username,
        'age': age,
        'gender': gender,
    }
    contents = json.dumps(user_dict)

    path.write_text(contents)
    return user_dict


def greet_user():
    """"""
    path = Path('username.json')
    user_dict = get_sorted_username(path)
    if user_dict:
        print(f"welcome back,{user_dict['username']}")
        print(f"you are {user_dict['age']} years old")
        print(f"seems like you are {user_dict['gender']}")
    else:
        user_dict = get_new_username(path)
        print(f"we'll remember you when you come back,{user_dict}")


greet_user()
"""
# practice 10.14
from pathlib import Path
import json

def square(x) :         # 计算平方数
    return x ** 2
lis =  [1,2,3,4,5]
new_list = map(square,lis)
print(new_list)