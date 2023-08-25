#!/usr/bin/python3

import tkinter as tk
from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("DARK")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green        global Kids



#	START OF TKINTER WINDOW CODE
class App(tk.Frame):
    def __init__(self, master):
        global Days, Hours, Minutes, Babies, Kids, StretchLegs, Food, Restrooms, Stores, MiscStops, Day
        Days = tk.IntVar()
        Hours = tk.IntVar()
        Minutes = tk.IntVar()
        Babies = tk.IntVar()
        Kids = tk.IntVar()
        StretchLegs = tk.IntVar()
        Food = tk.IntVar()
        Restrooms = tk.IntVar()
        Stores = tk.IntVar()
        MiscStops = tk.IntVar()
        Day = tk.StringVar()
        
        super().__init__(master)
#	EVERYTHING ON THE FIRST LEFT FRAME
        leftframe = customtkinter.CTkFrame(
        root
        )
        leftframe.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        Label = customtkinter.CTkLabel(leftframe, text="Expected Travel Time")
        Label.pack()
        Label = customtkinter.CTkLabel(leftframe, text="\nDays")
        Label.pack()
        self.DaysIPT = customtkinter.CTkEntry(leftframe, placeholder_text="0")
        self.DaysIPT.pack()
        self.Days = tk.IntVar()
        self.Days.set("0")
        self.DaysIPT["textvariable"] = self.Days
        Label = customtkinter.CTkLabel(leftframe, text="Hours")
        Label.pack()      
        self.HoursIPT = customtkinter.CTkEntry(leftframe, placeholder_text="0")
        self.HoursIPT.pack()
        self.Hours = tk.IntVar()
        self.Hours.set("0")
        self.HoursIPT["textvariable"] = self.Hours
        Label = customtkinter.CTkLabel(leftframe, text="Minutes")
        Label.pack()
        self.MinutesIPT = customtkinter.CTkEntry(leftframe, placeholder_text="0")
        self.MinutesIPT.pack()
        self.Minutes = tk.IntVar()
        self.Minutes.set("0")
        self.MinutesIPT["textvariable"] = self.Minutes
        
        Label = customtkinter.CTkLabel(leftframe, text="Non-Adults")
        Label.pack()
        Label = customtkinter.CTkLabel(leftframe, text="Babies")
        Label.pack()     
        self.BabiesIPT = customtkinter.CTkEntry(leftframe, placeholder_text="0")
        self.BabiesIPT.pack()
        self.Babies = tk.IntVar()
        self.Babies.set("0")
        self.BabiesIPT["textvariable"] = self.Babies
        Label = customtkinter.CTkLabel(leftframe, text="Kids")
        Label.pack()
        self.KidsIPT = customtkinter.CTkEntry(leftframe, placeholder_text="0")
        self.KidsIPT.pack()
        self.Kids = tk.IntVar()
        self.Kids.set("0")
        self.KidsIPT["textvariable"] = self.Kids


#	EVERYTHING ON THE SECOND LEFT FRAME
        leftframe2 = customtkinter.CTkFrame(
        root
        )
        leftframe2.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        Label = customtkinter.CTkLabel(leftframe2, text="Stops\n")
        Label.pack()
        Label = customtkinter.CTkLabel(leftframe2, text="Stretching Of Legs")
        Label.pack()
        self.StretchLegsIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="0")
        self.StretchLegsIPT.pack()
        self.StretchLegs = tk.IntVar()
        self.StretchLegs.set("0")
        self.StretchLegsIPT["textvariable"] = self.StretchLegs
        Label = customtkinter.CTkLabel(leftframe2, text="Getting Food")
        Label.pack()
        self.FoodIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="0")
        self.FoodIPT.pack()
        self.Food = tk.IntVar()
        self.Food.set("0")
        self.FoodIPT["textvariable"] = self.Food
        Label = customtkinter.CTkLabel(leftframe2, text="Bathrooms")
        Label.pack()
        self.RestroomsIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="0")
        self.RestroomsIPT.pack()
        self.Restrooms = tk.IntVar()
        self.Restrooms.set("0")
        self.RestroomsIPT["textvariable"] = self.Restrooms
        Label = customtkinter.CTkLabel(leftframe2, text="Shopping")
        Label.pack()
        self.StoresIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="0")
        self.StoresIPT.pack()
        self.Stores = tk.IntVar()
        self.Stores.set("0")
        self.StoresIPT["textvariable"] = self.Stores
        Label = customtkinter.CTkLabel(leftframe2, text="Other Stops")
        Label.pack()
        self.MiscStopsIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="0")
        self.MiscStopsIPT.pack()
        self.MiscStops = tk.IntVar()
        self.MiscStops.set("0")
        self.MiscStopsIPT["textvariable"] = self.MiscStops
        Label = customtkinter.CTkLabel(leftframe2, text="Day Of The Week")
        Label.pack()       
        self.DayIPT = customtkinter.CTkOptionMenu(leftframe2, variable = Day, values=[ "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        self.DayIPT.pack()
        self.DayIPT.set(self.DayIPT._values[0])
#	EVERYTHING ON THE THIRD LEFT FRAME 
        leftframe3 = customtkinter.CTkFrame(
        root
        )
        leftframe3.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        Label = customtkinter.CTkLabel(leftframe3, text="Accurate Time")
        Label.pack()
        global output 
        output = customtkinter.CTkTextbox(
        leftframe3,
        state='disabled',
        height = 1,
        )
        output.pack(fill = BOTH)

        exitbutton = customtkinter.CTkButton(
        leftframe3,
        text = 'Calculate',
        command = self.Run
        ).pack()

#	END OF TKINTER WINDOW CODE
    def Run(self):
        Days = self.DaysIPT.get()
        Hours = self.HoursIPT.get()
        Minutes = self.MinutesIPT.get()
        Misc = self.MiscStopsIPT.get()
        Kids = self.KidsIPT.get()
        Babies = self.BabiesIPT.get()
        Food = self.FoodIPT.get()
        StretchLegs = self.StretchLegsIPT.get()
        Stores = self.StoresIPT.get()
        Restrooms = self.RestroomsIPT.get()
        Day = self.DayIPT.get()
                
        try:
            Days = int(Days)
        except:
            Days = 0
        try:
            Hours = int(Hours)
        except:
            Hours = 0
        try:
            Minutes = int(Minutes)
        except:
            Minutes = 0
        try:
            Misc += int(Misc)
        except:
            Misc = 0
        try:
            Kids = int(Kids)
        except:
            Kids = 0
        try:
            Babies = int(Babies)
        except:
            Babies = 0
        try:
            Food = int(Food)
        except:
            Food = 0
        try:
            StretchLegs = int(StretchLegs)
        except:
            StretchLegs = 0
        try:
            Stores = int(Stores)
        except:
            Stores = 0
        try:
            Restrooms = int(Restrooms)
        except:
            Restrooms = 0
        if Days == 0 and Hours == 0 and Minutes == 0:
            pass
        else:
            Hours += Misc
            Minutes += (Kids * 5) 
            Minutes += (Babies* 10) 
            Minutes += (Food * 90) 
            Minutes += (5 * StretchLegs )
            Minutes += ((30 * (Kids + 1)) * Stores )
            Minutes += ((3 * (Kids + 1) + (Babies * 5)) * Restrooms)
            if Day == "Saturday":
                Minutes += 30
            if Day == "Sunday":
                Minutes -= 10
            elif Day == "Monday" or Day == "Friday":
                Minutes += 20
            else:
                Minutes += 5
            if int(Minutes) >= 60:
                while int(Minutes) >= 60:
                    Hours += 1
                    Minutes -= 60
            if int(Hours) >= 24:
                while int(Hours) >= 24:
                    Days += 1
                    Hours -= 24
            if int(Minutes) < 0:
                Hours -= 1
                Minutes = 60 + Minutes
            if int(Hours) < 0:
                Days -= 1
                Hours = 24 + Hours
            if int(Days) < 0:
                Days = 0
        output.configure(state='normal')
        output.delete(1.0, END)
        output.insert(END, f'Days:{Days} Hours:{Hours} Minutes:{Minutes}')
        output.configure(state='disabled')
        
title = "Trip Planner"
root = customtkinter.CTk(className="TPER")
root.geometry("900x450")
root.resizable(True,True)
myapp = App(root)
myapp.master.title(title)
myapp.mainloop()
