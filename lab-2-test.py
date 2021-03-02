class Game():

    money = 0

    def __init__(self):
        pass

    @staticmethod
    def set_money(count):
        Game.money = count

    @staticmethod
    def print_money_amount():
        print(f"You have {Game.money} left")


class Vehicle(Game):

    def __init__(self):

        Game.__init__(self)

    def vehicle_upgrade(self):

        print(f"/////////// {Game.money} /////////")
        Game.money = Game.money - 1000
        print(f"/////////// {Game.money} /////////")


class Tier3(Vehicle):

    def __init__(self):

        Vehicle.__init__(self)

    def upgrade(self):

        print(f"/////////// {Game.money} /////////")
        Game.money = Game.money - 1000
        print(f"/////////// {Game.money} /////////")


game = Game()

t3 = Tier3()

t3.set_money(10000)
t3.print_money_amount()
t3.vehicle_upgrade()
t3.print_money_amount()
t3.upgrade()
t3.print_money_amount()






