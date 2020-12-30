from car import Car
from car import CarsInStock

MAIN_MENU = """\
Welcome to Bilsäljarharry!

1. Print a car
2. Change owner of the car
3. Save all cars to a file
4. Load cars from a file
5. Remove a car
6. List all cars and attributes.
7. Add car
8. Close the app
"""

PRINT_CAR = "1"
CHANGE_OWNER = "2"
SAVE_CARS_TO_FILE = "3"
LOAD_CARS_FROM_FILE = "4"
REMOVE_CAR = "5"
LIST_ALL_CARS = "6"
ADD_CAR = "7"
CLOSE = "8"


def get_menu_selection():
    return input("Make your choice: ")


def main():
    print(MAIN_MENU)
    choice = get_menu_selection()
    while choice != 8:
        if choice == PRINT_CAR:
            volvo_xc60 = Car("Volvo","xc60",)
            print(volvo_xc60)
        elif choice == CHANGE_OWNER:
                new_owner = input ("Please write the name of the new owner. ")
                Car.set_owner(new_owner)
        #elif choice == SAVE_CARS_TO_FILE:
        #elif choice == LOAD_CARS_FROM_FILE:
        #elif choice == REMOVE_CAR:
        #elif choice == LIST_ALL_CARS:
        elif choice == ADD_CAR:
            print ("Please input brand ,model, new car price and year of manufacture")
            brand = input("Brand: ")
            model = input("Model: ")
            new_car_price = int(input("New car price: "))
            year_of_manufacture = int(input("Year of manufacture: "))          
            CarsInStock.add_car(brand,model,new_car_price,year_of_manufacture)
        elif choice == CLOSE:
            exit

        

if __name__ == "__main__":
    main()
