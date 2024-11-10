class UserModel:
    def __init__(self, user_id: int, first_name: str, last_name:str , email: str , password: str, role_id: int):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.role_id = role_id

    def __str__(self) -> str:
        return f'{self.user_id}, {self.first_name}, {self.last_name}, {self.email}'

    @staticmethod
    def dictionary_to_user(dictionary):
        user = UserModel(dictionary['user_id'], dictionary['first_name'], dictionary['last_name'], dictionary['email'], dictionary['password'],
                         dictionary['role_id'])
        return user

    @staticmethod
    def dictionaries_to_users(list_of_dictionary):
        users = []
        for item in list_of_dictionary:
            user = UserModel.dictionary_to_user(item)
            users.append(user)
        return users


