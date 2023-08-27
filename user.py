class User():
    def __init__(self, firstName: str, lastName: str, age: int, hobby: str):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.hobby = hobby
        self.loginAttempts = 0

    def describeUser(self):
        print(self.firstName.title() + " " + self.lastName.title() + " is " + str(self.age) + " years old and enjoys " + self.hobby + '.')

    def greetUser(self):
        print('Hello ' + self.firstName.title() + " " + self.lastName.title() + "!")

    def incrementLoginAttempts(self):
        self.loginAttempts += 1
    
    def resetLoginAttempts(self):
        self.loginAttempts = 0