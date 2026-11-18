class vehicle:
    def __init__(self, max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage

car = vehicle(200,25)
print("Cars max speed is", car.max_speed )
print("Cars mileage:" , car.mileage)