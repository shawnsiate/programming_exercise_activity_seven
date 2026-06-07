class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5.0, color="blue", on=False):
        self.__speed = speed
        self.__radius = float(radius)
        self.__color = str(color)
        self.__on = bool(on)

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def is_on(self):
        return self.__on

    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
            self.__speed = speed

    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)

    def set_on(self, on_status):
        self.__on = bool(on_status)

if __name__ == "__main__":
    print("=============================================")
    print("       INTERACTIVE FAN CONFIGURATOR          ")
    print("=============================================\n")

    fan_one = Fan()
    fan_two = Fan()

    fans = [("FAN OBJECT 1", fan_one), ("FAN OBJECT 2", fan_two)]
    speed_labels = {1: "SLOW", 2: "MEDIUM", 3: "FAST"}

    for name, fan_object in fans:
        print(f"CONFIGURING: {name}")
        print("-" * 30)

        print("Select Speed: [1] SLOW | [2] MEDIUM | [3] FAST")
        choice = int(input("Enter choice (1-3): "))
        if choice == 1:
            fan_object.set_speed(Fan.SLOW)
        elif choice == 2:
            fan_object.set_speed(Fan.MEDIUM)
        elif choice == 3:
            fan_object.set_speed(Fan.FAST)

        radius_input = float(input("Enter fan radius (e.g., 5.0, 10.0): "))
        fan_object.set_radius(radius_input)

        color_input = input("Enter fan color: ")
        fan_object.set_color(color_input)

        status_input = input("Turn fan ON? (yes/no): ").strip().lower()
        fan_object.set_on(status_input == "yes")

        print(f"{name} Saved successfully!\n")

    print("=============================================")
    print("         GENERATING LIVE FAN REPORTS         ")
    print("=============================================")

    for name, fan_object in fans:
        print(f"\n--- [ {name} LIVE STATUS ] ---")
        current_speed = fan_object.get_speed()
        print(f"Speed  : {speed_labels.get(current_speed, 'UNKNOWN')}")
        print(f"Radius : {fan_object.get_radius()}")
        print(f"Color  : {fan_object.get_color()}")
        print(f"Status : {'RUNNING' if fan_object.is_on() else 'IDLE'}")
        print("-" * 35)