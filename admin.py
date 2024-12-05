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

