from logic.vacation_logic import *
import datetime

class VacationFacade():
    def __init__(self):
        self.logic = VacationLogic()

    list_of_countries = ['placeholder', 'Barbados', 'Italy', 'Germany', 'Cyprus', 'Japan', 'France', 'Yemen', 'United-States', 'Israel', 'Austria']



        

    def get_all_vacations(self):
        vacations = self.logic.get_all_vacations()
        for vacation in vacations:
            print(vacation.vacation_id, self.list_of_countries[vacation.country_id], vacation.vacation_discription, vacation.vacation_start_date,
                   vacation.vacation_end_date,vacation.price, vacation.file_name)


    
    def insert_vacation(self, country_id, discription: str, start_date: datetime, end_date: datetime, price: int, file_name) -> int:        
        if country_id not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]: #(list)range(1,10)
            raise ValueError('Eror: country must be represented as a digit between 1-10')
        if  type(discription) is not str:
            raise ValueError('Eror: discription must be a string')
        if price > 10000 or price < 0:
            raise ValueError('Eror: Price can not be above 10,000 or below 0')
        if start_date > end_date:
            raise ValueError('Eror: end date of the vacation can not be sooner than its start date')
        if start_date < datetime.datetime.now():
            raise ValueError('Eror: Vacation date expired')
        vacation = VacationModel(None, country_id, discription, start_date, end_date, price, file_name)
        result = self.logic.insert_vacation(vacation)
        print(f'{discription} vacation been added')
        return result
    
    def get_a_vacation(self, id):
        vacation = self.logic.get_vacation(id)
        return vacation

    def update_vacation(self, country_id: int, discription: str, start_date: datetime,
                         end_date: datetime, price: int, vacation_id_to_change: int):
        if country_id is None or discription is None or start_date is None or end_date is None or price is None or vacation_id_to_change is None:
            raise TypeError('Eror: all fields are required')
        if price < 0 or price > 10000:
            raise ValueError('Eror: price can not be lower than 0 or higher than 10,000')
        if start_date > end_date:
            raise ValueError('Eror: end date of the vacation can not be sooner than its start date')
        vacation = VacationModel(vacation_id_to_change, country_id, discription, start_date, end_date, price, file_name=None)
        row_count = self.logic.update_vacation(vacation)
        print(f'vacation {discription} altered succesfully')
        return row_count
        


    def delete_vacation(self, id):
        row_count = self.logic.delete_vacation(id)
        if row_count == None:
            print('There is no such a vacation ')
        else:
            print('vacation been deleted ')
        return row_count
       
    

            