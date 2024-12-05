"""
# practice 7.1
message = input("What kind of car would you like? ")
print(f"Let me see if I can find you a {message.title()}")

# practice 7.2
message = input("how many people will come? ")
message = int(message)
if message > 8:
    print(f"sorry, we don't have empty table")
else:
    print("we have empty table")

# practice 7.3
num = input("please input a number: ")
num = int(num)
if num % 10 == 0:
    print(f"you num {num} is a multiple of 10")
else:
    print(f"the num {num} is not 10 beishu")

# practice 7.4
toppings = "\nplease enter your topping:"
toppings += "\nIf you ordered enough,enter 'quit': "
message = ""
while message != 'quit':
    message = input(toppings)
    if message != 'quit':
        print(f"you ordered {message}")

# practice 7.5
active = True
while active:
    message = input("\ngive me your age please.\nenter 'quit' to quit: ")
    if message == 'quit':
        active = False
        continue
    message = int(message)
    if message < 3:
        print("\tyou are free")
    elif 3 <= message < 12:
        print("\tyou ticket is 10 dolors")
    elif message >= 12:
        print("\tyour ticket is 15 dolors")

# practice 7.6
while True:
    message = input("\ngive me your age please.\nenter 'quit' to quit: ")
    if message == 'quit':
        break
    message = int(message)
    if message < 3:
        print("\tyou are free")
    elif 3 <= message < 12:
        print("\tyou ticket is 10 dolors")
    elif message >= 12:
        print("\tyour ticket is 15 dolors")

# practice 7.8
sandwich_orders = ['tuna', 'lada', 'dota']
finished_sandwich = []
while sandwich_orders:
    # 移除的
    order = sandwich_orders.pop()
    print(f"I made you {order} sandwich.")

    finished_sandwich.append(order)
print("\nYour sandwich is ready.")
for sandwich in finished_sandwich:
    print(sandwich)

# practice 7.9
sandwich_orders = ['tuna', 'pastrami', 'lada', 'pastrami', 'dota', 'pastrami']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
if 'pastrami' not in sandwich_orders:
    print("Sorry,pastrami is sell out")
"""
# practice 7.10
vication = {}
while True:
    print("If you could visit ont place in the world,where would you go?")
    name = input("what is your name? ")
    place = input("the place you will visit? ")
    vication[name] = place

    repeat = input("will you like to invite another person?(yes/no)")
    if repeat == 'no':
        break
    else:
        continue
for k,v in vication.items():
    print(f"{k.title()} would like to {v}")
