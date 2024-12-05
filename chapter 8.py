"""
# practice 8.1
def display_message():
    '''本章主题：函数'''
    print("this chapter is about hanshu")


display_message()

# practice 8.2
def favorite_book(title):
    '''喜欢的书'''
    print(f"One of my favorite book is {title.title()}")


favorite_book('python of 3')



# practice 8.3
def make_shirt(size, simple):
    '''discreb a shirt'''
    print(f"This shirt size is {size},it has a {simple}")


make_shirt(simple='cat', size=14)



# practice 8.4
def make_shirt(size, simple='i love python'):
    '''descreb a shirt'''
    print(f"This shirt size is {size},it has a {simple.title()}")


make_shirt(20, simple='i really love python')

# practice 8.5
def describe_city(city_name, country='china'):
    '''city'''
    print(f"{city_name.title()} is in {country.title()}")


describe_city('beijing')
describe_city(city_name='shanghai')
describe_city(country='iceland', city_name='reykjavik')

# practice 8.6
def city_country(city_name, country):
    '''chengshi-guojia'''
    cc = f"{city_name.title()}, {country.title()}"
    return cc


cc = city_country('beijing', 'china')
print(cc)

# practice 8.7
def make_album(singer,music,songs=None):
    '''zhuanji'''
    album = {
        'singer': singer,
        'music': music,
    }
    if songs:
        album['songs'] = songs
    return album


album = make_album('daolang','senlin')
print(album)
album1 = make_album('laolang','sss',21)
print(album1)

# practice 8.8
def make_album(singer,music,songs=None):
    '''zhuanji'''
    album = {
        'singer': singer,
        'music': music,
    }
    if songs:
        album['songs'] = songs
    return album


while True:
    print("\nplease give me a singer and music:")
    print("(enter 'q' at any time to quit)")
    singer = input("singer: ")
    if singer == 'q':
        break
    music = input("music: ")
    if music == 'q':
        break
    print(make_album(singer,music))

# practice 8.9
messages = ['liuyang', 'wusi', 'shankun', 'niudongcui', 'hanleilei']
def show_messages(messages):
    '''打印消息'''
    for message in messages:
        print(message)


show_messages(messages)

# practice 8.10 and 8.11
def show_messages(messages,sent_messages):
    '''打印消息'''
    print(messages,sent_messages)


def send_messages(messages,sent_messages):
    while messages:
        messsage = messages.pop()
        sent_messages.append(messsage)


messages = ['liuyang', 'wusi', 'shankun', 'niudongcui', 'hanleilei']
sent_messages = []
send_messages(messages,sent_messages)
show_messages(messages,sent_messages)

messages = ['liuyang', 'wusi', 'shankun', 'niudongcui', 'hanleilei']
sent_messages = []
send_messages(messages[:],sent_messages)
show_messages(messages,sent_messages)

# practice 8.12
def sandwitch(*args):
    for arg in args:
        print(f"you ordered a {arg} sandwitch")


sandwitch('luci')

# practice 8.13
def build_profile(first,last,**user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info


my_info = build_profile('liu','yang',
                        age=34,
                        job='software test engineer')
for k,v in sorted(my_info.items()):
    print(k,v)

# practice 8.14
def car_info(maker,model,**kwargs):
    kwargs['maker'] = maker
    kwargs['model'] = model
    return kwargs


car = car_info('subaru', 'outback',
               color='red',
               tow_package=True,
               )
print(car)
"""
# practice 8.15
def make_shirt(size,character='l love python'):
    '''describe the function'''
    print(f"i have a t-shirt {size},and it's has {character.title()}")
make_shirt(34,'l really love python')