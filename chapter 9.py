"""
# practice 9.1
class Restaurant:
    '''定义餐馆'''

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化属性'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''方法1'''
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type}")

    def open_restaurant(self):
        '''方法2'''
        print(f"{self.restaurant_name} is open")


restaurant = Restaurant('xibei','chinese')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# practice 9.2
class Restaurant:
    '''定义餐馆'''

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化属性'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''方法1'''
        print(f"\n{self.restaurant_name.title()} is a {self.cuisine_type}")

    def open_restaurant(self):
        '''方法2'''
        print(f"{self.restaurant_name} is open")


rest1 = Restaurant('xibei','china')
rest2 = Restaurant('heiniu','japan')
rest3 = Restaurant('pizza','italy')

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()

# practice 9.3
class User:
    '''user类'''

    def __init__(self,first_name,last_name,*args):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.arg = args

    def describ_user(self):
        '''user info'''
        print(f"{self.first_name}{self.last_name}")
        for info in self.arg:
            print(f"{info}")

    def greet_user(self):
        '''say hello'''
        print(f"Hello,{self.first_name}{self.last_name}")


user1 = User('wu','si',
             36,
             'female',
             )
user1.describ_user()
user1.greet_user()

# practice 9.4
class Restaurant:
    '''定义餐馆'''

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化属性'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''方法1'''
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type}")

    def open_restaurant(self):
        '''方法2'''
        print(f"{self.restaurant_name} is open")

    def set_number_served(self,num):
        self.number_served = num

    def increment_number_served(self,update_num):
        self.number_served += update_num


restaurant = Restaurant('xibei','china')
restaurant.set_number_served(6)
print(restaurant.number_served)
restaurant.increment_number_served(4)
print(restaurant.number_served)

# practice 9.5
class User:
    '''user类'''

    def __init__(self,first_name,last_name,*args):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.arg = args
        self.login_attempts = 0

    def describ_user(self):
        '''user info'''
        print(f"{self.first_name}{self.last_name}")
        for info in self.arg:
            print(f"{info}")

    def greet_user(self):
        '''say hello'''
        print(f"Hello,{self.first_name}{self.last_name}")

    def increment_login_attemps(self):
        '''递增'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('wu','si',36)
user.increment_login_attemps()
print(user.login_attempts)
user.increment_login_attemps()
print(user.login_attempts)
user.increment_login_attemps()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

# practice 9.6
class Restaurant:
    '''定义餐馆'''

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化属性'''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''方法1'''
        print(f"{self.restaurant_name.title()} is a {self.cuisine_type}")

    def open_restaurant(self):
        '''方法2'''
        print(f"{self.restaurant_name} is open")

    def set_number_served(self,num):
        self.number_served = num

    def increment_number_served(self,update_num):
        self.number_served += update_num


class IceCreamStand(Restaurant):
    '''冰淇淋小馆'''

    def __init__(self,restaurant_name,cuisine_type):
        '''初始化冰淇淋小馆'''
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['apple','banana','watermelon']

    def icecream_taste(self):
        '''显示口味'''
        print("we have the following flavors:")
        for flavor in self.flavors:
            print(f"-{flavor}")


icecream = IceCreamStand('mixuebingcheng','previte')
icecream.icecream_taste()
icecream.describe_restaurant()

# practice 9.8
class User:
    '''user类'''

    def __init__(self,first_name,last_name,*args):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.arg = args
        self.login_attempts = 0

    def describe_user(self):
        '''user info'''
        print(f"{self.first_name}{self.last_name}")
        for info in self.arg:
            print(f"{info}")

    def greet_user(self):
        '''say hello'''
        print(f"Hello,{self.first_name}{self.last_name}")

    def increment_login_attempts(self):
        '''递增'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    '''管理员类'''

    def __init__(self,first_name,last_name,*args):
        '''初始化管理员类'''
        super().__init__(first_name,last_name,*args)
        self.privileges = Privileges()


class Privileges:
    '''权限'''

    def __init__(self,privileges=[]):
        '''初始化属性'''
        self.privileges = privileges

    def show_privileges(self):
        '''管理员权限'''
        print("Admin have the following privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("The user has no privileges")


user = Admin('liu','yang',34)
user.privileges.show_privileges()
user.privileges.privileges = ['can add post', 'can delete post', 'can ban user']
user.privileges.show_privileges()

# practice 9.9
class Car:
    '''一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year):
        '''初始化汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describ_name(self):
        '''返回汽车描述'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        '''显示汽车里程'''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        '''将里程设定为指定的值'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self,miles):
        '''增加里程'''
        self.odometer_reading += miles


class Battery:
    '''定义一个电池'''

    def __init__(self,battery_size=40):
        '''初始化电池属性'''
        self.battery_size = battery_size

    def descirb_battery(self):
        '''描述电池信息'''
        print(f"This car has a {self.battery_size}-KWh battery")

    def get_range(self):
        '''指出电池的续航里程'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size ==65:
            range = 225

        print(f"This car can go about {range} mile on a full charge.")

    def upgrade_battary(self):
        '''检查电池的容量'''
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    '''电动车'''

    def __init__(self,make,model,year):
        '''
        初始化父类的属性,定义电动车自己的属性
        '''
        super().__init__(make,model,year)
        self.battery = Battery()


my_leaf = ElectricCar('biyadi','leaf',2023)
my_leaf.battery.descirb_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battary()
my_leaf.battery.descirb_battery()
my_leaf.battery.get_range()

# practice 9.10
from restaurant import Restaurant as Rt

simple = Rt('xibei', 'kuaican')
simple.describe_restaurant()

# practice 9.11
from admin import User, Admin, Privileges

user = Admin('liu','yang',34)
user.privileges.show_privileges()
user.privileges.privileges = ['add','delete','reset','search']
user.privileges.show_privileges()

# practice 9.12
from admin_pr import Admin

user = Admin('liu', 'yang', 34)
user.privileges.show_privileges()
user.privileges.privileges = ['add', 'delete', 'reset', 'search']
user.privileges.show_privileges()

# practice 9.13
from random import randint


class Die:
    '''骰子'''

    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        '''打印随机数'''
        return randint(1,self.sides)


touzi = Die()
for i in range(10):
    print(touzi.roll_die(),end=' ')
touzi = Die(20)
print("\n创建一个20面的骰子")
for i in range(10):
    print(touzi.roll_die(),end=' ')
"""
class User:
    '''user类'''

    def __init__(self,first_name,last_name,*args):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.arg = args
        self.login_attempts = 0

    def describ_user(self):
        '''user info'''
        print(f"{self.first_name}{self.last_name}")
        for info in self.arg:
            print(f"{info}")

    def greet_user(self):
        '''say hello'''
        print(f"Hello,{self.first_name}{self.last_name}")

    def increment_login_attemps(self):
        '''递增'''
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('liu','yang')
i = 0
while i < 4:
    user.increment_login_attemps()
    print(user.login_attempts)
    i += 1
user.reset_login_attempts()
print(user.login_attempts)