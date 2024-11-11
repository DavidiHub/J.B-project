from models.user_model import *
from logic.user_logic import *
from facades.user_facades import *
from facades.vacation_facades import *
import datetime

user_facade = UserFacade()
vacation_facade = VacationFacade()


class Test:
    def test_all():
        def register(first_name, last_name, email, password):
            user_facade.insert_user(first_name, last_name, email, password)

        def login():
                user_facade.login()
            
        def get_all_vacations():
                vacation_facade.get_all_vacations()

        def add_vacation(discription, start_date, end_date, price):
            country_id = int(input('''select country:\nfor Barbados - 1\nfor Italy - 2\nfor Germany - 3\nfor Cyprus - 4
for Japan - 5\nfor France - 6\nfor Yemen - 7\nfor United-States - 8\nfor Israel - 9\nfor Austria - 10\nanswer: '''))
            vacation_facade.insert_vacation(country_id, discription, start_date, end_date, price, file_name=None)

        def update_vacation(discription, start_date, end_date, price, vacation_id):
            country_id = int(input('''select country:\nfor Barbados - 1\nfor Italy - 2\nfor Germany - 3\nfor Cyprus - 4
for Japan - 5\nfor France - 6\nfor Yemen - 7\nfor United-States - 8\nfor Israel - 9\nfor Austria - 10\nanswer: '''))
            vacation_facade.update_vacation(country_id, discription, start_date, end_date, price, vacation_id)

        def delete_vacation():
             get_all_vacations()
             vacation_id = int(input('which vacation would you like to delete? '))
             vacation_facade.delete_vacation(vacation_id)
        
        def like_a_vacation():
             user_facade.like_a_vacation()

        def unlike_vacation():
             user_facade.unlike_a_vacations()



        try:
            # register('Hen', 'Danino', 'Hendanino@gmail.com', '123456')
            # register('Asaf', 'Simpson', 'asaf@gmail.com', '9876')
            # login()
            # get_all_vacations()
            # add_vacation('sri-lanka', datetime.datetime(day=2, month=1, year=2028), datetime.datetime(day=10, month=1, year=2028), 5209)
            # update_vacation('Tokyo', datetime.datetime(day=5, month=9, year=2025), datetime.datetime(day=24, month=10, year=2026), 7000, 4)
            # delete_vacation()
            # like_a_vacation()
            # unlike_vacation()
            print('thank you! ')
            
            
        except ValueError as arr:
            print(arr)
        except TypeError as arr:
            print(arr)
        except Exception as arr:
            print(arr)