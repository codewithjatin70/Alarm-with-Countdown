import time

class Alarm:
    def __init__(self, name, time_sec, task):
        self.name = name
        self.task = task
        self.alarm = time_sec

    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Task : {self.task}")
        print(f"Alarm : {self.alarm} seconds")

    def start_alarm(self):
        print(f"Alarm started for {self.alarm} seconds... Please wait.")
        time.sleep(self.alarm)
        print(f"⏰ Time's up, {self.name}! Do your task: {self.task}")

name = input("Enter Your Name: ")
task = input("Enter Your Task: ")
alarm_sec = int(input("Enter Alarm Time in seconds: "))

alarm = Alarm(name, alarm_sec, task)
alarm.show_details()
alarm.start_alarm()
