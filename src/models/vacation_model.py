class VacationModel:
    def __init__(self, vacation_id, country_id, vacation_discription, vacation_start_date, vacation_end_date, price, file_name):
        self.vacation_id = vacation_id
        self.country_id = country_id
        self.vacation_discription = vacation_discription
        self.vacation_start_date = vacation_start_date
        self.vacation_end_date = vacation_end_date
        self.price = price
        self.file_name = file_name


    @staticmethod
    def dictionary_to_vacation(dictionary):
        vacation = VacationModel(dictionary['vacation_id'], dictionary['country_id'], dictionary['vacation_discription'],
                dictionary['vacation_start_date'], dictionary['vacation_end_date'], dictionary['price'], dictionary['file_name'])
        return vacation
    
    @staticmethod
    def dictionaries_to_vacations(list_of_dictionary):
        vacations = []
        for item in list_of_dictionary:
            vacation = VacationModel.dictionary_to_vacation(item)
            vacations.append(vacation)
        return vacations
    
            


