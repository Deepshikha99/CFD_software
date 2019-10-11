import tkinter as tk
from tkinter import filedialog
import os
import errno
from tkinter import font
curdir=os.getcwd()
folder = ""
project_name=""
flag=0
LARGE_FONT= ("Verdana", 16)
MEDIUM_FONT= ("Verdana", 12)
SMALL_FONT= ("Verdana", 9) 
flag2=0
def build():
	root=tk.Tk()
	root.resizable(0, 0)
	global flag
	#entry variable for storing project name
	sv=tk.StringVar(root)

	#project location
	

	#stores the current directory
	curdir=folder

	#to track if appropriate folders are created. The flag becomes 1 when folders are created.
	

	#window name
	root.title("CFD Software")

	#font styles
	helv36=font.Font(family='Helvetica', size=15)
	helv40=font.Font(family='Helvetica', size=16)

	#Project Title
	label=tk.Label(root, text="CFD SOFTWARE", fg="white", bg="black")
	label.config(font=("Courier", 20))
	label.pack()
	label.place(relheight=0.1, relwidth=1)

	#frame to show and take project name
	frame=tk.Frame(root)
	frame.pack()
	frame.place(relheight=0.7, relwidth=1, rely=0.1)
	label=tk.Label(frame, text="Create new Project", font=LARGE_FONT)
	label.pack()
	label.place(relwidth=1, relheight=0.2)
	label=tk.Label(frame, text="Project Name: ")
	label.config(font=helv36)
	label.pack()
	label.place(relwidth=0.25, relheight=0.2, rely=0.25)

	#To trace if create button should be enabled or disabled according to project name variable
	def callback(sv):
		global project_name
		project_name=sv.get()
		if sv.get()!="":
			button1.config(state="normal")
		else:
			button1.config(state="disabled")
	sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
	#E1 to take entry of project name
	E1 = tk.Entry(frame, textvariable=sv, bd =5, bg="gray88")
	E1.config(font=helv36)
	E1.pack()
	E1.place(relwidth=0.6, relheight=0.2, rely=0.25, relx=0.25)
	E1.focus_set()

	#frame to store and take project location name
	# frame=tk.Frame(root)
	# frame.pack()
	# frame.place(relheight=)
	label=tk.Label(frame, text="Project Location: ")
	label.config(font=helv36)
	label.pack()
	label.place(relwidth=0.25, relheight=0.2, rely=0.5)
	label=tk.Label(frame, text=folder, relief="sunken", bg="gray88")
	label.config(font=("Arial", 16))
	label.pack()
	label.place(relwidth=0.6, relheight=0.2, rely=0.5, relx=0.25)

	#to take project location from user
	def location():
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
	    global folder
	    folder = tk.filedialog.askdirectory()
	    global label
	    # label.destroy()
	    label=tk.Label(frame, text=folder, relief="sunken", bg="gray88")
	    label.config(font=("Arial", 16))
	    label.pack()
	    label.place(relwidth=0.6, relheight=0.2, rely=0.5, relx=0.25)
	#button to browse for project location
	button=tk.Button(frame, text="Browse", command=location, bg="gray88")
	button.config(font=helv36)
	button.pack()
	button.place(relwidth=0.13, relheight=0.2, rely=0.5, relx=0.87)

	#to create project folder and pre-processing, solver, post-processing folders inside it
	def create():
	    global folder
	    global project_name
	    
	    text1=project_name
	    path="%s/%s"%(folder, text1)
	    #create main directory
	    try:
	        os.makedirs(path)
	    except OSError as exc:
	        if exc.errno == errno.EEXIST and os.path.isdir(path):
	            pass
	        else:
	            raise
	    #create pre-processing directory
	    create=os.path.join(path, "pre-processing")
	    try:
	        os.makedirs(create)
	    except OSError as exc:
	        if exc.errno == errno.EEXIST and os.path.isdir(create):
	            pass
	        else:
	            raise
	    #create solver directory
	    create=os.path.join(path, "solver")
	    try:
	        os.makedirs(create)
	    except OSError as exc:
	        if exc.errno == errno.EEXIST and os.path.isdir(create):
	            pass
	        else:
	            raise
	    #create post-processing directory
	    create=os.path.join(path, "postprocessor")
	    try:
	        os.makedirs(create)
	    except OSError as exc:
	        if exc.errno == errno.EEXIST and os.path.isdir(create):
	            pass
	        else:
	            raise
	    global flag
	    flag=1
	    root.destroy()
	    
	     #once the folders are created, flag value is made 1 and this window is destroyed

	#button to create folders
	button1=tk.Button(frame, text="Create", command=create, bg="gray88") 
	button1.config(font=helv36, state="disabled")
	button1.pack()
	button1.place(relwidth=0.2, relheight=0.2, rely=0.75, relx=0.4)

	frame1=tk.Frame(root)
	frame1.pack()
	frame1.place(relwidth=1, relheight=0.2, rely=0.8)
	label=tk.Label(frame1, text="Already existing project?")
	label.config(font=LARGE_FONT)
	label.pack()
	label.place(relheight=0.8, relwidth=0.4, relx=0.2)

	def openexisting():
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
	    global folder
	    global project_name
	    fold = tk.filedialog.askdirectory()
	    project_name=os.path.basename(fold)
	    folder=os.path.dirname(fold)
	    global flag2
	    flag2=1
	    create()
	button=tk.Button(frame1, text="Open", font=helv36, command=openexisting)
	button.pack()
	button.place(relheight=0.8, relwidth=0.15, relx=0.6)


	#specifications of window

	root.geometry("750x350")
	root.update()
	windowWidth=root.winfo_width()
	windowHeight=root.winfo_height()
	# print(root.winfo_height())
	# print(root.winfo_reqheight())
	# windowWidth = root.winfo_reqwidth()
	# windowHeight = root.winfo_reqheight()
	positionRight = int((root.winfo_screenwidth()/2 - windowWidth/2))
	positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
	root.geometry("+{}+{}".format(positionRight, positionDown))
	
	 #window size can't be changed
	root.mainloop()
	return folder, project_name, flag, flag2
build()
