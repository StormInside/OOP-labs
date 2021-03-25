import math
from typing import Protocol, runtime_checkable, Iterable
from abc import abstractmethod

class Game():

    def __init__(self, location = {"x":[-1000,1000], "y":[-1000,1000]}, money = 0):

        self.money = money
        self.location = location

    def set_money(self, count):
        self.money = count

    def print_money_amount(self):
        print(f"You have {self.money} left")

    def __del__(self):
        print("\nGame has been removed")

@runtime_checkable
class Upgradable(Protocol):
    @abstractmethod
    def upgrade(self):
        pass

class Vehicle(Upgradable):

    def __init__(self,
                game,
                speed = 10,
                vehicle_level = 1,
                health = 1000,
                coordinates = {"x":0.0, "y":0.0},
                vehicle_up_dict = {2:{"health":1300, "speed":20, "price":2000},
                           3:{"health":1500, "speed":30, "price":3000},
                           4:{"health":2000, "speed":40, "price":4000}}
                ):

        self.game = game
        # Game.__init__(self)
        self.speed = speed
        self.vehicle_level = vehicle_level
        self.health = health
        self.vehicle_up_dict = vehicle_up_dict
        self.coordinates = coordinates

    def move(self, distance, direction):

        if direction in self.coordinates:
            new_value = self.coordinates[direction]+distance
            if new_value >= self.location[direction][0] and new_value <= self.location[direction][1]:
                self.coordinates[direction] = new_value
                print(f"vehicle moved to {self.coordinates} in {math.ceil(math.fabs(distance/self.speed))} sec")
            else:
                print(f"vehicle cant moved to {new_value} by {direction}")
        else:
            raise ValueError("Direction must be 'x' or 'y'")

    def upgrade(self, up_dict = None):
        # print(f"/////////// {self.game.money} /////////")
        if not up_dict:
            up_dict = self.vehicle_up_dict

        if self.vehicle_level < 4:
            price = up_dict[self.vehicle_level+1]["price"]
            
            if self.game.money >= price:
                self.game.money = self.game.money - price
                self.health = up_dict[self.vehicle_level+1]["health"]
                self.speed = up_dict[self.vehicle_level+1]["speed"]
                new_level = self.vehicle_level + 1
                self.vehicle_level = new_level
                print(f"Vehicle has been upgraded to lvl {new_level}") 
            else:
                print(f"You dont have much money {price} neded")
        else:
            print("You cant upgrade more than lvl 4")

    def __del__(self):
        print("\nVehicle has been removed")

class Weapon(Upgradable):

    def __init__(self,
                game,
                damage = 100,
                weapon_level = 1,
                weapon_up_dict = {2:{"damage":130, "price":1500}, 3:{"damage":150, "price":2000}, 4:{"damage":200, "price":3000}}
                ):

        self.game = game
        # Game.__init__(self)
        self.damage = damage
        self.weapon_level = weapon_level
        self.weapon_up_dict = weapon_up_dict

    def shoot(self, enemy):
        
        enemy.cause_damage(self.damage)

    def upgrade(self,  up_dict = None):

        if not up_dict:
            up_dict = self.weapon_up_dict

        if self.weapon_level < 4:
            price = up_dict[self.weapon_level+1]["price"]
            
            if self.game.money >= price:
                self.game.money = self.game.money - price
                self.damage = up_dict[self.weapon_level+1]["damage"]
                new_level = self.weapon_level + 1
                self.weapon_level = new_level
                print(f"Weapon has been upgraded to lvl {new_level}") 
            else:
                print(f"You dont have much money {price} neded")
        else:
            print("You cant upgrade more than lvl 4")


    def __del__(self):
        print(f"\nWeapon has been removed")

class Armor(Upgradable):

    def __init__(self,
                game,
                armour_health = 1000, 
                armor_level = 1, 
                armor_up_dict = {2:{"armour_health":1300, "price":1500}, 3:{"armour_health":1500, "price":2000}, 4:{"armour_health":2000, "price":3000}}
                ):

        self.game = game
        # Game.__init__(self)
        self.armour_health = armour_health
        self.armor_level = armor_level
        self.armor_up_dict = armor_up_dict

    def upgrade(self, up_dict = None):

        if not up_dict:
            up_dict = self.armor_up_dict

        if self.armor_level < 4:
            price = up_dict[self.armor_level+1]["price"]
            
            if self.game.money >= price:
                # print(id(self.game.money))
                self.game.money -= price
                # print(id(self.game.money))
                self.armour_health = up_dict[self.armor_level+1]["armour_health"]
                new_level = self.armor_level + 1
                self.armor_level = new_level
                print(f"Armor has been upgraded to lvl {new_level}") 
            else:
                print(f"You dont have much money {price} neded")
        else:
            print("You cant upgrade more than lvl 4")

    def __del__(self):
        print(f"\nArmor has been removed")



def upgrade_all(parts: Iterable[Upgradable])-> None:
    for part in parts:
        part.upgrade()

g = Game()
g.set_money(10000)

v = Vehicle(g)
a = Armor(g)
w = Weapon(g)

upgrade_all([v, a, w])
