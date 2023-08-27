'Python Crash Course Chapter 9 Exercises'

import typing
'''we can import an entire module
   access the classes you need using dot notation'''
import restaurant
'''we can specify which classes to import from a module
   we can use imported classes as if they were defined in this file
   so you do not need to use dot notation'''
from user import User
'''it is not recommended to import all classes from a module using *
   1. this makes it unclear which classes you're using from the module
   2. if you accidentally import a class with the same name as smth else in the file,
        you can create errors that are hard to diagnose'''
#from user import *

myRestaurant = restaurant.Restaurant("Dominos", "pizza")
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

r1 = restaurant.Restaurant('Good Food', 'sushi')
r2 = restaurant.Restaurant('Better Food', 'fried chicken')
r3 = restaurant.Restaurant('Best Food', 'ice cream')
r1.describeRestaurant()
r2.describeRestaurant()
r3.describeRestaurant()

print('#' * 30)

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

print('#' * 30)

# parent class must appear before child class
class IceCreamStand(restaurant.Restaurant):
    def __init__(self, flavors=['vanilla', 'chocolate', 'strawberry']):
        self.flavors = flavors

    def displayFlavors(self):
        res = "This stand sells "
        for i in range(len(self.flavors) - 1):
            res += self.flavors[i] + ', '
        res += 'and ' + self.flavors[-1] + ' ice cream.'
        print(res)

myStand = IceCreamStand()
myStand.displayFlavors()

class Admin(User):
    def __init__(self):
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def showPrivileges(self):
        print('The administrator has the following privileges:')
        for p in self.privileges:
            print('\t' + p)

myAdmin = Admin()
myAdmin.privileges.showPrivileges()



