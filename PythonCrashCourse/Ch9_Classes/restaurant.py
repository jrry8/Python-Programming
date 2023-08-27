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