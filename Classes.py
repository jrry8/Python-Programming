import typing

class Restaurant():
    def __init__(self, name, cuisineType):
        self.name = name
        self.cuisineType = cuisineType

    def describeRestaurant(self):
        print("Welcome to " + self.name + "!")
        print("We serve " + self.cuisineType + " cuisine.")

    def openRestaurant(self):
        print(self.name + " is now open!")

myRestaurant = Restaurant("Dominos", "pizza")
print("My restaurant name is " + myRestaurant.name)
print("My restaurant serves " + myRestaurant.cuisineType)
myRestaurant.describeRestaurant()
myRestaurant.openRestaurant()

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

    def describeUser(self):
        print(self.firstName.title() + " " + self.lastName.title() + " is " + str(self.age) + " years old and enjoys " + self.hobby + '.')

    def greetUser(self):
        print('Hello ' + self.firstName.title() + " " + self.lastName.title() + "!")

dummy = User('Joe', 'Biden', 80, 'getting lost')
dummy.describeUser()
dummy.greetUser()

    
