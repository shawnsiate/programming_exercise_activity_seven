class Pet:
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    def set_name(self, pet_name):
        self.__name = pet_name

    def set_animal(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, pet_age):
        self.__age = pet_age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

if __name__ == "__main__":
    print("===============================================")
    print("        WELCOME TO PET DATABASE CREATOR        ")
    print("===============================================")

    user_pet = Pet()

    input_name = input("Enter your pet's name: ")
    input_type = input("What kind of animal is it?: ")
    input_age = input("How old is your pet?: ")

    user_pet.set_name(input_name)
    user_pet.set_animal(input_type)
    user_pet.set_age(input_age)

    print("\n===============================================")
    print("         PET PROFILE SAVED TO DATABASE         ")
    print("===============================================")
    print(f"Name: {user_pet.get_name().upper()}")
    print(f"Animal Type: {user_pet.get_animal_type()}")
    print(f"Age: {user_pet.get_age()}")