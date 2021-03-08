import math


class Game():

    money = 0

    def __init__(self, location = {"x":[-1000,1000], "y":[-1000,1000]}, money = 0):

        Game.money = money
        self.location = location

    @staticmethod
    def set_money(count):
        Game.money = count

    @staticmethod
    def print_money_amount():
        print(f"You have {Game.money} left")

    def __del__(self):
        print("\nGame has been removed")

class Vehicle(Game):

    def __init__(self,
                speed = 10,
                vehicle_level = 1,
                health = 1000,
                coordinates = {"x":0.0, "y":0.0},
                vehicle_up_dict = {2:{"health":1300, "speed":20, "price":2000},
                           3:{"health":1500, "speed":30, "price":3000},
                           4:{"health":2000, "speed":40, "price":4000}}
                ):

        Game.__init__(self)
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

    def vehicle_upgrade(self, up_dict = None):
        # print(f"/////////// {Game.money} /////////")
        if not up_dict:
            up_dict = self.vehicle_up_dict

        if self.vehicle_level < 4:
            price = up_dict[self.vehicle_level+1]["price"]
            
            if Game.money >= price:
                Game.money = Game.money - price
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

class Weapon(Game):

    def __init__(self,
                damage = 100,
                weapon_level = 1,
                weapon_up_dict = {2:{"damage":130, "price":1500}, 3:{"damage":150, "price":2000}, 4:{"damage":200, "price":3000}}
                ):

        Game.__init__(self)
        self.damage = damage
        self.weapon_level = weapon_level
        self.weapon_up_dict = weapon_up_dict

    def shoot(self, enemy):
        
        enemy.cause_damage(self.damage)

    def weapon_upgrade(self,  up_dict = None):

        if not up_dict:
            up_dict = self.weapon_up_dict

        if self.weapon_level < 4:
            price = up_dict[self.weapon_level+1]["price"]
            
            if Game.money >= price:
                Game.money = Game.money - price
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

class Armor(Game):

    def __init__(self,
                armour_health = 1000, 
                armor_level = 1, 
                armor_up_dict = {2:{"armour_health":1300, "price":1500}, 3:{"armour_health":1500, "price":2000}, 4:{"armour_health":2000, "price":3000}}
                ):

        Game.__init__(self)
        self.armour_health = armour_health
        self.armor_level = armor_level
        self.armor_up_dict = armor_up_dict

    def armor_upgrade(self, up_dict = None):

        if not up_dict:
            up_dict = self.armor_up_dict

        if self.armor_level < 4:
            price = up_dict[self.armor_level+1]["price"]
            
            if Game.money >= price:
                # print(id(Game.money))
                Game.money -= price
                # print(id(Game.money))
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


class Tier3(Vehicle, Weapon, Armor):

    def __init__(self,
                name,
                upgrade_price = 5000,
                speed = 50,
                vehicle_level = 1,
                health = 2000,
                coordinates = {"x":0.0, "y":0.0},
                vehicle_up_dict = {2:{"health":2300, "speed":60, "price":4000},
                        3:{"health":2600, "speed":70, "price":5000},
                        4:{"health":3000, "speed":80, "price":6000}},
                damage = 200,
                weapon_level = 1,
                weapon_up_dict = {2:{"damage":230, "price":2500}, 3:{"damage":250, "price":3000}, 4:{"damage":300, "price":3500}},
                armour_health = 2000, 
                armor_level = 1, 
                armor_up_dict = {2:{"armour_health":2300, "price":2500}, 3:{"armour_health":2500, "price":3000}, 4:{"armour_health":3000, "price":3500}}           
                ):

        Vehicle.__init__(self, speed, vehicle_level, health, coordinates, vehicle_up_dict)
        Weapon.__init__(self, damage, weapon_level, weapon_up_dict)
        Armor.__init__(self, armour_health, armor_level, armor_up_dict)

        self.name = name
        self.upgrade_price = upgrade_price
        
    def cause_damage(self, damage):

        if self.armour_health >= damage:
            self.armour_health -= damage
            print(f"{self.name} gets {damage} damage; {self.health} main hp left and {self.armour_health} armour")
        else:
            new_damage = damage - self.armour_health
            self.armour_health = 0
            self.health -= new_damage
            if self.health <= 0:
                self.destroy(damage)
            else:
                print(f"{self.name} gets {damage} damage; {self.health} main hp left and {self.armour_health} armour")

    def upgrade(self):
        # Game.print_money_amount()
        if self.vehicle_level >= 3 and self.weapon_level >= 3 and self.armor_level >= 3:
            if Game.money >= self.upgrade_price:

                new_tier = Tier2(speed = 90,
                                name = self.name,
                                vehicle_level = 1,
                                health = 2000,
                                coordinates = self.coordinates,
                                vehicle_up_dict = {2:{"health":2300, "speed":60, "price":4000},
                                                3:{"health":2600, "speed":110, "price":5000},
                                                4:{"health":3000, "speed":120, "price":6000}},
                                damage = 200,
                                weapon_level = 1,
                                weapon_up_dict = {2:{"damage":330, "price":3500}, 3:{"damage":350, "price":4000}, 4:{"damage":400, "price":4500}},
                                armour_health = 2000, 
                                armor_level = 1, 
                                armor_up_dict = {2:{"armour_health":3300, "price":3500}, 3:{"armour_health":3500, "price":4000}, 4:{"armour_health":4000, "price":4500}}
                                )
                
                return new_tier
            else:
                print(f"You dont have much money {self.upgrade_price} neded")
                
        else:
            msg = "You must upgrade:\n"
            if self.vehicle_level <= 3:
                msg += f"Vehicle to lvl 3; Current {self.vehicle_level}\n"
            if self.weapon_level <= 3:
                msg += f"Weapon to lvl 3; Current {self.weapon_level}\n"    
            if self.armor_level <= 3:
                msg += f"Armor to lvl 3; Current {self.armor_level}"    
            print(msg)

    def destroy(self, damage):
        print(f"{self.name} gets {damage} damage; And have been destroyed")
        self.__del__()
        
    def __del__(self):
        print(f"\nTier3 has been removed")


class Tier2(Vehicle, Weapon, Armor):

    def __init__(self,
                name,
                upgrade_price = 7000,
                speed = 90,
                vehicle_level = 1,
                health = 2000,
                coordinates = {"x":0.0, "y":0.0},
                vehicle_up_dict = {2:{"health":2300, "speed":60, "price":4000},
                        3:{"health":2600, "speed":70, "price":5000},
                        4:{"health":3000, "speed":80, "price":6000}},
                damage = 200,
                weapon_level = 1,
                weapon_up_dict = {2:{"damage":230, "price":2500}, 3:{"damage":250, "price":3000}, 4:{"damage":300, "price":3500}},
                armour_health = 2000, 
                armor_level = 1, 
                armor_up_dict = {2:{"armour_health":2300, "price":2500}, 3:{"armour_health":2500, "price":3000}, 4:{"armour_health":3000, "price":3500}}           
                ):

        Vehicle.__init__(self, speed, vehicle_level, health, coordinates, vehicle_up_dict)
        Weapon.__init__(self, damage, weapon_level, weapon_up_dict)
        Armor.__init__(self, armour_health, armor_level, armor_up_dict)

        self.name = name
        self.upgrade_price = upgrade_price
        
    def cause_damage(self, damage):

        if self.armour_health >= damage:
            self.armour_health -= damage
            print(f"{self.name} gets {damage} damage; {self.health} main hp left and {self.armour_health} armour")
        else:
            new_damage = damage - self.armour_health
            self.armour_health = 0
            self.health -= new_damage
            if self.health <= 0:
                self.destroy(damage)
            else:
                print(f"{self.name} gets {damage} damage; {self.health} main hp left and {self.armour_health} armour")

    def upgrade(self):

        if self.vehicle_level >= 3 and self.weapon_level >= 3 and self.armor_level >= 3:
            if Game.money >= self.upgrade_price:

                new_tier = Tier1(speed = 90,
                                vehicle_level = 1,
                                health = 3000,
                                coordinates = self.coordinates,
                                vehicle_up_dict = {2:{"health":2300, "speed":100, "price":4000},
                                                3:{"health":2600, "speed":110, "price":5000},
                                                4:{"health":3000, "speed":120, "price":6000}},
                                damage = 200,
                                weapon_level = 1,
                                weapon_up_dict = {2:{"damage":330, "price":3500}, 3:{"damage":350, "price":4000}, 4:{"damage":400, "price":4500}},
                                armour_health = 2000, 
                                armor_level = 1, 
                                armor_up_dict = {2:{"armour_health":3300, "price":3500}, 3:{"armour_health":3500, "price":4000}, 4:{"armour_health":4000, "price":4500}}
                                )
                return new_tier
            else:
                print(f"You dont have much money {self.upgrade_price} neded")
                
        else:
            msg = "You must upgrade:\n"
            if self.vehicle_level <= 3:
                msg += f"Vehicle to lvl 3; Current {self.vehicle_level}\n"
            if self.weapon_level <= 3:
                msg += f"Weapon to lvl 3; Current {self.weapon_level}\n"    
            if self.armor_level <= 3:
                msg += f"Armor to lvl 3; Current {self.armor_level}"    
            print(msg)

    def destroy(self, damage):
        print(f"{self.name} gets {damage} damage; And have been destroyed")
        self.__del__()
        
    def __del__(self):
        print(f"\nTier2 has been removed")

class Tier1(Vehicle, Weapon, Armor):

    def __init__(self,
                name,
                upgrade_price = 9000,
                speed = 90,
                vehicle_level = 1,
                health = 3000,
                coordinates = {"x":0.0, "y":0.0},
                vehicle_up_dict = {2:{"health":2300, "speed":100, "price":4000},
                                3:{"health":2600, "speed":110, "price":5000},
                                4:{"health":3000, "speed":120, "price":6000}},
                damage = 200,
                weapon_level = 1,
                weapon_up_dict = {2:{"damage":330, "price":3500}, 3:{"damage":350, "price":4000}, 4:{"damage":400, "price":4500}},
                armour_health = 2000, 
                armor_level = 1, 
                armor_up_dict = {2:{"armour_health":3300, "price":3500}, 3:{"armour_health":3500, "price":4000}, 4:{"armour_health":4000, "price":4500}}          
                ):
        
        Vehicle.__init__(self, speed, vehicle_level, health, coordinates, vehicle_up_dict)
        Weapon.__init__(self, damage, weapon_level, weapon_up_dict)
        Armor.__init__(self, armour_health, armor_level, armor_up_dict)

        self.name = name
        self.upgrade_price = upgrade_price
        
    def cause_damage(self, damage):

        if self.armour_health >= damage:
            self.armour_health -= damage
            print(f"{self.name} gets {damage} damage; {self.health} main hp left and {self.armour_health} armour")
        else:
            new_damage = damage - self.armour_health
            self.armour_health = 0
            self.health -= new_damage
            if self.health <= 0:
                self.destroy(damage)
            else:
                print(f"{self.name} gets {damage} damage; {self.health} main hp left and {self.armour_health} armour")

    def destroy(self, damage):
        print(f"{self.name} gets {damage} damage; And have been destroyed")
        self.__del__()
        
    def __del__(self):
        print(f"\nTier1 has been removed")

game = Game()

t3 = Tier3("T3")

t3.set_money(100000)
t3.print_money_amount()

t3.vehicle_upgrade()
t3.print_money_amount()
t3.vehicle_upgrade()
t3.print_money_amount()
t3.vehicle_upgrade()
t3.print_money_amount()

t3.armor_upgrade()
t3.print_money_amount()
t3.armor_upgrade()
t3.print_money_amount()
t3.armor_upgrade()
t3.print_money_amount()

t3.weapon_upgrade()
t3.print_money_amount()
t3.weapon_upgrade()
t3.print_money_amount()
t3.weapon_upgrade()
t3.print_money_amount()

t2 = t3.upgrade()
t2.print_money_amount()
t2.vehicle_upgrade()
t2.print_money_amount()
