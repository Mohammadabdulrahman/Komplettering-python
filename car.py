class Car:
    def __init__(self, brand, model, new_car_price, year_of_manufacture, owner):
        self.brand = brand
        self.model = model
        self.owner = []
        self.new_car_price = new_car_price
        self.year_of_manufacture = year_of_manufacture

    def set_owner(self, owner):
        self.owner = owner

    def add_owner(self, owner):
        if self.owner ==[]:
            self.owner.append(owner)
        elif self.owner == owner: #den ägaren är redan tillagd
            pass 


    def __str__(self):
        return f'{self.brand} car of model {self.model} owned by {self.owner}'

    i=0

class CarsInStock():
    def __init__(self, brand, model, new_car_price, year_of_manufacture):
        #self.brand = brand
        #self.model = model
        #self.new_car_price = new_car_price
        #self.year_of_manufacture = year_of_manufacture
        self.list_of_cars = []

    def add_car(self, brand, model, new_car_price, year_of_manufacture):
        temp_car = Car(brand,model, int(new_car_price), int(year_of_manufacture), owner)
        self.list_of_cars.append(temp_car)

