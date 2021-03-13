from abc import abstractmethod, ABCMeta

class Carriage(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self, code = "12345", max_count = 200):

        self.code = code
        self.passengers_list = {}
        self.max_count = max_count

    @abstractmethod
    def add_passenger_to_list(self, name, surname, year):

        if self.has_place:
            self.passengers_list.update({surname : [name, year]})
            return True
        else:
            return False


    @abstractmethod
    def del_passenger_from_list(self, name, surname, year):

        if surname in self.passengers_list:
            if self.passengers_list[surname] == [name,year]:
                del self.passengers_list[surname]
                return True
            else:
                return False
        else:
            return False


    @abstractmethod
    def has_place(self):
        return len(self.passengers_list) < self.max_count

    @abstractmethod
    def __str__(self):
        return str(self.code)

    @abstractmethod
    def __del__(self):
        print("///Carriage has been removed///")



class Сompartment(Carriage):

    def __init__(self, code = "12345"):

        Carriage.__init__(self)

        self.type = "Сompartment"
        self.code = code


    def add_passenger_to_list(self, name, surname, year):
        if super().add_passenger_to_list(name, surname, year):
            print(f"{name} {surname} has been added to {self.type} N:{super().__str__()}")
        else:
            print(f"No more place in {self.type} N:{super().__str__()}")


    def del_passenger_from_list(self, name, surname, year):

        if super().del_passenger_from_list(name, surname, year):
            print(f"{name} {surname} has been removed from {self.type} N:{super().__str__()}")
        else:
            print(f"No such person {name} {surname} {year} in {self.type} N:{super().__str__()}")


    def has_place(self):
        return super().has_place()

    def __str__(self):
        return f"{self.type} N:{super().__str__()}"

    def __del__(self):
        print("///Сompartment has been removed///")



class Seat(Сompartment):

    def __init__(self, code = "12345"):

        Сompartment.__init__(self)

        self.type = "Seat"
        self.code = code


    def give_linen(self, surname, name):

        print(f"{surname} {name} got linen in {self.type} N:{super().__str__()}")



# class Train():

    # def __init__(self):
    #     pass

    # def __str__(self):
    #     return super().__str__()

    # def __del__(self):
    #     print("///Train has been removed///")

if __name__ == "__main__":

    c = Сompartment()
    print(c)
    c.add_passenger_to_list("Yurii", "Agafonow", 2001)
    print(c.passengers_list)
    c.del_passenger_from_list("Yuri", "Agafonow", 2001)
    print(c.passengers_list)
    c.del_passenger_from_list("Yurii", "Agafonow", 2001)
    print(c.passengers_list)

    s = Seat()
    print(s)
    s.add_passenger_to_list("Yurii", "Agafonow", 2001)
    print(s.passengers_list)
    s.del_passenger_from_list("Yuri", "Agafonow", 2001)
    print(s.passengers_list)
    s.del_passenger_from_list("Yurii", "Agafonow", 2001)
    print(s.passengers_list)


