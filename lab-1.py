
import time

class Washer():

    _serial_number = 10000

    def __init__(self,
                 manufacturer = "undefined",
                 modes = ["default", ], 
                 default_speed = 1000,
                 price = None,
                 size = [100, 50, 100],
                 ):
        
        self.manufacturer = manufacturer
        self.modes = modes
        self.default_speed = default_speed
        self.price = price
        self.size = size

        Washer._serial_number += 1
        self.serial_number = Washer._serial_number

    @staticmethod
    def get_serial_mumbers():
        i = Washer._serial_number
        while (i > 10000 and i <= Washer._serial_number):
            print(i)
            i-=1

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def add_mode(self, new_modes):
        if type(new_modes) is list:
            self.modes.extend(new_modes)
        else:
            raise TypeError("new_modes must be list")
    
    def rm_mode(self, modes2del):
        if type(modes2del) is list:
            for mode in modes2del:
                if mode in self.modes:
                    self.modes.remove(mode)
                else:
                    print(f"Mod {mode} doesnt exist in modes")
        else:
            raise TypeError("modes2del must be list")

    def set_default_speed(self, default_speed):
        if type(default_speed) is int:
            self.default_speed = default_speed
        else:
            raise TypeError("default_speed must be int")
        
    def set_price(self, price):
        if type(price) is int:
            self.price = price
        else:
            raise TypeError("price must be int")

    def set_size(self, size):
        if type(size) is list:
            self.size = size
        else:
            raise TypeError("size must be list")

    def start_wash(self, mode = "default"):
        if mode == "default":
            for i in range(1, 7):
                print(f"Washing with warm water speed = {self.default_speed}; {(7-i)*10} minutes left")
                time.sleep(1)
            print("Washing compleat!!!")
        elif mode == "fast":
            if mode in self.modes:
                for i in range(1, 4):
                    print(f"Washing with warm water speed = {self.default_speed * 2}; {(4-i)*10} minutes left")
                    time.sleep(1)
                print("Washing compleat!!!")
            else:
                print("Sorry, your washer cant use this mode")
        elif mode == "cold":
            if mode in self.modes:
                for i in range(1, 13):
                    print(f"Washing with warm water speed = {int(self.default_speed * 1.5)}; {(13-i)*10} minutes left")
                    time.sleep(1)
                print("Washing compleat!!!")
            else:
                print("Sorry, your washer cant use this mode")
        else:
            print("Sorry, mod undefined")

if __name__ == "__main__":

    Washer1 = Washer(1000)
    Washer2 = Washer("Best-Washers",["default", "fast", "cold"],1500,2000)

    Washer.get_serial_mumbers()

    print(Washer1.modes)
    print(Washer2.modes)

    Washer1.start_wash("cold")
    Washer1.start_wash()
    Washer2.start_wash("fast")
    Washer2.start_wash("cold")

    Washer1.set_manufacturer("Manufactor")
    print(Washer1.manufacturer)
    Washer1.set_default_speed(3000)
    print(Washer1.default_speed)
    Washer1.add_mode(["fast"])
    print(Washer1.modes)
    Washer1.start_wash("fast")



    
