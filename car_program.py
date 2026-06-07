import time

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0

    def get_speed(self):
        return self.__speed


if __name__ == "__main__":
    print("=============================================")
    print("    🏎️  VROOM VROOM: CAR SIMULATION v1  🏎️    ")
    print("=============================================")

    my_vehicle = Car("2026", "Nissan GT-R")

    print(f"\nCreated Vehicle Target: {my_vehicle._Car__year_model} {my_vehicle._Car__make}")
    print("Starting engine... Let's accelerate!")
    print("-" * 45)

    for i in range(1, 6):
        my_vehicle.accelerate()
        time.sleep(0.3)
        print(f"Pushing Throttle [{i}/5] -> Current Speed: {my_vehicle.get_speed()} km/h")

    print("\n" + "-" * 45)
    print("Hit the brakes! Slowing down safety test...")
    print("-" * 45)

    for i in range(1, 6):
        my_vehicle.brake()
        time.sleep(0.3)
        print(f"Applying Brakes  [{i}/5] -> Current Speed: {my_vehicle.get_speed()} km/h")

    print("\n=============================================")
    print("         SIMULATION SUCCESSFULLY DONE        ")
    print("=============================================")

