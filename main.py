#!/usr/bin/python3

import tkinter as tk
from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("DARK")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green        global Kids



#	START OF TKINTER WINDOW CODE
class App(tk.Frame):
    def __init__(self, master):
        global Days, Hours, Minutes, Babies, Kids, StretchLegs, Food, Restrooms, Stores, MiscStops
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
        
        super().__init__(master)
#	EVERYTHING ON THE FIRST LEFT FRAME
        leftframe = customtkinter.CTkFrame(
        root
        )
        leftframe.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        Label = customtkinter.CTkLabel(leftframe, text="Expected Travel Time")
        Label.pack()
        self.DaysIPT = customtkinter.CTkEntry(leftframe, placeholder_text="Days")
        self.DaysIPT.pack()
        self.Days = tk.IntVar()
        self.Days.set("0")
        self.DaysIPT["textvariable"] = self.Days
        
        self.HoursIPT = customtkinter.CTkEntry(leftframe, placeholder_text="Hours")
        self.HoursIPT.pack()
        self.Hours = tk.IntVar()
        self.Hours.set("0")
        self.HoursIPT["textvariable"] = self.Hours

        self.MinutesIPT = customtkinter.CTkEntry(leftframe, placeholder_text="Minutes")
        self.MinutesIPT.pack()
        self.Minutes = tk.IntVar()
        self.Minutes.set("0")
        self.MinutesIPT["textvariable"] = self.Minutes
        
        Label = customtkinter.CTkLabel(leftframe, text="Non-Adults")
        Label.pack()
        
        self.BabiesIPT = customtkinter.CTkEntry(leftframe, placeholder_text="Babies")
        self.BabiesIPT.pack()
        self.Babies = tk.IntVar()
        self.Babies.set("0")
        self.BabiesIPT["textvariable"] = self.Babies

        self.KidsIPT = customtkinter.CTkEntry(leftframe, placeholder_text="Kids")
        self.KidsIPT.pack()
        self.Kids = tk.IntVar()
        self.Kids.set("0")
        self.KidsIPT["textvariable"] = self.Kids


#	EVERYTHING ON THE SECOND LEFT FRAME
        leftframe2 = customtkinter.CTkFrame(
        root
        )
        leftframe2.pack(side = LEFT, fill=BOTH, anchor = NE, padx = 10, expand=1)
        
        Label = customtkinter.CTkLabel(leftframe2, text="Stops")
        Label.pack()

        self.StretchLegsIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="Stretching Of Legs")
        self.StretchLegsIPT.pack()
        self.StretchLegs = tk.IntVar()
        self.StretchLegs.set("0")
        self.StretchLegsIPT["textvariable"] = self.StretchLegs

        self.FoodIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="Getting Food")
        self.FoodIPT.pack()
        self.Food = tk.IntVar()
        self.Food.set("0")
        self.FoodIPT["textvariable"] = self.Food

        self.RestroomsIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="Bathrooms")
        self.RestroomsIPT.pack()
        self.Restrooms = tk.IntVar()
        self.Restrooms.set("0")
        self.RestroomsIPT["textvariable"] = self.Restrooms

        self.StoresIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="Shopping")
        self.StoresIPT.pack()
        self.Stores = tk.IntVar()
        self.Stores.set("0")
        self.StoresIPT["textvariable"] = self.Stores

        self.MiscStopsIPT = customtkinter.CTkEntry(leftframe2, placeholder_text="Other Stops")
        self.MiscStopsIPT.pack()
        self.MiscStops = tk.IntVar()
        self.MiscStops.set("0")
        self.MiscStopsIPT["textvariable"] = self.MiscStops

        
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

        Hours += Misc
        Minutes += (Kids * 5) 
        Minutes += (Babies* 10) 
        Minutes += (Food * 90) 
        Minutes += (5 * StretchLegs )
        Minutes += ((30 * (Kids + 1)) * Stores )
        Minutes += ((3 * (Kids + 1) + (Babies * 5)) * Restrooms)
    
        if int(Minutes) >= 60:
            while int(Minutes) >= 60:
                Hours += 1
                Minutes -= 60
        if int(Hours) >= 24:
            while int(Hours) >= 24:
                Days += 1
                Hours -= 24
                           
        output.configure(state='normal')
        output.delete(1.0, END)
        output.insert(END, f'Days:{Days} Hours:{Hours} Minutes:{Minutes}')
        output.configure(state='disabled')
        
title = "Trip Planner"
root = customtkinter.CTk(className="TPER")
root.geometry("900x250")
root.resizable(True,True)
myapp = App(root)
myapp.master.title(title)
myapp.mainloop()
