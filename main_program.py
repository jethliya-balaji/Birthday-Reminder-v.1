import pickle
import datetime
import time
from os import path
from plyer import notification as notif

TODAY_DATE = datetime.datetime.now().strftime("%d %B").capitalize()

class BirthdayReminder:
    def __init__(self):
        self.Friend_birth = {}
        self.check_data()

    def add_birth_dates(self, name, date):
        self.Friend_birth.update({name: date})
        self.check_data()

    def remove(self, name):
        old_data = pickle.load(open("data.pkl", "rb"))
        if name in self.Friend_birth:
            del self.Friend_birth[name]
            old_data.update(self.Friend_birth)
            pickle.dump(self.Friend_birth, open("data.pkl", "wb"))
            print(name + " has been Removed\n")
        else:
            print("Not Such Name")

    def display_birth_dates(self):
        if self.Friend_birth == {}:
            print("NOT ADDED ANY BIRTHDAYS")
        else:
            for friend, birthdate in self.Friend_birth.items():
                print(f"{friend}'s birthday is on {birthdate}")

    def get_input(self):
        name_friend = input("Enter The Name Of A Person:)- ").capitalize().strip()
        birth_date = input("Enter the Birth Date Of The Person(date month):)- ").capitalize().strip()
        self.add_birth_dates(name_friend, birth_date)

    def check_data(self):
        if path.isfile('data.pkl'):
            old_data = pickle.load(open("data.pkl", "rb"))
            self.Friend_birth.update(old_data)
            pickle.dump(self.Friend_birth, open("data.pkl", "wb"))
        else:
            pickle.dump(self.Friend_birth, open("data.pkl", "wb"))

    def check_date(self):
        if TODAY_DATE in self.Friend_birth.values():
            key = [i for i, name in self.Friend_birth.items() if name == TODAY_DATE]
            rm = ", ".join(key)
            notif.notify(title='Birthday', message=f'Its {TODAY_DATE} Birthday of {rm}', timeout=10)


if __name__ == '__main__':
    userId = BirthdayReminder()
    while True:
        print(
            f"-------------WelCome to Birthday Reminder------------- Date - {TODAY_DATE}\n"
            "To add Birthday type: 1\n"
            "To see Birthday you added type: 2\n"
            "To remove Birthday type: 3\n"
            "Press q to Quit\n"
        )
        user_choice = input("\n")

        if user_choice == '1':
            userId.get_input()
            time.sleep(2)
        elif user_choice == '2':
            userId.display_birth_dates()
            time.sleep(2)
        elif user_choice == '3':
            remove_name = input("Enter The Name You Want To Remove:)- ").strip().capitalize()
            userId.remove(remove_name)
            time.sleep(1)
        elif user_choice == "q" or "Q":
            exit()
        elif user_choice.isalpha() or user_choice.isnumeric():
            print("Invalid option\n")
            time.sleep(1)
