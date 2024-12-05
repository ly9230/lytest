from admin import User


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

