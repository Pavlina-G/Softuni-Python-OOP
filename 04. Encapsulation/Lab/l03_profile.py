class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    def __validate_password(self, password):
        is_long = len(password) >= 8
        has_uppercase = [x for x in password if x.isupper()]
        has_digit = [x for x in password if x.isdigit()]

        if not is_long or not has_uppercase or not has_digit:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    @property
    def password(self):
        return ''.join('*' * len(self.__password))

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
# correct_profile = Profile("Username", "Passw0rd")
# print(correct_profile)
