"""
# practice 6.1
information = {
    'first_name': 'liu',
    'last_name': 'yang',
    'age': 34,
    'city': 'beijing'
}
print(information.get('first_name'))
print(information.get('last_name'))
print(information['age'])
print(information['city'])

# practice 6.2
like_nums = {}
like_nums['wusi'] = 1
like_nums['niudongcui'] = 2
like_nums['shankun'] = 3
like_nums['hanleilei'] = 4
for name in like_nums:
    print(f'{name} like {like_nums[name]}')

# practice 6.4
glossary = {'string': 'A series of characters.', 'comment': 'A note in a program that the Python interpreter ignores.',
            'list': 'A collection of items in a particular order.',
            'loop': 'Work through a collection of items, one at a time.',
            'dictionary': "A collection of key-value pairs.", 'conditional test': 'A comparison between two values.',
            'float': 'A numerical value with a decimal component.',
            'boolean expression': 'An expression that evaluates to True or False.',
            'key': 'The first item in a key-value pair in a dictionary.',
            'value': 'An item associated with a key in a dictionary.'}
for k,v in glossary.items():
    print(f"{k} means {v}")

# practice 6.5
rivers = {
    'nile': 'egypt',
    'changjiang': 'china',
    'huanghe': 'china',
}
for k,v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}.")
for k in rivers.keys():
    print(k)
for v in rivers.values():
    print(v)
for v in set(rivers.values()):
    print(v)

# practice 6.6
favorite_languages = dict(jen='python', sarah='c', edward='ruby', phil='python')
coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for being investigate,{coder}")
    else:
        print(f"invite you to join the investigate {coder}")

# practice 6.7
information1 = {
    'first_name': 'liu',
    'last_name': 'yang',
    'age': 34,
    'city': 'beijing',
}
information2 = {
    'first_name': 'shan',
    'last_name': 'kun',
    'age': 33,
    'city': 'tonghua',
}
information3 = {
    'first_name': 'han',
    'last_name': 'leilei',
    'age': 32,
    'city': 'nantong',
}
people = [information1, information2, information3]
for person in people:
    name = f"{person['first_name'].title()}{person['last_name'].title()}"
    age = person['age']
    city = person['city']
    print(f"{name} is {age} years old,live in {city}")

# practice 6.8
pets = []
# 定义宠物
pet = {
    'master': 'wusi',
    'leixing': 'cat',
    'weight': '13',
}
pets.append(pet)
pet = {
    'master': 'niudongcui',
    'leixing': 'dog',
    'weight': '16',
}
pets.append(pet)
pet = {
    'master': 'shankun',
    'leixing': 'fish',
    'weight': '1',
}
pets.append(pet)
for pet in pets:
    master = pet['master']
    leixing = pet['leixing']
    weight = pet['weight']
    print(f"{master.title()} have a {leixing},it's weight {weight}")

# practice 6.9
favorite_places = {
    'hanleilei': ['nantong', 'henan', 'beijing'],
    'wusi': ['liaoning', 'beijing'],
    'niudongcui': ['tonghua', 'yunnan', 'beijing'],
}
for k,v in favorite_places.items():
    print(f"{k.title()}'s favorite place are:")
    for place in v:
        print(f"-{place}")

# practice 6.10
like_nums = {
    'wusi': [1, 3, 4],
    'niudongcui': [2, 4, 5],
    'shankun': [5, 4, 7],
    'hanleilei': [8, 9, 0],
}
for name,numbers in like_nums.items():
    print(f"{name.title()} like number are here:")
    for number in numbers:
        print(f"---{number}")
"""
# practice 6.11
cities = {
    'beijing': {
        'country': 'china',
        'population': 1,
        'fact': 'zhengzhizhongxin',
    },
    'shanghai': {
        'country': 'china',
        'population': 2,
        'fact': 'jinrongzhongxin',
    },
    'guangzhou': {
        'country': 'china',
        'population': 3,
        'fact': 'jinchukou',
    },
}

