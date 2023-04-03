from tkinter import *
import tkinter.messagebox
import mysql.connector
from prettytable import PrettyTable
import datetime
#connect mysqldb to python
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 passwd="root",
 port=3306,
 )
#declare the global variables
global st, et, des_slot,f,l,r,rn
global STARTTIME
global ENDTIME
#global v1,v2,v3,v4,v5,v6,v7,v8,v9
bw4=Tk()
bw4.withdraw()
bw2=Tk()
bw2.withdraw()
bw3=Tk()
bw3.withdraw()
 
in1 = IntVar()
in2 = IntVar()
in3 = IntVar()
in4 = IntVar()
in5 = IntVar()
in6 = IntVar()
in7 = IntVar()
in8 = IntVar()
in9 = IntVar()
#declare the main window global, along with the frames
global bw
global tframe
global bframe
bw= Tk()
tframe=Frame(bw)
tframe.pack(side=TOP)
bframe=Frame(bw)
bframe.pack(side=BOTTOM)
bw.title('THE MUSIC CLUB - Login')
bw.geometry("400x300+530+200")
member= Button(tframe, text = 'TMC Member', command=lambda:login())
member.grid(row=14,column='10', sticky = S)
coremember= Button(tframe, text = 'TMC Core Member', command=lambda:loginAdmin())
coremember.grid(row=15,column='10', sticky = S)
def create_checkboxes():
 bw4.deiconify()
 #global in1,in2,in3,in4,in5,in6,in7,in8,in9
 drums=Checkbutton(bw4, text='Drums,', variable=in1,onvalue=1, 
offvalue=0,command=get_value1)
 drums.grid(row=1, sticky=S)
 electric=Checkbutton(bw4, text='Electric,', variable=in2,onvalue=1, 
offvalue=0,command=get_value2)
 electric.grid(row=2, sticky=S)
 acoustic=Checkbutton(bw4, text='Acoustic,', variable=in3,onvalue=1, 
offvalue=0,command=get_value3)
 acoustic.grid(row=3, sticky=S)
 bass=Checkbutton(bw4, text='Bass,', variable=in4,onvalue=1, offvalue=0, 
command=get_value4)
 bass.grid(row=4, sticky=S)
 cajon=Checkbutton(bw4, text='Cajon,', variable=in5,onvalue=1, offvalue=0, 
command=get_value5)
 cajon.grid(row=5, sticky=S)
 tabla=Checkbutton(bw4, text='Tabla,', variable=in6,onvalue=1, 
offvalue=0,command=get_value6)
 tabla.grid(row=6, sticky=S)
 mic=Checkbutton(bw4, text='Microphone,', variable=in7,onvalue=1, offvalue=0, 
command=get_value7)
 mic.grid(row=7, sticky=S)
 amps=Checkbutton(bw4, text='Amps,', variable=in8,onvalue=1, 
offvalue=0,command=get_value8)
 amps.grid(row=8, sticky=S)
 keyboard=Checkbutton(bw4, text='Keyboard,', variable=in9,onvalue=1, 
offvalue=0,command=get_value9)
 keyboard.grid(row=9, sticky=S)
 submit=Button(bw4, text='Submit', command=lambda: insert_instruments_used())
 submit.grid(row=10, sticky=S)
 done1=Button(bw4, text='Done', command=lambda: closewindow4())
 done1.grid(row=11, sticky=S)
 
def create_checkboxes_ADMIN():
 bw4.deiconify()
 #global in1,in2,in3,in4,in5,in6,in7,in8,in9
 drums=Checkbutton(bw4, text='Drums,', variable=in1,onvalue=1, 
offvalue=0,command=get_value1)
 drums.grid(row=1, sticky=S)
 electric=Checkbutton(bw4, text='Electric,', variable=in2,onvalue=1, 
offvalue=0,command=get_value2)
 electric.grid(row=2, sticky=S)
 acoustic=Checkbutton(bw4, text='Acoustic,', variable=in3,onvalue=1, 
offvalue=0,command=get_value3)
 acoustic.grid(row=3, sticky=S)
 bass=Checkbutton(bw4, text='Bass,', variable=in4,onvalue=1, offvalue=0, 
command=get_value4)
 bass.grid(row=4, sticky=S)
 cajon=Checkbutton(bw4, text='Cajon,', variable=in5,onvalue=1, offvalue=0, 
command=get_value5)
 cajon.grid(row=5, sticky=S)
 tabla=Checkbutton(bw4, text='Tabla,', variable=in6,onvalue=1, 
offvalue=0,command=get_value6)
 tabla.grid(row=6, sticky=S)
 mic=Checkbutton(bw4, text='Microphone,', variable=in7,onvalue=1, offvalue=0, 
command=get_value7)
 mic.grid(row=7, sticky=S)
 amps=Checkbutton(bw4, text='Amps,', variable=in8,onvalue=1, 
offvalue=0,command=get_value8)
 amps.grid(row=8, sticky=S)
 keyboard=Checkbutton(bw4, text='Keyboard,', variable=in9,onvalue=1, 
offvalue=0,command=get_value9)
 keyboard.grid(row=9, sticky=S)
 submit=Button(bw4, text='Submit', command=lambda: 
insert_instruments_used_ADMIN())
 submit.grid(row=10, sticky=S)
 done1=Button(bw4, text='Done', command=lambda: closewindow4())
 done1.grid(row=11, sticky=S)
 
def get_value1():
 global v1
 v1=in1.get()
 i_id=1
 if v1==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v1, i_id))
 mydb.commit()
 
def get_value2(): 
 global v2
 v2=in2.get()
 i_id=2
 if v2==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v2, i_id))
 mydb.commit()
def get_value3():
 global v3
 v3=in3.get()
 i_id=3
 if v3==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v3, i_id))
 mydb.commit()
def get_value4():
 global v4
 v4=in4.get()
 i_id=4
 if v4==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v4, i_id))
 mydb.commit()
def get_value5():
 global v5
 v5=in5.get()
 i_id=5
 if v5==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v5, i_id))
 mydb.commit()
 
def get_value6():
 global v6
 v6=in6.get()
 i_id=6
 if v6==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v6, i_id))
 mydb.commit()
def get_value7():
 global v7
 v7=in7.get()
 i_id=7
 if v7==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v7, i_id))
 mydb.commit()
def get_value8():
 global v8
 v8=in8.get()
 i_id=8
 if v8==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v8, i_id))
 mydb.commit()
def get_value9():
 global v9
 v9=in9.get()
 i_id=9
 if v9==1:
 mycursor=mydb.cursor()
 mycursor.execute("""update equipment set inst_checked = %s where 
inst_id=%s""", (v9, i_id))
 mydb.commit()
 
#login for tmc members
def login(): 
 global dob
 dob=timeofbooking()
 fname = Label(bframe, text = 'First name')
 lname = Label(bframe, text = 'Last name' )
reg_no = Label(bframe, text = 'Registration Number')
 global entry1
 global entry2
 global entry3
 entry1 = Entry(bframe)
 entry2 = Entry(bframe)
 entry3 = Entry(bframe)
 fname.grid(padx=10,pady=10,row=10, column='9', sticky = S)
 lname.grid(padx=10,pady=10, row=11,column='9', sticky = S)
 reg_no.grid(padx=10,pady=10,row=12,column='9', sticky = S)
 entry1.grid(row=10, column = '10')
 entry2.grid(row=11, column = '10')
 entry3.grid(row=12, column = '10') 
 login= Button(bframe, text = 'Login', command=lambda:verify_details())
 login.grid(row=14,column='10', sticky = S)
 logout=Button(bframe, text='Logout', command=lambda: closeallwindows())
 logout.grid(row=15,column='10', sticky = S)
 #login for admins
def loginAdmin():
 global dob
 dob=timeofbooking()
 fname = Label(bframe, text = 'First name')
 lname = Label(bframe, text = 'Last name' )
 reg_no = Label(bframe, text = 'Registration Number')
 global entrycmem1
 global entrycmem2
 global entrycmem3
 entrycmem1 = Entry(bframe)
 entrycmem2 = Entry(bframe)
 entrycmem3 = Entry(bframe)
 fname.grid(padx=10,pady=10,row=10, column='9', sticky = S)
 lname.grid(padx=10,pady=10, row=11,column='9', sticky = S)
 reg_no.grid(padx=10,pady=10,row=12,column='9', sticky = S)
 entrycmem1.grid(row=10, column = '10')
 entrycmem2.grid(row=11, column = '10')
 entrycmem3.grid(row=12, column = '10') 
 login= Button(bframe, text = 'Login', command=lambda:verify_admin())
 login.grid(row=14,column='10', sticky = S)
 logout=Button(bframe, text='Logout', command=lambda: closeallwindowsadmin())
 logout.grid(row=15,column='10', sticky = S)
#verify details for tmc members
def verify_details():
 mycursor = mydb.cursor()
 mycursor.execute("""use tmcjamroom""")
 mycursor.execute("""SELECT fname,lname,reg_no FROM members""")
 sqlfinalentry = mycursor.fetchall()
 yo=0
 try:
 global f
 global l
 f=entry1.get()
 l=entry2.get() 
 except ValueError:
 tkinter.messagebox.showinfo('Error','Invalid input.')
 try:
 global r
 global rn
 r=entry3.get()
 rn=int(r)
 except:
 tkinter.messagebox.showinfo('Error','Please enter a number.')
 finalentry = f,l,rn
 tup=tuple(sqlfinalentry)
 for x in tup:
 if (finalentry==x):
 yo=1
 welcome()
 homepage() 
 if yo==0:
 error()
#verify details for admin
def verify_admin():
 mycursor = mydb.cursor()
 mycursor.execute("""use tmcjamroom""")
 mycursor.execute("""SELECT fname,lname,reg_no FROM admin""")
 sqlfinaladminentry = mycursor.fetchall()
 yo=0
 try:
 f=entrycmem1.get()
 l=entrycmem2.get() 
 r=entrycmem3.get() 
 except ValueError:
 tkinter.messagebox.showinfo('Error','Invalid input.')
 finalentry = f,l,r
 admintup=tuple(sqlfinaladminentry)
 for x in admintup:
 if (finalentry==x):
 yo=1
 welcome()
 homepageAdmin() 
 if yo==0:
 accessdenied()
#homepage for TMC members
def homepage():
 bw2.deiconify()
 #global bw2
 global topframe
 global bottomframe
 global leftframe
 #bw2=Tk()
 bw2.title('Home')
 bw2.geometry("400x300+530+200")
 topframe=Frame(bw2)
 topframe.pack(side=TOP)
 bottomframe=Frame(bw2)
 bottomframe.pack(side=BOTTOM)
 leftframe=Frame(bw2)
 leftframe.pack(side=LEFT)
 bslot=Button(topframe, text='Book a Slot', command=lambda: book_slot())
 bslot.grid(row=10, sticky = S)
 vsched=Button(topframe, text='View Current Schedule', command=lambda: 
view_schedule())
 vsched.grid(row=11, sticky = S)
 cancel=Button(topframe, text='Cancel your Slot', command=lambda: deleteSlot())
 cancel.grid(row=12, sticky = S)
 logout=Button(topframe, text='Logout', command=lambda: closewindow1())
 logout.grid(row=13, sticky = S)
#homepage for Admins
def homepageAdmin():
 bw3.deiconify()
 #global bw3
 global TOPframe
 global BOTTOMframe
 #bw3=Tk()
 bw3.title('Admin-Home')
 bw3.geometry("400x300+530+200")
 TOPframe=Frame(bw3)
 TOPframe.pack(side=TOP)
 BOTTOMframe=Frame(bw3)
 BOTTOMframe.pack(side=BOTTOM)
 bslot=Button(TOPframe, text='Book a Slot', command=lambda: Admin_book())
 bslot.grid(row=10, sticky = S)
 vsched=Button(TOPframe, text='View Current Schedule', command=lambda: 
view_schedule())
 vsched.grid(row=11, sticky = S)
 viewintsr=Button(TOPframe, text='View Equipment Used', command=lambda: 
view_instruments_used())
 viewintsr.grid(row=12, sticky= S)
 mem=Button(TOPframe, text='View Members', command=lambda: view_members())
 mem.grid(row=13, sticky = S)
 cancel=Button(TOPframe, text='Cancel your Slot', command=lambda: 
deleteAdminSlot())
 cancel.grid(row=14, sticky = S)
 logout=Button(TOPframe, text='Logout', command=lambda: closeallwindowsadmin())
 logout.grid(row=15, sticky = S)
#book a slot for a TMC member
def book_slot():
stime=Label(bottomframe, text='Slot Start Time')
etime=Label(bottomframe, text='Slot End Time')
stime.grid(row=1, column =9, sticky = N)
etime.grid(row=2, column=9, sticky = N)
global entry4
global entry5
entry4 = Entry(bottomframe)
entry5 = Entry(bottomframe)
entry4.grid(row=1, column = 10)
entry5.grid(row=2, column = 10)
book = Button(bottomframe, text = 'Confirm', command=lambda: confirmBook())
book.grid(row=3,column=10, sticky = N)
Done = Button(bottomframe, text ='Done', command=lambda: 
closeslotbookingframe())
Done.grid(row=4, column=10, sticky = N)
def confirmBook():
 global mom
 global STARTTIME
 global ENDTIME
 STARTTIME=entry4.get()
 ENDTIME=entry5.get()
 mom = STARTTIME, ENDTIME
 actualwork()
def get_entry4():
 global STARTTIME
 global ENDTIME
 STARTTIME=entry4.get()
 ENDTIME=entry5.get()
 
def check_existing_slot():
 global stat1
 global check
 global smth1
 global smth2
 global firstcheck
 global STARTTIME
 global ENDTIME
 stat1='Booked'
 mycursor=mydb.cursor()
 mycursor.execute("""SELECT firstname,lastname FROM schedule""")
 full_name=mycursor.fetchall()
 mycursor.execute("""SELECT start_time,end_time,status FROM schedule""")
 timings=mycursor.fetchall()
 mycursor.execute("""SELECT day from schedule""")
 day=mycursor.fetchall()
 daytup=tuple(day)
 #checking if program is running on current day; if not, clear entries
 for i in daytup:
 if i[0] == 'null' :
 break
 for i in daytup:
 if i[0] != dob and i[0] != 'null': 
 mycursor.execute("""DELETE from schedule where 1""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('1','5','6','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('2','6','7','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('3','7','8','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('4','8','9','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('5','9','10','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('6','10','11','Available','null')""")
 mycursor.execute("""delete from viewins where 1""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(1,'5','6')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(2,'6','7')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(3,'7','8')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(4,'8','9')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(5,'9','10')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(6,'10','11')""")
 mydb.commit()
 firstcheck=1
 break
 else:
 firstcheck=2
 pass
 if firstcheck==1:
 smth1=0
 smth2=0
 elif firstcheck==2:
 f=entry1.get()
 l=entry2.get()
 fullname=tuple(full_name)
 inputfullname=f,l
 tim=tuple(timings)
 inputtimings=STARTTIME,ENDTIME,stat1
 smth1=0
 smth2=0
 for y in fullname:
 if inputfullname==y:
 smth1=1
 for b in tim:
 if inputtimings==b:
 smth2=2
 check=smth1+smth2
 if check==1:
 tkinter.messagebox.showinfo('Error','You have already booked a slot.')
 elif check==2:
 tkinter.messagebox.showinfo('Error','This slot has been booked. Sorry!')
 elif check==3:
 tkinter.messagebox.showinfo('Error','You have already booked a slot.')
 else:
 pass
 return check
def actualwork():
flag=check_existing_slot()
if flag==0:
 f=entry1.get()
 l=entry2.get()
 mycursor= mydb.cursor()
 mycursor.execute("""use tmcjamroom""")
 mycursor.execute("""SELECT start_time, end_time FROM slots""")
 slottup=mycursor.fetchall()
 slot=tuple(slottup)
 for x in slot:
 if mom==x:
 mycursor.execute("""UPDATE schedule SET firstname=%s, lastname=%s, 
reg_no=%s, day=%s WHERE start_time=%s""" , (f,l,rn,dob,(entry4.get())))
 mycursor.execute("""UPDATE schedule SET status=%s WHERE start_time=%s """
, (stat1, (entry4.get())))
 mydb.commit()
 tkinter.messagebox.showinfo('Equipments Used','Please enter the equipment 
you will use during your jam slot.')
 create_checkboxes()
elif flag==1 or flag==2:
 pass
#delete a slot (for TMC members)
def deleteSlot():
 mycursor=mydb.cursor()
 r=entry3.get()
 regn=int(r)
 afterdelstat='Available'
 afterdelday='null'
 mycursor.execute("""update schedule set firstname = null, lastname = null, 
reg_no=null, status=%s, day=%s where reg_no = %s""", 
(afterdelstat,afterdelday,regn))
 #mycursor.execute("""update viewins set firstname = null, reg_no=null, 
inst_used = null where reg_no = %s""", (regn))
 mydb.commit()
 tkinter.messagebox.showinfo('Success!','Your slot has been cancelled.')
 
 
def deleteAdminSlot():
 mycursor=mydb.cursor()
 r=entrycmem3.get()
 regnu=int(r)
 afterdelstat='Available'
 afterdelday='null'
 mycursor.execute("""update schedule set firstname = null, lastname = null, 
reg_no=null, status=%s, day=%s where reg_no = %s""", 
(afterdelstat,afterdelday,regnu))
 #mycursor.execute("""update viewins set firstname = null, reg_no=null, 
inst_used = null where reg_no = %s""", (regnu))
 mydb.commit()
 tkinter.messagebox.showinfo('Success!','Your slot has been cancelled.')
 
#book a slot for an Admin
def Admin_book():
stime=Label(BOTTOMframe, text='Slot Start Time')
etime=Label(BOTTOMframe, text='Slot End Time')
stime.grid(row=1, column =9, sticky = N)
etime.grid(row=2, column=9, sticky = N)
global entry4
global entry5
entry4 = Entry(BOTTOMframe)
entry5 = Entry(BOTTOMframe)
entry4.grid(row=1, column = 10)
entry5.grid(row=2, column = 10)
book = Button(BOTTOMframe, text = 'Confirm', command=lambda: ADMINconfirmBook())
book.grid(row=3,column=10, sticky = N)
Done = Button(BOTTOMframe, text ='Done', command=lambda: 
closeadminslotbookingframe())
Done.grid(row=4, column=10, sticky = N)
def ADMINconfirmBook():
 global mom
 global STARTTIME
 global ENDTIME
 STARTTIME=entry4.get()
 ENDTIME=entry5.get()
 mom = STARTTIME,ENDTIME
 timeofbooking()
 ADMINactualwork()
def admin_check_existing_slot():
 global stat1
 global check
 global smth1
 global smth2
 global firstcheck
 stat1='Booked'
 mycursor=mydb.cursor()
 mycursor.execute("""SELECT firstname,lastname FROM schedule""")
 full_name=mycursor.fetchall()
 mycursor.execute("""SELECT start_time,end_time,status FROM schedule""")
 timings=mycursor.fetchall()
 mycursor.execute("""SELECT day from schedule""")
 day=mycursor.fetchall()
 daytup=tuple(day)
 #checking if program is running on current day; if not, clear entries
 for i in daytup:
 if i[0] == 'null' :
 break
 for i in daytup:
 if i[0] != dob and i[0] != 'null': 
 mycursor.execute("""DELETE from schedule where 1""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('1','5','6','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('2','6','7','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('3','7','8','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('4','8','9','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('5','9','10','Available','null')""")
 mycursor.execute("""insert into schedule(slot_id,start_time, end_time, 
status,day)values('6','10','11','Available','null')""")
 mycursor.execute("""delete from viewins where 1""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(1,'5','6')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(2,'6','7')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(3,'7','8')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(4,'8','9')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(5,'9','10')""")
 mycursor.execute("""insert into viewins(slot_id, start_time, 
end_time)values(6,'10','11')""")
 mydb.commit()
 firstcheck=1
 break
 else:
 firstcheck=2
 pass
 if firstcheck==1:
 smth1=0
 smth2=0
 elif firstcheck==2:
 f=entrycmem1.get()
 l=entrycmem2.get()
 fullname=tuple(full_name)
 inputfullname=f,l
 tim=tuple(timings)
 inputtimings=STARTTIME,ENDTIME,stat1
 smth1=0
 smth2=0
 for y in fullname:
 if inputfullname==y:
 smth1=1
 for b in tim:
 if inputtimings==b:
 smth2=2
 check=smth1+smth2
 if check==1:
 tkinter.messagebox.showinfo('Error','You have already booked a slot.')
 elif check==2:
 tkinter.messagebox.showinfo('Error','This slot has been booked. Sorry!')
 elif check==3:
 tkinter.messagebox.showinfo('Error','You have already booked a slot.')
 else:
 pass
 return check
def ADMINactualwork():
flag=admin_check_existing_slot()
if flag==0:
 global f
 f=entrycmem1.get()
 l=entrycmem2.get()
 r=entrycmem3.get()
 rn=int(r)
 mycursor = mydb.cursor()
 mycursor.execute("""use tmcjamroom""")
 mycursor.execute("""SELECT start_time, end_time FROM slots""")
 slottup=mycursor.fetchall()
 slot=tuple(slottup)
 for x in slot:
 if mom==x:
 mycursor.execute("""UPDATE schedule SET firstname=%s, lastname=%s, 
reg_no=%s, day=%s WHERE start_time=%s""" , (f,l,rn,dob,STARTTIME))
 mycursor.execute("""UPDATE schedule SET status=%s WHERE start_time=%s """
, (stat1,STARTTIME))
 mydb.commit()
 tkinter.messagebox.showinfo('Equipments Used','Please enter the equipment 
you will use during your jam slot.')
 create_checkboxes_ADMIN()
elif flag==1 or flag==2:
 pass
 
#insert the instruments used into the viewins table
def insert_instruments_used():
f=entry1.get()
r=entry3.get()
regn=int(r)
mycursor=mydb.cursor()
mycursor.execute("""select inst_name from equipment where inst_checked = 1 """) 
instr=mycursor.fetchall()
ins=str(instr)
mycursor.execute("""UPDATE viewins SET firstname=%s, reg_no=%s, inst_used = %s
WHERE start_time = %s""", (f,regn,ins, STARTTIME))
booked()
clear_equipment_table()
mydb.commit()
def insert_instruments_used_ADMIN():
f=entrycmem1.get()
r=entrycmem3.get()
regnu=int(r)
mycursor=mydb.cursor()
mycursor.execute("""select inst_name from equipment where inst_checked = 1 """) 
instr=mycursor.fetchall()
ins=str(instr)
mycursor.execute("""UPDATE viewins SET firstname=%s, reg_no=%s, inst_used = %s
WHERE start_time = %s""", (f,regnu,ins,STARTTIME))
booked()
clear_equipment_table()
mydb.commit()
#TMC Member will view schedule
def view_schedule():
 mycursor=mydb.cursor()
 mycursor.execute("""SELECT slot_id FROM schedule""")
 slotid=mycursor.fetchall()
 mycursor.execute("""SELECT firstname FROM schedule""")
 firstname=mycursor.fetchall()
 mycursor.execute("""SELECT lastname FROM schedule""")
 lastname=mycursor.fetchall()
 mycursor.execute("""SELECT start_time FROM schedule""")
 starttime=mycursor.fetchall()
 mycursor.execute("""SELECT end_time FROM schedule""")
 endtime=mycursor.fetchall()
 mycursor.execute("""SELECT status FROM schedule""")
 status=mycursor.fetchall()
 mycursor.execute("""SELECT day FROM schedule""")
 dayy=mycursor.fetchall()
 t = PrettyTable(['Slot ID','First Name', 'Last Name', 'Slot Start Time', 'Slot 
End Time', 'Status', 'Time of Booking'])
 
t.add_row([slotid[0],firstname[0],lastname[0],starttime[0],endtime[0],status[0], 
dayy[0]])
 print(t)
 
t.add_row([slotid[1],firstname[1],lastname[1],starttime[1],endtime[1],status[1],d
ayy[1]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 
t.add_row([slotid[2],firstname[2],lastname[2],starttime[2],endtime[2],status[2], 
dayy[2]])
 print( "\n".join(t.get_string().splitlines()[-2:]) ) 
 
t.add_row([slotid[3],firstname[3],lastname[3],starttime[3],endtime[3],status[3], 
dayy[3]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 
t.add_row([slotid[4],firstname[4],lastname[4],starttime[4],endtime[4],status[4], 
dayy[4]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 
t.add_row([slotid[5],firstname[5],lastname[5],starttime[5],endtime[5],status[5], 
dayy[5]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 
def view_members():
 mycursor=mydb.cursor()
 mycursor.execute("""SELECT reg_no FROM members""")
 reg=mycursor.fetchall()
 mycursor.execute("""SELECT fname FROM members""")
 firstname=mycursor.fetchall()
 mycursor.execute("""SELECT lname FROM members""")
 lastname=mycursor.fetchall()
 mycursor.execute("""SELECT field FROM members""")
 field=mycursor.fetchall()
 mycursor.execute("""SELECT residence FROM members""")
 residence=mycursor.fetchall()
 mycursor.execute("""SELECT sex FROM members""")
 sex=mycursor.fetchall()
 t = PrettyTable(['Registration Number','First Name', 'Last Name', 'Field', 
'Residence', 'Sex'])
 t.add_row([reg[0],firstname[0],lastname[0],field[0],residence[0],sex[0]])
 print(t)
 t.add_row([reg[1],firstname[1],lastname[1],field[1],residence[1],sex[1]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[2],firstname[2],lastname[2],field[2],residence[2],sex[2]])
 print( "\n".join(t.get_string().splitlines()[-2:]) ) 
 t.add_row([reg[3],firstname[3],lastname[3],field[3],residence[3],sex[3]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[4],firstname[4],lastname[4],field[4],residence[4],sex[4]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[5],firstname[5],lastname[5],field[5],residence[5],sex[5]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[6],firstname[6],lastname[6],field[6],residence[6],sex[6]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[7],firstname[7],lastname[7],field[7],residence[7],sex[7]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[8],firstname[8],lastname[8],field[8],residence[8],sex[8]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[9],firstname[9],lastname[9],field[9],residence[9],sex[9]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([reg[10],firstname[10],lastname[10],field[10],residence[10],sex[10]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
#view the instruments inserted 
def view_instruments_used():
 mycursor=mydb.cursor()
 mycursor.execute("""SELECT inst_used FROM viewins""")
 instruments=mycursor.fetchall()
 mycursor.execute("""SELECT slot_id FROM viewins""")
 slotid=mycursor.fetchall()
 mycursor.execute("""SELECT firstname FROM viewins""")
 firstname=mycursor.fetchall()
 mycursor.execute("""SELECT start_time FROM viewins""")
 starttime=mycursor.fetchall()
 mycursor.execute("""SELECT end_time FROM viewins""")
 endtime=mycursor.fetchall()
 t = PrettyTable(['Slot ID','First Name','Slot Start Time', 'Slot End Time', 
'Instruments Used'])
 t.add_row([slotid[0],firstname[0],starttime[0],endtime[0], instruments[0]])
 print(t)
 t.add_row([slotid[1],firstname[1],starttime[1],endtime[1], instruments[1]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([slotid[2],firstname[2],starttime[2],endtime[2], instruments[2]])
 print( "\n".join(t.get_string().splitlines()[-2:]) ) 
 t.add_row([slotid[3],firstname[3],starttime[3],endtime[3],instruments[3]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([slotid[4],firstname[4],starttime[4],endtime[4],instruments[4]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 t.add_row([slotid[5],firstname[5],starttime[5],endtime[5], instruments[5]])
 print( "\n".join(t.get_string().splitlines()[-2:]) )
 
def clear_equipment_table():
 mycursor=mydb.cursor()
 mycursor.execute("""delete from equipment where 1""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(1,'Drums')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(2,'Acoustic Guitar')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(3,'Electric Guitar')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) values(4,'Bass 
Guitar')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(5,'Cajon')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(6,'Tabla')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(7,'Amps')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(8,'Microphone')""")
 mycursor.execute("""insert into equipment(inst_id, inst_name) 
values(9,'Keyboard')""")
 mydb.commit()
#close windows 
def closewindow1():
 bw.destroy()
def closeallwindows():
 bw2.destroy()
 bw.destroy()
 
def closeallwindowsadmin():
 bw3.destroy()
 bw.destroy()
def closeslotbookingframe():
 bottomframe.pack_forget()
def closeadminslotbookingframe():
 BOTTOMframe.pack_forget()
def closewindow2():
 bw2.destroy()
def closewindow4():
 bw4.destroy()
#misc functions
def timeofbooking():
now_var = datetime.datetime.now()
global dayofbooking
dayofbooking = now_var.strftime("%A")
return dayofbooking
def booked():
 tkinter.messagebox.showinfo('Success','Your slot has been booked. Thank you!')
def accessdenied():
 tkinter.messagebox.showinfo('Caution','Access denied! Please enter the valid 
admin credentials.')
def welcome():
 tkinter.messagebox.showinfo('Welcome','You have successfully logged in.')
def error():
 tkinter.messagebox.showinfo('Error','Please enter the correct credentials.')
bw.mainloop()
