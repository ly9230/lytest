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

