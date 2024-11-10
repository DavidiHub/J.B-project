
from models.user_model import *
from utils.dal import DAL




class UserLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_users(self):
        sql = 'select * from mydb.users'
        result = self.dal.get_table(sql)
        users = UserModel.dictionaries_to_users(result)
        return users
    
    def get_one_user(self, email, password):
        sql = 'select * from mydb.users where email = %s and password = %s'
        result = self.dal.get_one(sql, (email, password, ))
        if result is None: return None
        user = UserModel.dictionary_to_user(result)
        return user
    
    def get_one_like(self, like_id):
        sql = ' select user_id from mydb.likes where like_id=%s'
        result = self.dal.get_one(sql, (like_id, ))
        if result is None: return None
        return result['user_id']
    
    def insert_user(self, user):
        sql = 'insert into mydb.users (first_name, last_name, email, password, role_id) values (%s, %s,%s, %s, %s)'
        last_inserted_id = self.dal.insert(sql, (user.first_name, user.last_name, user.email, user.password, user.role_id, ))
        return last_inserted_id
    
    def is_email_exist(self, email):
        sql = 'select email from mydb.users where email = %s'
        result = self.dal.get_one(sql, (email, ))
        if result is None: return False
        return True
    
    def login(self, email, password):
        sql = 'select * from mydb.users where email =%s and password =%s'
        result = self.dal.get_one(sql, (email, password, ))
        if result is None:return False
        user = UserModel.dictionary_to_user(result)
        return user
    
    def insert_like(self, user_id, vacation_id):
        sql = 'insert into mydb.likes (user_id, vacation_id) values (%s, %s)'
        last_inserted_id = self.dal.insert(sql, (user_id, vacation_id, ))
        return last_inserted_id
    
    def delete_like(self, id):
        sql = 'delete from mydb.likes where like_id = %s'
        row_count = self.dal.delete(sql, (id, ))
        return row_count
    
    

    


    
