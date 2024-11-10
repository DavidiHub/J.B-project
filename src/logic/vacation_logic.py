from utils.dal import DAL
from models.vacation_model import *

class VacationLogic:
    def __init__(self):
        self.dal = DAL()

    def get_all_vacations(self):
        sql = 'select * from mydb.vacations order by vacation_start_date'
        result = self.dal.get_table(sql)
        vacations = VacationModel.dictionaries_to_vacations(result)
        return vacations
    

    
    def get_vacation(self, id):
        sql = 'select * from mydb.vacations where vacation_id=%s'
        result = self.dal.get_one(sql, (id, ))
        if result is None: return None
        vacation = VacationModel.dictionary_to_vacation(result)
        return vacation
    
    def insert_vacation(self, vacation):
        sql = '''insert into mydb.vacations(country_id, vacation_discription,vacation_start_date,
        vacation_end_date, price, file_name) values (%s, %s, %s, %s, %s, %s)'''
        last_inserted_id = self.dal.insert(sql, (vacation.country_id, vacation.vacation_discription,
                                                  vacation.vacation_start_date, vacation.vacation_end_date, vacation.price, vacation.file_name, ))
        return last_inserted_id
    
    def update_vacation(self, vacation):
        sql = '''update mydb.vacations set country_id=%s, vacation_discription=%s,
          vacation_start_date=%s, vacation_end_date=%s, price=%s where vacation_id=%s'''
        row_count = self.dal.update(sql, (vacation.country_id, vacation.vacation_discription,
                                           vacation.vacation_start_date, vacation.vacation_end_date, vacation.price, vacation.vacation_id, ))
        return row_count
    
    def delete_vacation(self, id):
        sql = 'delete from mydb.vacations where vacation_id=%s'
        row_count = self.dal.delete(sql, (id, ))
        if row_count == 0:
            return None
        return row_count