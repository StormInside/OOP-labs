from abc import ABCMeta, abstractmethod
import time

class Command(metaclass = ABCMeta):

    @abstractmethod
    def execute(self):
        pass

class Save_Docunment(Command):

    def __init__(self, receiver, data):

        self._receiver = receiver
        self.data = data

    def execute(self):

        print(f"Saving...")
        self._receiver.file_save(self.data)

class Import(Command):

    def __init__(self, receiver):

        self._receiver = receiver

    def execute(self, data):

        print(f"Importing...")
        save_command = self._receiver.file_import(data)
        return save_command

class Receiver:

    def file_save(self, data = None):
        print(f"Saved document ({data})")

    def file_import(self, a=None):
        print(f"Imported file ({a})")
        save_command = Save_Docunment(receiver, {"Document_name": a["Document_name"]})
        return save_command


def auto(save_command):
    save_command.execute()
    time.sleep(1)
    

current_file = "Default"

receiver = Receiver()

save_command = Save_Docunment(receiver, {"Document_name": current_file})

import_command = Import(receiver)

while True:
    auto(save_command)
    _input = input("Your command\n--> ")
    if _input == "save":
        save_command.execute()
    elif _input == "import":
        file_name = input("File Name\n--> ")
        save_command = import_command.execute({"Document_name": file_name})
    else:
        print("No such command")