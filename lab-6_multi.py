from abc import ABCMeta, abstractmethod
import threading
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
        save_command = Save_Docunment(self, {"Document_name": a["Document_name"]})
        return save_command

class Program:

    def __init__(self):
        
        self.current_file = "Default"
        self.receiver = Receiver()
        self.import_command = Import(self.receiver)

        self.save_command = Save_Docunment(self.receiver, {"Document_name": self.current_file})


    def auto(self):
        while True:
            self.save_command.execute()
            time.sleep(10)
    

    def text_interface(self, ):
        while True:
            _input = input("Your command\n--> ")
            if _input == "save":
                self.save_command.execute()
            elif _input == "import":
                file_name = input("File Name\n--> ")
                self.save_command = self.import_command.execute({"Document_name": file_name})
            else:
                print("No such command")

    def runner(self):

        thread_auto = threading.Thread(target=self.auto)
        thread_interface = threading.Thread(target=self.text_interface)
        thread_auto.start()
        thread_interface.start()

if __name__ == "__main__":

    pr = Program()
    pr.runner()