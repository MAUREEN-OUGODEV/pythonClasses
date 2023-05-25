class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.current_speed = 0
        self.hooting = False

    def get_descriptive_name(self):
        name = f"{self.year} {self.make} {self.model}"
        return name.title()

    def read_distance(self):
        return (f"This car has {self.distance} miles on it.")

    def update_distance(self, mileage):
        if mileage >= self.distance:
            self.distance = mileage
            return mileage
        else:
            return("You can't roll back an odometer!")

    def increment_distance(self, miles):
        self.distance+= miles
        return miles
    def hooting_sound():
        hooting =True
        return hooting
nissan=Car("Vits","nissam",2006)
print(nissan.get_descriptive_name())
print(nissan.read_distance())
print(nissan.update_distance(200))
print(nissan.increment_distance(400))

    



    
