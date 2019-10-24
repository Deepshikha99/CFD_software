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
       top=tk.Frame(self)
       top.pack()
       top.place(relwidth=1, relheight=0.6)
       bottom=tk.Frame(self)
       bottom.pack()
       bottom.place(relwidth=1, relheight=0.4, rely=0.6)

       left=tk.Frame(top)
       left.pack()
       left.place(relwidth=0.5, relheight=1)
       right=tk.Frame(top)
       right.pack()
       right.place(relwidth=0.5, relheight=1, relx=0.5)

       label=tk.Label(left, text="Choose one from these", font=helv36)
       label.pack(anchor=tk.W)
       label.place(relx=0.3, rely=0.1, relheight=0.1)
       #Radiobuttons of Gmsh, BDF, DM
       rb=tk.Radiobutton(left, text='Gmsh', variable=preprocess, value=1, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.25, relx=0.3, relheight=0.1)
       rb=tk.Radiobutton(left, text='DM', variable=preprocess, value=2, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.40, relx=0.3, relheight=0.1)
       rb=tk.Radiobutton(left, text='BDF', variable=preprocess, value=3, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.55, relx=0.3, relheight=0.1)

       label=tk.Label(right, text="Select Parameters", font=helv36)
       label.pack()
       label.place(relx=0.3, rely=0.1, relheight=0.1)
       label = tk.Label(right, text="Mesh format", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.3, relheight=0.1, relwidth=0.5)
       meshformat.set("select")
       w = tk.OptionMenu(right, meshformat, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.3, relheight=0.1, relwidth=0.3)
       label = tk.Label(right, text="Geo Available", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.5, relheight=0.1, relwidth=0.5)
       geoavailable.set("select")
       w = tk.OptionMenu(right, geoavailable, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.3)

       
       label=tk.Label(bottom, text="Geo File: ", font=helv36)
       label.pack()
       label.place(rely=0.1, relx=0.05, relwidth=0.15, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=geofilename, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.6, relheight=0.15, rely=0.1, relx=0.2)
       def selectgeo():
        try:
          try:
              filledpre.tk.call('tk_getOpenFile', '-foobarbaz')
          except TclError:
              pass
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        except:
          pass
        def openfile():
        # geofile=filedialog.askopenfilename(title='Select file', filetypes=(('Geo files', '*.geo'), ('all files', '*.*')))
        # geofilename.set(ntpath.basename(geofile))
        # os.system("cp %s %s/%s/pre-processing"%(geofile, folder, project_name))
          buttonimp1.config(state="normal")
        openfile()
        bottom.bind('<Control-o>', openfile)
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectgeo)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.1, relx=0.8)
       
       def createmsh():
        # os.system("gmsh -2 %s/%s/pre-processing/%s"%(folder, project_name,geofilename.get()))
        buttonimp2.config(state="normal")
        filename=geofilename.get()
        msh=os.path.splitext(filename)[0]
        msh=msh+".msh"
        mshfilename.set(msh)
        filename=geofile
        mshe=os.path.splitext(filename)[0]
        mshfile=mshe+".msh"
        global sol1
        global sol2
        sol1=1
        if sol1==1 and sol2==1:
          sv.set("1")

       buttonimp1=tk.Button(bottom, text="Create msh", font=helv36, state="disabled", command=createmsh)
       buttonimp1.pack()
       buttonimp1.place(relwidth=0.20, relheight=0.15, rely=0.3, relx=0.4)

       label=tk.Label(bottom, text="Msh File: ", font=helv36)
       label.pack()
       label.place(rely=0.55, relx=0.05, relwidth=0.15, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=mshfilename, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.6, relheight=0.15, rely=0.55, relx=0.2)
       def selectmsh():
        try:
          try:
              filledpre.tk.call('tk_getOpenFile', '-foobarbaz')
          except TclError:
              pass
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        except:
          pass
        def openfile():
        # mshfile=filedialog.askopenfilename(title='Select file', filetypes=(('Msh files', '*.msh'), ('all files', '*.*')))
        # mshfilename.set(ntpath.basename(mshfile))
        # os.system("cp %s %s/%s/pre-processing"%(mshfile, folder, project_name))
          buttonimp2.config(state="normal")
          global sol1
          global sol2
          sol1=1
          if sol1==1 and sol2==1:
            sv.set("1")
        openfile()
        bottom.bind('<Control-o>', openfile)
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectmsh)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.55, relx=0.8)

       def showmsh():
        print("some")
        # os.system("gmsh %s/%s/pre-processing/%s"%(folder, project_name,mshfilename.get()))
       buttonimp2=tk.Button(bottom, text="Show msh", font=helv36, state="disabled", command=showmsh)
       buttonimp2.pack()
       buttonimp2.place(relwidth=0.20, relheight=0.15, rely=0.75, relx=0.4)
      

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       top=tk.Frame(self)
       top.pack()
       top.place(relwidth=1, relheight=0.6)
       bottom=tk.Frame(self)
       bottom.pack()
       bottom.place(relwidth=1, relheight=0.4, rely=0.6)

       left=tk.Frame(top)
       left.pack()
       left.place(relwidth=0.5, relheight=1)
       right=tk.Frame(top)
       right.pack()
       right.place(relwidth=0.5, relheight=1, relx=0.5)

       label=tk.Label(left, text="Choose one from these", font=helv36)
       label.pack(anchor=tk.W)
       label.place(relx=0.3, rely=0.1, relheight=0.1)
       #Radiobuttons of OpenFOAM, Fluent, Fluidity
       rb=tk.Radiobutton(left, text='OpenFOAM', variable=solver, value=1, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.25, relx=0.3, relheight=0.1)
       rb=tk.Radiobutton(left, text='Fluent', variable=solver, value=2, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.40, relx=0.3, relheight=0.1)
       rb=tk.Radiobutton(left, text='Fluidity', variable=solver, value=3, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.55, relx=0.3, relheight=0.1)

       label=tk.Label(right, text="Select Parameters", font=helv36)
       label.pack()
       label.place(relx=0.3, rely=0.1, relheight=0.1)

       label = tk.Label(right, text="Orientation", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.25, relheight=0.1, relwidth=0.5)
       orientation.set("select")
       w = tk.OptionMenu(right, orientation, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.25, relheight=0.1, relwidth=0.3)

       label = tk.Label(right, text="Number of Cores", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.4, relheight=0.1, relwidth=0.5)
       numberofcores.set("select")
       w = tk.OptionMenu(right, numberofcores, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.4, relheight=0.1, relwidth=0.3)

       label = tk.Label(right, text="Timestep", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.55, relheight=0.1, relwidth=0.5)
       timestep.set("select")
       w = tk.OptionMenu(right, timestep, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.55, relheight=0.1, relwidth=0.3)

       label = tk.Label(right, text="Simulation Time", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.7, relheight=0.1, relwidth=0.5)
       simulationtime.set("select")
       w = tk.OptionMenu(right, simulationtime, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.7, relheight=0.1, relwidth=0.3)

       
       label=tk.Label(bottom, text="Msh File: ", font=helv36)
       label.pack()
       label.place(rely=0.1, relx=0.05, relwidth=0.15, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=mshfilename, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.6, relheight=0.15, rely=0.1, relx=0.2)
       def selectmsh():
        global sol1
        global sol2
        sol1=1
        if sol1==1 and sol2==1:
          sv.set("1")
        try:
          try:
              filledpre.tk.call('tk_getOpenFile', '-foobarbaz')
          except TclError:
              pass
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        except:
          pass
        def openfile():
          print("some")
        # mshfile=filedialog.askopenfilename(title='Select file', filetypes=(('Msh files', '*.msh'), ('all files', '*.*')))
        # mshfilename.set(ntpath.basename(mshfile))
        # os.system("cp %s %s/%s/pre-processing"%(mshfile, folder, project_name))
        openfile()
        bottom.bind('<Control-o>', openfile)
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectmsh)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.1, relx=0.8)
       
       label=tk.Label(bottom, text="Flml File: ", font=helv36)
       label.pack()
       label.place(rely=0.55, relx=0.05, relwidth=0.15, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=flmlfilename, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.6, relheight=0.15, rely=0.55, relx=0.2)
       def selectflml():
        global sol1
        global sol2
        sol2=1
        if sol1==1 and sol2==1:
          sv.set("1")
        try:
          try:
              filledpre.tk.call('tk_getOpenFile', '-foobarbaz')
          except TclError:
              pass
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
          filledpre.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        except:
          pass
        def openfile():
          print("some")
        # flmlfile=filedialog.askopenfilename(title='Select file', filetypes=(('Flml files', '*.flml'), ('all files', '*.*')))
        # flmlfilename.set(ntpath.basename(flmlfile))
        # os.system("cp %s %s/%s"%(flmlfile, folder, project_name))
        openfile()
        bottom.bind('<Control-o>', openfile)
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectflml)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.55, relx=0.8)

       def createvtu():
        # os.chdir(r"%s/%s"%(folder, project_name))
        # os.system("fluidity ./solver/%s"%flmlfilename.get())
        # os.system("find %s/%s/ -maxdepth 1 -type f -print0 | xargs -0 mv -t %s/%s/postprocessor"%(folder, project_name, folder, project_name))
        sv2.set("1")
        postfoldername.set("%s/%s/postprocessor"%(folder, project_name))
       def callback(sv):
        if sv.get()=="1":
          buttonsolve.config(state="normal")
       sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
       buttonsolve=tk.Button(bottom, text="Run fluidity", font=helv36, state="disabled", command=createvtu)
       buttonsolve.pack()
       buttonsolve.place(relwidth=0.20, relheight=0.15, rely=0.75, relx=0.4)

       
class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       top=tk.Frame(self)
       top.pack()
       top.place(relwidth=1, relheight=0.6)
       bottom=tk.Frame(self)
       bottom.pack()
       bottom.place(relwidth=1, relheight=0.4, rely=0.6)

       left=tk.Frame(top)
       left.pack()
       left.place(relwidth=0.5, relheight=1)
       right=tk.Frame(top)
       right.pack()
       right.place(relwidth=0.5, relheight=1, relx=0.5)

       label=tk.Label(left, text="Choose one or more from these", font=helv36)
       label.pack(anchor=tk.W)
       label.place(relx=0.2, rely=0.1, relheight=0.1)
       #Checkbuttons of Paraview, TechPlot and Python
       rb=tk.Checkbutton(left, text="Paraview", variable=postprocess1, onvalue=1, offvalue=0, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.25, relx=0.3, relheight=0.1)
       rb=tk.Checkbutton(left, text="Techplot", variable=postprocess2, onvalue=1, offvalue=0, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.40, relx=0.3, relheight=0.1)
       rb=tk.Checkbutton(left, text="Python", variable=postprocess3, onvalue=1, offvalue=0, font=helv36, fg="maroon4")
       rb.pack(anchor=tk.W)
       rb.place(rely=0.55, relx=0.3, relheight=0.1)

       label=tk.Label(right, text="Select Parameters", font=helv36)
       label.pack()
       label.place(relx=0.3, rely=0.1, relheight=0.1)
       label = tk.Label(right, text="Animation", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.3, relheight=0.1, relwidth=0.5)
       animation.set("select")
       w = tk.OptionMenu(right, animation, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.3, relheight=0.1, relwidth=0.3)
       label = tk.Label(right, text="Plot", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.5, relheight=0.1, relwidth=0.5)
       plot.set("select")
       w = tk.OptionMenu(right, plot, "select", "one", "two", "three")
       w.config(font=SMALL_FONT)
       w.pack()
       w.place(relx=0.5, rely=0.5, relheight=0.1, relwidth=0.3)


       label=tk.Label(bottom, text="Solver Folder: ", font=helv36)
       label.pack()
       label.place(rely=0.2, relx=0, relwidth=0.2, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=postfoldername, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.6, relheight=0.15, rely=0.2, relx=0.2)     

       def selectpost():
        sv2.set("1")
        try:
          try:
              root.tk.call('tk_getOpenFile', '-foobarbaz')
          except TclError:
              pass
          root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
          root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        except:
            pass
        root.tk.call('set', '::tk::dialog::file::showHiddenBtn', '1')
        root.tk.call('set', '::tk::dialog::file::showHiddenVar', '0')
        # postfolder = tk.filedialog.askdirectory()
        # postfoldername.set(postfolder)
        # os.system(""find %s/ -maxdepth 1 -type f -print0 | xargs -0 cp -t %s/%s/postprocessor"%(postfolder, folder, project_name)")
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectpost)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.2, relx=0.8)  
       def callback(sv):
        if sv2.get()=="1":
          buttonpost.config(state="normal")
       sv2.trace("w", lambda name, index, mode, sv=sv2: callback(sv2))
       def paraview():
        print("some")
        # os.system("find %s/files/ -maxdepth 1 -type f -print0 | xargs -0 cp -t %s/%s/postprocessor"%(curdir, folder, project_name))
        # os.chdir(r"%s/%s/postprocessor"%(folder, project_name))
        # os.system("python plot_data.py")
        
       buttonpost=tk.Button(bottom, text="Run paraview", font=helv36, command=paraview, state="disabled")
       buttonpost.pack()
       buttonpost.place(relwidth=0.20, relheight=0.15, rely=0.5, relx=0.4)


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
    