from tkinter import *
import os
from tkinter import messagebox
 
creds = 'tempfile.temp'


def Signup():
	global pwordE
	global nameE
	global roots

	roots = Tk()
	roots.title('Secret')
	roots.geometry("400x400")
	
	instruction = Label(roots, text='Please Enter new Credentials')
	instruction.pack()

	nameL = Label(roots, text='New Username: ',font = ("calibri",12,"bold"))
	pwordL = Label(roots,text='New Password: ',font = ("calibri",12,"bold"))
	nameL.pack()
	

	nameE = Entry(roots,font = ("calibri",12,"bold"))
	nameE.pack()
	pwordL.pack()
	pwordE = Entry(roots, show='*',font = ("calibri",12,"bold"))
	pwordE.pack()
	

	signupButton = Button(roots, text='Signup', command=FSSignup, font =("calibri",12,"bold"))
	signupButton.pack()
	roots.mainloop()

def FSSignup():
	with open(creds, 'w') as f:
		f.write(nameE.get())	
		f.write('\n')
		f.write(pwordE.get())
		f.close()

	roots.destroy()
	Login()

def Login():
	global nameEL
	global pwordEL
	global rootA

	rootA = Tk()
	rootA.title('Secret-Data')
	rootA.geometry("400x400")
	l =Label(rootA, text="*****SMDEV*****", font = ("calibri",20,"bold"))
	l.pack()
	l.configure(background='sky blue')
	instruction = Label(rootA, text='Please Login\n', font = ("calibri",20,"bold"))
	instruction.pack()

	nameL = Label(rootA, text='Username: ',font = ("calibri",12,"bold"))
	nameL.pack()
	nameEL = Entry(rootA, font =("calibri",12,"bold"))
	nameEL.pack()
	pwordEL = Entry(rootA, show='*', font = ("calibri",12,"bold"))
	pwordL = Label(rootA, text='Password: ',font = ("calibri",12,"bold"))
	pwordL.pack()
	pwordEL.pack()
	Label(rootA).pack()
	loginB = Button(rootA, text='Login', command=CheckLogin,font = ("calibri",12,"bold"))
	loginB.pack()
	Label(rootA).pack()
	rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser,font = ("calibri",12,"bold"))
	rmuser.pack()
	rootA.mainloop()
def Search_PlayerData():
	
	win = Tk()
	win.title("Search Your Notes")
	win.geometry("350x200")
	win.configure(background='green')
	l=Label(win, text="Please Enter File Name", font=('Arial',15,'bold'))
	l.pack()
	l.configure(background='green')
	searchvalue = StringVar()
	entry1 = Entry(win, textvariable=searchvalue,font=('Arial',20, 'bold'))
	entry1.pack()
	def Openfile():
		try:
			file=open(entry1.get(), 'r')
			data=file.readlines()
			win2 = Tk()
			win2.title('Show Info')
			win2.geometry('400x400')
			Label(win2, text=f' Name: {data[0]}', font=('Arial',20,'bold')).pack()
			Label(win2, text=f' Runrate: {data[1]}', font=('Arial',20,'bold')).pack()
			Label(win2, text=f' Best Score: {data[2]}', font=('Arial',20,'bold')).pack()
			Label(win2, text=f' Position: {data[3]}', font=('Arial',20,'bold')).pack()
			Label(win2, text=f' Average: {data[4]}', font=('Arial',20,'bold')).pack()
  		    
			file.close()
		except:
			messagebox.showinfo('Information', message='File not exists')
		
	btn = Button(win, text='Search', command=Openfile,font=('calibri',20,'bold'))
	btn.pack()
        
# check Login Function + creating further functionalities
def CheckLogin():
	with open(creds) as f:
		data = f.readlines()
		uname = data[0].rstrip()
		pword = data[1].rstrip()

	if nameEL.get() == uname and pwordEL.get() == pword:
		r = Tk()
		r.title('Main Screen')
		r.geometry('300x300')
	#Function For Adding Player Information

		def AddPlayer():
			p = Tk()
			p.title("Player add")
			p.geometry("300x200")
			t_label=Label(p, text='Enter Player Name',font=('Arial',15, 'bold'))
			t_label.pack()
			t_label.configure(background='green')
			
			name=StringVar()
			P_name= Entry(p, textvariable=name, font=('Arial', 15, 'bold'))
			P_name.pack()
			 #function for creating player data file
			def Create_PlayerFile():
				try:
					file=open(P_name.get(), 'w')
					win = Tk()
					win.title('Player Information Adding Page')
					win.geometry('500x300')
					win.configure(background='green')
					u_namevar = StringVar()
					run_ratevar = StringVar()
					best_scorevar = StringVar()
					team_var = StringVar()
					position_var = StringVar()
					average_var  = StringVar()


					u_namelbl=Label(win, text='Name: ',font=('Arial',15,'bold'))
					u_namelbl.grid(row=2, column=2)
					u_namelbl.configure(background='green')
					u_nametxt=Entry(win, textvariable=u_namevar, font=('Arial',15,'bold'))
					u_nametxt.grid(row=2, column=4)
					Runratelbl=Label(win, text='Run Rate: ',font=('Arial',15,'bold'))
					Runratelbl.grid(row=4, column=2)
					Runratelbl.configure(background='green')
					runrate_var=Entry(win, textvariable=run_ratevar, font=('Arial',15,'bold'))
					runrate_var.grid(row=4, column=4)
					bestscorelbl=Label(win, text='Best Score: ',font=('Arial',15,'bold'))
					bestscorelbl.grid(row=6, column=2)
					bestscorelbl.configure(background='green')
					best_scoretxt=Entry(win, textvariable=best_scorevar, font=('Arial',15,'bold'))
					best_scoretxt.grid(row=6, column=4)
					Positionlbl=Label(win, text='Position: ',font=('Arial',15,'bold'))
					Positionlbl.grid(row=8, column=2)
					Positionlbl.configure(background='green')
					Positiontxt=Entry(win, textvariable=position_var, font=('Arial',15,'bold'))
					Positiontxt.grid(row=8, column=4)
					averagelbl=Label(win, text='Average: ', font=('Arial',15,'bold'))
					averagelbl.grid(row=10, column=2)
					averagelbl.configure(background='green')
					averagetxt= Entry(win, textvariable=average_var, font=('Arial',15,'bold'))
					averagetxt.grid(row=10, column=4)
					# creating Player Info Save btn Functionality
					def Savess():
						file.write(u_nametxt.get())
						file.write('\n')
						file.write(runrate_var.get())
						file.write('\n')
						file.write(best_scoretxt.get())
						file.write('\n')
						file.write(Positiontxt.get())
						file.write('\n')
						file.write(averagetxt.get())	
						file.write('\n')
						file.close()
						win.destroy()
					btn = Button(win, text= 'Save',font=('Arial',15,'bold'),command=Savess)
					btn.grid(row=13, column=4)
					
				except:
					messagebox.showinfo('Info!', message='File cannot be created')
			#Creating S_btn Functionality
			def Save_Btn():
				win = Tk()
				win.title('Add Player Info')
				win.geometry('500x300')
				win.configure(background='green')

				# creating Savebtn
				savebtn=Button(win, text='Save', font=('Arial',20,'bold'),command=Savebtnn)
				savebtn.grid(row=10, column=3)
				savebtn.configure(background='yellow')

				teamlbl=Label(win, text='Best Score: ',font=('Arial',15,'bold'))
				teamlbl.grid(row=8, column=2)
				teamlbl.configure(background='green')
				teamtxt=Entry(win, textvariable=team_var, font=('Arial',15,'bold'))
				teamtxt.grid(row=8, column=4)
			S_btn=Button(p, text="Done", font=('Arial',20,'bold'),command= Create_PlayerFile)
			S_btn.pack()
			
			p.configure(background='green')
		
		rlbl = Label(r, text= 'Welcome '+nameEL.get()+'\n[+] Logged In',font = ("calibri",20,'bold'))
		rlbl.pack()
		btn = Button(r, text = "Add Player Info",command=AddPlayer,font = ('calibri',12,'bold'))
		btn.pack()
		Label(r).pack()
		btn1 = Button(r, text = "Search Player Info",command=Search_PlayerData, font = ("calibri",12,"bold"))
		btn1.pack()
		rootA.destroy()
		r.mainloop()
	else:
		r = Tk()	
		r.title('D:')
		r.geometry('150x50')
		rlbl = Label(r, text='\n[! Invalid Login')
		rlbl.pack()
		r.mainloop()	

def DelUser():
	os.remove(creds)
	rootA.destroy()
	Signup()

if os.path.isfile(creds):
	Login()
else:
	Signup()
