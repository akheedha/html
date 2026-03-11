class Vehicle:
    def __init__(self, id, price):    
        self.vehicle_id = id
        self.base_price = price

class Car(Vehicle):
    def __init__(self, id, price, seat):
        super().__init__(id, price)
        self.num_seat = seat

    def show_detail(self):
        print(f"\nId: ${self.vehicle_id}")
        print(f"Price: ${self.base_price}")
        print(f"Name: ${self.num_seat}\n")

    def rental_charge(self):
        return self.base_price * self.num_seat

class Bike(Vehicle):
    def __init__(self, id, price, type):
        super().__init__(id, price)
        self.bike_type = type

    def show_detail(self):
        print(f"\nId: ${self.vehicle_id}")
        print(f"Price: ${self.base_price}")
        print(f"Bike type: ${self.bike_type}\n")

    def rental_charge(self):
        return self.base_price * 0.5

def calculate_rental(Vehicle):
    return Vehicle.rental_charge() 


car1 = Car("CAR001", 100.0, 4)
bike1 = Bike("BIKE001", 80.0, "Scooter")

car1.show_detail()
bike1.show_detail()

print("Car Charge:", calculate_rental(car1))
print("Bike Charge:", calculate_rental(bike1))