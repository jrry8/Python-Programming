import typing

class Restaurant():
    def __init__(self, name, cuisineType):
        self.name = name
        self.cuisineType = cuisineType
        self.numberServed = 0

    def describeRestaurant(self):
        print("Welcome to " + self.name + "!")
        print("We serve " + self.cuisineType + " cuisine.")

    def openRestaurant(self):
        print(self.name + " is now open!")

    def setNumberServed(self, n):
        self.numberServed = n
    
    def incrementNumberServed(self, n):
        self.numberServed += n

myRestaurant = Restaurant("Dominos", "pizza")
print("My restaurant name is " + myRestaurant.name)
print("My restaurant serves " + myRestaurant.cuisineType)
myRestaurant.describeRestaurant()
myRestaurant.openRestaurant()

print('My restaurant has served ' + str(myRestaurant.numberServed) + ' people.')
myRestaurant.numberServed = 7
print('My restaurant has served ' + str(myRestaurant.numberServed) + ' people.')
myRestaurant.setNumberServed(9)
print('My restaurant has served ' + str(myRestaurant.numberServed) + ' people.')
myRestaurant.incrementNumberServed(8)
print('My restaurant has served ' + str(myRestaurant.numberServed) + ' people.')

print('#' * 30)

r1 = Restaurant('Good Food', 'sushi')
r2 = Restaurant('Better Food', 'fried chicken')
r3 = Restaurant('Best Food', 'ice cream')
r1.describeRestaurant()
r2.describeRestaurant()
r3.describeRestaurant()

print('#' * 30)

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

dummy = User('Joe', 'Biden', 80, 'getting lost')
dummy.describeUser()
dummy.greetUser()
print("Login attempts = " + str(dummy.loginAttempts))
dummy.incrementLoginAttempts()
print("Login attempts = " + str(dummy.loginAttempts))
dummy.incrementLoginAttempts()
dummy.incrementLoginAttempts()
print("Login attempts = " + str(dummy.loginAttempts))
dummy.resetLoginAttempts()
print("Login attempts = " + str(dummy.loginAttempts))

    
