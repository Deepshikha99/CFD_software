#!/usr/bin/env python3
import tkinter as tk
from tkinter import font
import logging
import os
import project as project
from tkinter.ttk import *
from tkinter import *
import tkinter.scrolledtext as ScrolledText
import time

LARGE_FONT= ("Verdana", 16)
MEDIUM_FONT= ("Verdana", 12)
SMALL_FONT= ("Verdana", 9) 

curdir=os.getcwd()

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
      

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.container=tk.Frame(self)
        self.container.pack(side="top", fill="both", expand = True)
        self.logwindow = tk.Frame(self.container, bg="green")
        self.mainwindow=tk.Frame(self.container)
        self.logwindow.pack()

        self.mainwindow.pack()
        self.logwindow.place(relwidth=0.3, relheight=1, relx=0.7)
        self.mainwindow.place(relwidth=0.7, relheight=1) 
        header=tk.Frame(self.mainwindow)
        header.pack()
        header.place(relwidth=1, relheight=0.1)
        header.tkraise()
        mainsection=tk.Frame(self.mainwindow)
        mainsection.pack()
        mainsection.place(relheight=0.9, relwidth=1, rely=0.1)

        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)


        p1.place(in_=mainsection, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=mainsection, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=mainsection, x=0, y=0, relwidth=1, relheight=1)
        def page1():
          b1.config(bd="5")
          b2.config(bd="0")
          b3.config(bd="0")
          p1.show()
        def page2():
          b1.config(bd="0")
          b2.config(bd="5")
          b3.config(bd="0")
          p2.show()
        def page3():
          b1.config(bd="0")
          b2.config(bd="0")
          b3.config(bd="5")
          p3.show()
        b1 = tk.Button(header, text="Pre-processing", command=page1, font=helv36, bg="white", bd="5")
        b2 = tk.Button(header, text="Solving", command=page2, font=helv36, bg="white")
        b3 = tk.Button(header, text="Post-processing", command=page3, font=helv36, bg="white")

        b1.pack(expand="true", fill="both")
        b2.pack(expand="true", fill="both")
        b3.pack(expand="true", fill="both")
        b1.place(relheight=1, relwidth=0.333)
        b2.place(relheight=1, relwidth=0.333, relx=0.333)
        b3.place(relheight=1, relwidth=0.333, relx=0.666)
        header.grid_columnconfigure(1, weight=1, uniform="group1")
        header.grid_columnconfigure(2, weight=1, uniform="group1")
        header.grid_columnconfigure(3, weight=1, uniform="group1")
        p1.show()

 
if __name__ == "__main__":
    folder, project_name, flag, flag2=project.build()
    if flag==0:
      exit(0)
    root = tk.Tk()
    helv36 = font.Font(family='Helvetica', size=15)
    helv26 = font.Font(family='Helvetica', size=12)
    preprocess=tk.IntVar()
    preprocess.set(1)
    solver=tk.IntVar()
    solver.set(3)
    postprocess1=tk.IntVar()
    postprocess1.set(1)
    postprocess2=tk.IntVar()
    postprocess3=tk.IntVar()
    meshformat = tk.StringVar(root)
    geoavailable=tk.StringVar(root)
    orientation=tk.StringVar(root)
    numberofcores=tk.StringVar(root)
    timestep=tk.StringVar(root)
    simulationtime=tk.StringVar(root)
    animation=tk.StringVar(root)
    plot=tk.StringVar(root)
    sol1=0
    sol2=0
    geofilename=tk.StringVar(root)
    geofile=""
    mshfile=""
    mshfilename=tk.StringVar(root)
    flmlfile=""
    flmlfilename=tk.StringVar(root)
    postfoldername=tk.StringVar(root)
    postfolder=""
    sv=tk.StringVar(root)
    sv.set("0")
    sv2=tk.StringVar(root)
    sv2.set("0")

    main = MainView(root)    
    root.title("CFD Software")
    main.pack(side="top", fill="both", expand=True)
    root.geometry("1500x1500")
    root.minsize(1200, 500)
    root.mainloop()
    