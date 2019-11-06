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
import ntpath
import glob

LARGE_FONT= ("Verdana", 16)
MEDIUM_FONT= ("Verdana", 12)
SMALL_FONT= ("Verdana", 9) 

curdir=os.getcwd()
curdir="/home/khushi/Desktop/cfd"

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global filehandle
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
          file=filedialog.askopenfilename(title='Select file', filetypes=(('Geo files', '*.geo'), ('all files', '*.*')))
          if not file:
            return
          geofile=file
          geofilename.set(ntpath.basename(geofile))
          os.system("cp %s %s/%s/pre-processing"%(geofile, folder, project_name))
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="%s is now present in pre-processing folder."%geofilename.get()
          logging.info(msg)
          logging.info("\n")
          filehandle.write(msg+"\n")
          if buttonimp1['state']=="disabled":
            buttonimp1.config(state="normal")
            timeStr = time.asctime()
            msg="Time: "+timeStr
            logging.info(msg)
            filehandle.write(msg+"\n")
            msg="'Create msh' button if pressed, takes a little time. Kindly wait until the process finishes."
            logging.info(msg)
            filehandle.write(msg+"\n")
            logging.info("\n")
        openfile()
        bottom.bind('<Control-o>', openfile)
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectgeo)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.1, relx=0.8)
       
       def createmsh():
        count=0
        for file in os.listdir("%s/%s/pre-processing"%(folder, project_name)):
          if file.endswith(".msh"):
              count+=1
        os.system("gmsh -2 %s/%s/pre-processing/%s"%(folder, project_name,geofilename.get()))
        count2=0
        for file in os.listdir("%s/%s/pre-processing"%(folder, project_name)):
          if file.endswith(".msh"):
              count2+=1
        if ((count2-count)!=1):
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="No new file created. Look at the terminal window for more details."
          logging.info(msg)
          logging.info("\n")
          filehandle.write(msg+"\n")
          return
         
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="%s.msh is created and is saved in pre-processing folder."%os.path.splitext(geofilename.get())[0]
        logging.info(msg)
        logging.info("\n")
        filehandle.write(msg+"\n")

        if buttonimp2['state']=="disabled":
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="'Show msh' button if pressed, takes a little time. Kindly wait until the process completes."
          logging.info(msg)
          filehandle.write(msg+"\n")
          logging.info("\n")
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
       if geofile=="":
        buttonimp1=tk.Button(bottom, text="Create msh", font=helv36, state="disabled", command=createmsh)
        buttonimp1.pack()
        buttonimp1.place(relwidth=0.20, relheight=0.15, rely=0.3, relx=0.4)
       else:
        buttonimp1=tk.Button(bottom, text="Create msh", font=helv36, command=createmsh)
        buttonimp1.pack()
        buttonimp1.place(relwidth=0.20, relheight=0.15, rely=0.3, relx=0.4)
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="'Create msh' button if pressed, takes a little time. Kindly wait until the process finishes."
        logging.info(msg)
        filehandle.write(msg+"\n")
        logging.info("\n")


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
          file=filedialog.askopenfilename(title='Select file', filetypes=(('Msh files', '*.msh'), ('all files', '*.*')))
          if not file:
            return
          mshfile=file
          mshfilename.set(ntpath.basename(mshfile))
          os.system("cp %s %s/%s/pre-processing"%(mshfile, folder, project_name))
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="%s is present in pre-processing folder."%mshfilename.get()
          logging.info(msg)
          logging.info("\n")
          filehandle.write(msg+"\n")
          if buttonimp2['state']=="disabled":
            buttonimp2.config(state="normal")
            timeStr = time.asctime()
            msg="Time: "+timeStr
            logging.info(msg)
            filehandle.write(msg+"\n")
            msg="'Show msh' button if pressed, takes a little time. Kindly wait until the process completes."
            logging.info(msg)
            filehandle.write(msg+"\n")
            logging.info("\n")
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
        os.system("gmsh %s/%s/pre-processing/%s"%(folder, project_name,mshfilename.get()))
       if mshfile=="":
        buttonimp2=tk.Button(bottom, text="Show msh", font=helv36, state="disabled", command=showmsh)
        buttonimp2.pack()
        buttonimp2.place(relwidth=0.20, relheight=0.15, rely=0.75, relx=0.4)
       else:
        buttonimp2=tk.Button(bottom, text="Show msh", font=helv36, command=showmsh)
        buttonimp2.pack()
        buttonimp2.place(relwidth=0.20, relheight=0.15, rely=0.75, relx=0.4)
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="'Show msh' button if pressed, takes a little time. Kindly wait until the process completes."
        logging.info(msg)
        filehandle.write(msg+"\n")
        logging.info("\n")

       

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global filehandle
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
       rb=tk.Radiobutton(left, text='OpenFOAM', variable=solver, value=1, font=helv36, fg="maroon4", command = lambda : getScript(rb))
       rb.pack(anchor=tk.W)
       rb.place(rely=0.25, relx=0.3, relheight=0.1)
       rb=tk.Radiobutton(left, text='Fluent', variable=solver, value=2, font=helv36, fg="maroon4", command = lambda : getScript(rb))
       rb.pack(anchor=tk.W)
       rb.place(rely=0.40, relx=0.3, relheight=0.1)
       rb=tk.Radiobutton(left, text='Fluidity', variable=solver, value=3, font=helv36, fg="maroon4", command = lambda : getScript(rb))
       rb.pack(anchor=tk.W)
       rb.place(rely=0.55, relx=0.3, relheight=0.1)

       label=tk.Label(right, text="Select Parameters", font=helv36)
       label.pack()
       label.place(relx=0.3, rely=0.1, relheight=0.1)

       label = tk.Label(right, text="Orientation", font=helv36, fg="dark green")
       label.pack()
       label.place(relx=0, rely=0.25, relheight=0.1, relwidth=0.5)
       orientation.set("select")
       w = tk.OptionMenu(right, orientation, "select", "series", "parallel")
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


       tempframe=tk.Frame(self)
       templabel1=tk.Label(tempframe, text="File: ", font=helv36)
       templabel1.pack()
       templabel1.place(rely=0.3, relx=0.05, relwidth=0.15, relheight=0.15)
       templabel2=tk.Label(tempframe, textvariable=dictfile, font=helv36, relief="sunken")
       templabel2.pack()
       templabel2.place(relwidth=0.6, relheight=0.15, rely=0.3, relx=0.2)
       def selectdict():
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
          file=filedialog.askopenfilename(title='Select file', filetypes=(('Msh files', '**'), ('all files', '**')))
          if not file:
            return
          dictfile.set(file)
          # print(dictfile.get())
          tempbutton.config(state="normal")
        openfile()
       tempbutton2=tk.Button(tempframe, text="Browse", font=helv36, command=selectdict)
       tempbutton2.pack()
       tempbutton2.place(relwidth=0.15, relheight=0.15, rely=0.3, relx=0.8)
       def openfoam():
        file=os.path.dirname(dictfile.get())
        file2=os.path.basename(dictfile.get())
        file3=os.path.dirname(file)
        os.chdir(r"%s"%file3)
        # print(os.getcwd())
        os.system("paraFoam")
       tempbutton=tk.Button(tempframe, text="Run", font=helv36, command=openfoam, state="disabled")
       tempbutton.pack()
       tempbutton.place(relwidth=0.4, relx=0.3, relheight=0.2, rely=0.6)

       def getScript(widget):
        if solver.get()==1:
          tempframe.pack(in_=bottom)
          tempframe.place(relwidth=1, relheight=0.4, rely=0.6)
          tempframe.lift()
        else:
          tempframe.lower(bottom)

       solver.trace("w", lambda name, index, mode, sv=solver: callback(solver))

       label=tk.Label(bottom, text="Msh File: ", font=helv36)
       label.pack()
       label.place(rely=0.1, relx=0.05, relwidth=0.15, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=mshfilename, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.6, relheight=0.15, rely=0.1, relx=0.2)
       def selectmsh():
        # solver.set(3)
        # print(solver.get())
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
          file=filedialog.askopenfilename(title='Select file', filetypes=(('Msh files', '*.msh'), ('all files', '*.*')))
          if not file:
            return
          mshfile=file
          mshfilename.set(ntpath.basename(mshfile))
          os.system("cp %s %s/%s/pre-processing"%(mshfile, folder, project_name))
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="%s is now present in pre-processing folder."%mshfilename.get()
          logging.info(msg)
          logging.info("\n")
          filehandle.write(msg+"\n")
        openfile()
        bottom.bind('<Control-o>', openfile)
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectmsh)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.1, relx=0.8)
       
       label=tk.Label(bottom, text="Flml File: ", font=helv36)
       label.pack()
       label.place(rely=0.3, relx=0.05, relwidth=0.15, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=flmlfilename, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.6, relheight=0.15, rely=0.3, relx=0.2)
       def selectflml():
        global sol1
        global sol2
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
          file=filedialog.askopenfilename(title='Select file', filetypes=(('Flml files', '*.flml'), ('all files', '*.*')))
          if not file:
            return
          flmlfile=file
          flmlfilename.set(ntpath.basename(flmlfile))
          os.system("cp %s %s/%s/solver"%(flmlfile, folder, project_name))
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="%s is now present in %s folder."%(flmlfilename.get(), project_name)
          logging.info(msg)
          logging.info("\n")
          filehandle.write(msg+"\n")
          sol2=1
          if sol1==1 and sol2==1:
            sv.set("1")
        openfile()
        bottom.bind('<Control-o>', openfile)
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectflml)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.3, relx=0.8)


       def createvtu():
        if orientation.get()=="parallel":
          DIR = '%s/%s/postprocessor'%(folder, project_name)
          count= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
          os.chdir(r"%s/%s"%(folder, project_name))
          os.system("mpiexec -n 4 flredecomp -i 1 -o 4 ./solver/water_collapse ./solver/water_collapse_flredecomp")
          # os.system("fluidity ./solver/%s"%flmlfilename.get())
          os.system("mpiexec -n 4 fluidity -v2 -l ./solver/water_collapse_flredecomp.flml")
          for x in os.listdir("%s/%s"%(folder, project_name)):
            if x!="pre-processing" and x!="solver" and x!="postprocessor":
              os.system("mv %s/%s/%s %s/%s/postprocessor"%(folder, project_name, x, folder, project_name))
          count2= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        else:
          DIR = '%s/%s/postprocessor'%(folder, project_name)
          count= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
          os.chdir(r"%s/%s"%(folder, project_name))
          os.system("fluidity ./solver/%s"%flmlfilename.get())
          os.system("find %s/%s/ -maxdepth 1 -type f -print0 | xargs -0 mv -t %s/%s/postprocessor"%(folder, project_name, folder, project_name))
          count2= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        if (count2-count)==0:
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="No new files are created. Look at the terminal for more details."
          logging.info(msg)
          logging.info("\n")
          filehandle.write(msg+"\n")
          return
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="All vtu files are now present in postprocessor folder."
        logging.info(msg)
        logging.info("\n")
        filehandle.write(msg+"\n")
        sv2.set("1")
        postfoldername.set("%s/%s/postprocessor"%(folder, project_name))
       def callback(sv):
        print(sv.get())
        if sv.get()=="1":
          # if buttonsolve['config']=="disabled":
          buttonsolveimp.config(state="normal")
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="'Run fluidity' button if pressed, takes a long time. Kindly wait until the process completes."
          logging.info(msg)
          filehandle.write(msg+"\n")
          logging.info("\n")
       sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
       if temp==0:
        buttonsolveimp=tk.Button(bottom, text="Run fluidity", font=helv36, state="disabled", command=createvtu)
        buttonsolveimp.pack()
        buttonsolveimp.place(relwidth=0.20, relheight=0.15, rely=0.55, relx=0.4)
       else:
        buttonsolveimp=tk.Button(bottom, text="Run fluidity", font=helv36, command=createvtu)
        buttonsolveimp.pack()
        buttonsolveimp.place(relwidth=0.20, relheight=0.15, rely=0.55, relx=0.4)
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="'Run fluidity' button if pressed, takes a long time. Kindly wait until the process completes."
        logging.info(msg)
        filehandle.write(msg+"\n")
        logging.info("\n")

       def showvtu():
        os.chdir(r"%s/%s/postprocessor"%(folder, project_name))
        os.system("paraview")
       buttonsolve=tk.Button(bottom, text="Show files", font=helv36, command=showvtu)
       buttonsolve.pack()
       buttonsolve.place(relwidth=0.20, relheight=0.15, rely=0.75, relx=0.4)

class Page3(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       global filehandle
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


       label=tk.Label(bottom, text="Postprocessor Folder: ", font=helv36)
       label.pack()
       label.place(rely=0.2, relx=0, relwidth=0.23, relheight=0.15)
       labelpre=tk.Label(bottom, textvariable=postfoldername, relief="sunken", width="20")
       labelpre.config(font=("Arial", 12), pady=10)
       labelpre.pack()
       labelpre.place(relwidth=0.57, relheight=0.15, rely=0.2, relx=0.23)     

       def selectpost():
        
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
        postfolder = tk.filedialog.askdirectory()
        postfoldername.set(postfolder)
        if orientation.get()=="parallel":
          for x in os.listdir("%s"%postfoldername.get()):
            if x!="pre-processing" and x!="solver" and x!="postprocessor":
              os.system("mv %s/%s %s/%s/postprocessor"%(postfolder, x, folder, project_name))
        else:
          os.system("find %s/ -maxdepth 1 -type f -print0 | xargs -0 cp -t %s/%s/postprocessor"%(postfolder, folder, project_name))
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="Selected folder files are now in postprocessor folder."
        logging.info(msg)
        logging.info("\n")
        filehandle.write(msg+"\n")
        sv2.set("1")
       button=tk.Button(bottom, text="Browse", font=helv36, command=selectpost)
       button.pack()
       button.place(relwidth=0.15, relheight=0.15, rely=0.2, relx=0.8)  
       def callback(sv):
        if sv2.get()=="1":
          # if buttonpost['config']=="disabled":
          buttonpost.config(state="normal")
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="'Postprocess' button if pressed, takes a little time. Kindly wait until the process completes."
          logging.info(msg)
          filehandle.write(msg+"\n")
          logging.info("\n")
       sv2.trace("w", lambda name, index, mode, sv=sv2: callback(sv2))
       def paraview():
        if orientation.get()=="parallel":
          os.system("find %s/files2/ -maxdepth 1 -type f -print0 | xargs -0 cp -t %s/%s/postprocessor"%(curdir, folder, project_name)) 
        else:
          os.system("find %s/files/ -maxdepth 1 -type f -print0 | xargs -0 cp -t %s/%s/postprocessor"%(curdir, folder, project_name))
        DIR = '%s/%s/postprocessor'%(folder, project_name)
        count= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        os.chdir(r"%s/%s/postprocessor"%(folder, project_name))
        os.system("python plot_data.py")
        DIR = '%s/%s/postprocessor'%(folder, project_name)
        count2= len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        if (count2-count)==0:
          timeStr = time.asctime()
          msg="Time: "+timeStr
          logging.info(msg)
          filehandle.write(msg+"\n")
          msg="No new files are created. Look at the terminal for more details."
          logging.info(msg)
          logging.info("\n")
          filehandle.write(msg+"\n")
          return
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="Output files are created and are present in postprocessor folder."
        logging.info(msg)
        logging.info("\n")
        filehandle.write(msg+"\n")
       buttonpost=tk.Button(bottom, text="Postprocess", font=helv36, command=paraview)
       buttonpost.pack()
       buttonpost.place(relwidth=0.20, relheight=0.15, rely=0.5, relx=0.4)

def head(self):
  st = ScrolledText.ScrolledText(self, state='normal')
  st.configure(font='TkFixedFont', bg="white")
  st.pack(expand="true", fill="both")

  # Create textLogger
  text_handler = TextHandler(st)
  
  # Logging configuration
  logging.basicConfig(filename='test.log',
      level=logging.INFO, 
      format='%(asctime)s - %(levelname)s - %(message)s')        
  
  # Add the handler to logger
  logger = logging.getLogger()        
  logger.addHandler(text_handler)

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
        head(self.logwindow)    
        header=tk.Frame(self.mainwindow)
        header.pack()
        header.place(relwidth=1, relheight=0.1)
        header.tkraise()
        mainsection=tk.Frame(self.mainwindow)
        mainsection.pack()
        mainsection.place(relheight=0.9, relwidth=1, rely=0.1)
        global flag2
        global filehandle
        if flag2==1:
          try:
            filehandle=open("%s/%s/run.log"%(folder, project_name), 'r')
            for x in filehandle:
              logging.info(x)
            filehandle.close()
          except:
            pass
          filehandle=open("%s/%s/run.log"%(folder, project_name), 'a')
        timeStr = time.asctime()
        msg="Time: "+timeStr
        logging.info(msg)
        filehandle.write(msg+"\n")
        msg="The current working folder is %s. It has subdirectories of pre-processing, solver and postprocessor."%project_name
        logging.info(msg)
        logging.info("\n")
        filehandle.write(msg+"\n")

        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        # if sol1==1 and sol2==1:
        #   sv.set("1")

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

class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    
    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(tk.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tk.END)
        self.text.after(0, append)

 
if __name__ == "__main__":
    folder, project_name, flag, flag2=project.build()
    logging.getLogger().setLevel(logging.INFO)
    if flag==0:
      exit(0)
    if flag2==0:
      filehandle = open("%s/%s/run.log"%(folder, project_name), 'w')
    root = tk.Tk()
    root.title("%s/%s-CFD Software"%(folder, project_name))
    root.geometry("1500x1500")
    root.minsize(1200, 500)
    helv36 = font.Font(family='Helvetica', size=15)
    helv26 = font.Font(family='Helvetica', size=12)
    preprocess=tk.IntVar(root)
    preprocess.set(1)
    solver=tk.IntVar(root)
    solver.set(3)
    postprocess1=tk.IntVar(root)
    postprocess2=tk.IntVar(root)
    postprocess3=tk.IntVar(root)
    postprocess3.set(1)
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
    dictfile=tk.StringVar(root)
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
    count=0
    if flag2==1:
      for file in os.listdir("%s/%s/pre-processing"%(folder, project_name)):
        if file.endswith(".geo"):
            geofile=(os.path.join("%s/%s/pre-processing"%(folder, project_name), file))
            geofilename.set(file)
            count+=1
      if count!=1:
        geofile=""
        geofilename.set("")
      if count==1:
        sol1=1
      count=0
      for file in os.listdir("%s/%s/pre-processing"%(folder, project_name)):
        if file.endswith(".msh"):
            mshfile=(os.path.join("%s/%s/pre-processing"%(folder, project_name), file))
            mshfilename.set(file)
            count+=1
      if count!=1:
        mshfile=""
        mshfilename.set("") 
      if count==1:
        sol2=1 
      count=0
      for file in os.listdir("%s/%s/solver"%(folder, project_name)):
        if file.endswith(".flml"):
            flmlfile=(os.path.join("%s/%s/solver"%(folder, project_name), file))
            flmlfilename.set(file)
            count+=1
      if count!=1:
        flmlfile=""
        flmlfilename.set("") 
    postfolder=folder+"/"+project_name+"/postprocessor"
    postfoldername.set(postfolder)
    temp=0   
    if sol1==1 and sol2==1:
      temp=1
    main = MainView(root)    
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
    filehandle.close()
    