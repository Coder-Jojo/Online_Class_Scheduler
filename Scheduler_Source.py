import csv
import webbrowser as web
import datetime as dt
import schedule 
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb

def get_today_classes(day): #Get list of the classes today
    with open('Schedule.csv') as f:
        reader = csv.reader(f)
        list_of_classes = (list(reader))[day][1:]
        return list_of_classes

def launch_class(link):  #Launch the class after confirmation from the user
    root=Tk()
    res=mb.askquestion('Join Class', 'Do you really want to join the class starting now')
    if res == 'yes' :
        mb.showinfo('Join Class', 'You accepted to join the class')
        web.open(link)
        root.destroy()
    else :
        mb.showinfo('Join Class', 'You declined to join the class')
        root.destroy()


def schedule_classes(date):  #Using the list of classes schedule the classes to be launched at respective times
    list_of_classes=get_today_classes(date.weekday())
    for link in list_of_classes:
        if(link != ""):
            launch_time_offset=dt.timedelta(minutes=(list_of_classes.index(link))*90)
            print(launch_time_offset.total_seconds())
            launch_time=dt.datetime(date.year,date.month,date.day,8,30)+launch_time_offset
            launch_time=launch_time.strftime("%H:%M")
            print(launch_time)
            schedule.every(1).day.at(launch_time).do(launch_class, link)
   



cur_time = dt.datetime.now()
print("the time right now is:", cur_time.hour, cur_time.minute)
#x = dt.time(hour=a.hour, minute=a.minute)
date = dt.datetime.today()
schedule_classes(date)
while True:                 # Run the classes when it is the correct time
    schedule.run_pending()
    time.sleep(1)
