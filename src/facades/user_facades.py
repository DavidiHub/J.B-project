from logic.user_logic import *
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


class UserFacade():
    def __init__(self):
        self.logic = UserLogic()


    def get_all_users(self):
        users = self.logic.get_all_users()
        return users
    
    def get_one_user(self, email, password):
        user = self.logic.get_one_user(email, password)
        return user
    
    def insert_user(self, first_name: str, last_name: str, email: str, password: str):
        # login_result = UserFacade().login()
        # if login_result.role_id != 1:
        #     raise ValueError('Eror: only admin can add users ')
        if first_name is None or last_name is None or email is None or password is None:
            raise TypeError('Eror: all fields are required')
        if not UserFacade().email_check(email):
            raise ValueError('Eror: invalid email')
        if len(password) < 4:
            raise TypeError('Eror: password must be at least 4 chars long')
        if UserFacade().is_email_exist(email):
            raise ValueError('Eror: Email already exist')
        user = UserModel(None , first_name, last_name, email, password, 2)
        self.logic.insert_user(user)
        print(f'registration succesful')
        return user
    
    def is_email_exist(self, email):
        result = self.logic.is_email_exist(email)
        return result
    
    # def insert_like(self, user_id, vacation_id):
    #     like_id = self.logic.insert_like(user_id, vacation_id)
    #     return like_id
    
    # def delete_like(self, id):
    #     row_count = self.logic.delete_like(id)
    #     return row_count
    
    def login(self):
        email = input('Email: ')
        password = input('Password: ')
        if email is None or password is None:
            raise TypeError('Eror: all fields are required')
        if len(password) < 4:
            raise ValueError('Eror: password must be at least 4 characters long ')
        if not UserFacade.email_check(email):
            raise ValueError('Eror: invalid Email')
        row_count = self.logic.login(email, password)
        if row_count is False: return False
        else:
            print('login succes')
        return row_count
    
    def like_a_vacation(self):
        user = UserFacade().login()
        if user is False:
            raise ValueError('Error: Login Failed')
        elif user.role_id == 1:
            raise ValueError('Eror: Admin can not add Likes')
        vacation_id = input('insert vacation id to like a vacation: ')
        self.logic.insert_like(user.user_id,vacation_id)
        print('Like added succesfully')
        



    # def like_a_vacation_v2(self):
    #     email = input('Email: ')
    #     if not UserFacade.email_check(email):
    #         raise ValueError('invalid Email')
    #     password = input('Password: ')
    #     user = self.logic.get_one_user(email, password)
    #     if user.role_id == 1:
    #         raise ValueError('Admin can not add Like')
    #     login_result = UserFacade().login()
    #     if login_result == False:
    #         print('you are not registered')
    #         return None
    #     else:
    #         vacation_id = input('insert vacation id to like a vacation: ')
    #         self.logic.insert_like(user.user_id,vacation_id)
    #         print('Like added succesfully')

    def unlike_a_vacations(self):
        user = UserFacade().login()
        if user is False:
            raise ValueError('Eror: you are not registered')
        elif user.role_id == 1:
            raise ValueError('Eror: admin can not unlike a vacations ')
        like_id = input('Which Like would you want to delete? ')
        if user.user_id == self.logic.get_one_like(like_id):
            self.logic.delete_like(like_id)
            print('Like deleted succesfully')
            return True
        else:
            print('You are not authorized to delete this like')
            return None
        
        

    # def unlike_a_vacation_v2(self):
    #     email = input('Email: ')
    #     if not UserFacade.email_check(email):
    #         raise ValueError('invalid Email')
    #     password = input('Password: ')
    #     user = self.logic.get_one_user(email, password)
    #     if user.role_id == 1:
    #         raise ValueError('Admin can not unlike vacations ')
    #     login_result = UserFacade().login(email, password)
    #     if login_result == False:
    #         print('you are not registered')
    #         return None
    #     else:
    #         like_id = input('Which Like would you want to delete? ')
    #         if user.user_id == self.logic.get_one_like(like_id):
    #             self.logic.delete_like(like_id)
    #             print('Like deleted succesfully')
    #             return True
    #         else:
    #             print('You are not authorized to delete this like')
    #             return None







    
    @staticmethod
    def email_check(email):
        if(re.fullmatch(regex, email)):
            return True
 
        else:
            return False
        
