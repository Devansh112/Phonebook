from Tkinter import *
from tkMessageBox import *
import sqlite3
con=sqlite3.Connection('phonebookdb')
cur=con.cursor()
cur.execute('create table if not exists phonebook ( Srno INTEGER ,Fname varchar(20),Mname varchar(20), Lname varchar(20), City varchar(20),Pin Number(10), Company varchar(20), Website varchar(50), Address varchar(50), DoB varchar(10), PRIMARY KEY (Srno))')
cur.execute("create table if not exists phonenumber ( Srno INTEGER ,ptype varchar(15), Pno varchar(10), foreign key (Srno) references phonebook(Srno), primary key(pno,Srno))")
cur.execute("create table if not exists emailid ( Srno INTEGER ,Emailtype varchar(15), Emailid varchar(50), foreign key (Srno) references phonebook(Srno), primary key(Emailid,Srno))")
            

        #page1
root1=Tk()
root1.title('Introduction Window')
root1.geometry('455x250')
root1.configure(bg='aliceblue')
Label(root1,fg="red",text='Phonebook',font=('Arial',25,),bg='aliceblue').grid(row=0,column=3)
Label(root1,fg="blue",text='Python and Database Project',font=('Arial',20),bg='aliceblue').grid(row=2,column=3)
Label(root1,fg="purple",text='Developed By:Devansh Mishra(181B078)',font=('Arial',18),bg='aliceblue').grid(row=3,column=3)
Label(root1,fg="cyan",text='------------------------------------------------------',font=('Arial',18),bg='aliceblue').grid(row=4,column=3)
Label(root1,fg="violet",text='Kindly Make Mouse Movement to go Beyond this Page',font=('Arial',10),bg='aliceblue').grid(row=5,column=3)


def Close(e=1):
    root1.destroy()
root1.bind('<Motion>',Close)

root1.mainloop()


                    #page2
root2=Tk()
root2.title('PHONEBOOK')

photo=PhotoImage(file='PhonebookImage.gif')
root2.geometry('420x515')
labelPhoto=Label(root2,image=photo).grid(columnspan=2,row=0,column=1)



Label(root2,text='First Name-').grid(row=1,column=0)
entry1=Entry(root2)
entry1.grid(row=1,column=1)

Label(root2,text='Middle Name-').grid(row=2,column=0)
entry2=Entry(root2)
entry2.grid(row=2,column=1)

Label(root2,text='Last Name-').grid(row=3,column=0)
entry3=Entry(root2)
entry3.grid(row=3,column=1)

Label(root2,text='Company Name-').grid(row=4,column=0)
entry4=Entry(root2)
entry4.grid(row=4,column=1)

Label(root2,text='Address-').grid(row=5,column=0)
entry5=Entry(root2)
entry5.grid(row=5,column=1)

Label(root2,text='City-').grid(row=6,column=0)
entry6=Entry(root2)
entry6.grid(row=6,column=1)

Label(root2,text='Pin-').grid(row=7,column=0)
entry7=Entry(root2)
entry7.grid(row=7,column=1)

Label(root2,text='Website-').grid(row=8,column=0)
entry8=Entry(root2)
entry8.grid(row=8,column=1)

Label(root2,text='DOB-').grid(row=9,column=0)
entry9=Entry(root2)
entry9.grid(row=9,column=1)

Label(root2,text='Phone Type:').grid(row=10,column=0)
v1=IntVar()
Radiobutton(root2,text='Home',variable=v1,value=1).grid(row=10,column=1)
Radiobutton(root2,text='Office',variable=v1,value=2).grid(row=10,column=2)
Radiobutton(root2,text='Mobile',variable=v1,value=3).grid(row=10,column=3)
Label(root2,text='Phone Number').grid(row=11,column=0)
entry10=Entry(root2)
entry10.grid(row=11,column=1)

Label(root2,text='Email Type:').grid(row=12,column=0)
v2=IntVar()
Radiobutton(root2,text='Office',variable=v2,value=1).grid(row=12,column=1)
Radiobutton(root2,text='Personal',variable=v2,value=2).grid(row=12,column=2)
Label(root2,text='Email ID-').grid(row=13,column=0)
entry11=Entry(root2)
entry11.grid(row=13,column=1)

                   #button funcs
def delete():
    x=askyesno('Exit','Are you sure you want to exit?')
    if(x==True):
      root2.destroy()

def clear():
  
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry9.delete(0,END)
    entry10.delete(0,END)
    entry11.delete(0,END)
    showinfo('Success','All Records Clear')
def insert():
    
    if v1.get()==1:
        ptype='Home'
    elif v1.get()==2:
        ptype='Office'
    elif v1.get()==3:
        ptype='Mobile'
    else:
        ptype=''
    if v2.get()==1:
        emailtype='Personal'
    elif v2.get()==2:
        emailtype='Office'
    else:
        emailtype=''
    
    cur.execute('select count(*) from phonebook')
    sno1=cur.fetchall()[0][0]
    cur.execute('select max(Srno) from phonebook')
    try:
        sno2=cur.fetchall()[0][0]
    except:
        sno2=0
    if sno1>=sno2:
        x=sno1
    else:
        x=sno2
    data=(x,entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get(),entry8.get(),entry9.get())
    cur.execute('Insert into phonebook (Srno,Fname,MName,Lname,City,Pin,Company,Website,Address,DoB) values (?,?,?,?,?,?,?,?,?,?)',data)
    con.commit()
    no=(x,ptype,entry10.get())
    cur.execute("insert into phonenumber (Srno,ptype,pno) values (?,?,?)",no)
    con.commit()
    email=(x,emailtype,entry11.get())
    cur.execute("insert into emailid (Srno,Emailtype,Emailid) values (?,?,?)",email)
    con.commit()
        
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)
    entry8.delete(0,END)
    entry9.delete(0,END)
    entry10.delete(0,END)
    entry11.delete(0,END)



    showinfo('Saved','Recorded')

def search():
    root3=Tk()
    root3.title('Search Window')
    root3.geometry('550x700')
    Label(root3,text='Enter Name you want to search').grid(row=1,column=1)
    e=Entry(root3)
    e.grid(row=1,column=2)
    lb1=Listbox(root3)
    lb1.grid(row=2,column=2,ipadx=100,ipady=100)
    def find(event=1):
        lb1.delete(0,END)
        item=e.get()
        cur.execute('select * from phonebook where (fname like (?)) or (fname like (?)) or (fname like (?))',(str(item+"%"),str('%'+item+"%"),str("%"+item)))
        global details
        details=cur.fetchall()
        for i in range(len(details)):
            lb1.insert(END,details[i][1]+" "+details[i][2])
        def detail(eve=1):
            index=int(lb1.curselection()[0])
            lb2=Listbox(root3)
            lb2.grid(row=2,column=2,ipadx=100,ipady=100)
            lb2.insert(END,'First Name :'+str(details[index][1]))
            lb2.insert(END,'Middle Name :'+str(details[index][2]))
            lb2.insert(END,'Last Name :'+str(details[index][3]))
            lb2.insert(END,'Company Name :'+str(details[index][4]))
            lb2.insert(END,'Address :'+str(details[index][5]))
            lb2.insert(END,'City :'+str(details[index][6]))
            lb2.insert(END,'PIN :'+str(details[index][7]))
            lb2.insert(END,'Website :'+str(details[index][8]))
            lb2.insert(END,'DOB :'+str(details[index][9]))

            cur.execute('select * from phonenumber where srno=(?)',((str(details[index][0])),))
            global details1
            details1=cur.fetchall()
            
            lb2.insert(END,'PhoneType: '+str(details1[0][1]))
            lb2.insert(END,'Phone: '+str(details1[0][2]))

            cur.execute('select * from emailid where srno=(?)',((str(details[index][0])),))
            global details2
            details2=cur.fetchall()
            
            lb2.insert(END,'Email Type: '+str(details2[0][1]))
            lb2.insert(END,'EmailID: '+str(details2[0][2]))
            def delete2():
                if askyesno("Confirm","Are you sure?")==True:
                    cur.execute('delete from phonebook where srno=(?)',((str(details[index][0])),))
                    cur.execute('delete from phonenumber where srno=(?)',((str(details[index][0])),))
                    cur.execute('delete from Emailid where srno=(?)',((str(details[index][0])),))
                    con.commit()
                    root3.destroy()

            def update():
                if askyesno("Confirm","Are you sure?")==True:
                    cur.execute('delete from phonebook where srno=(?)',((str(details[index][0])),))
                    cur.execute('delete from phonenumber where srno=(?)',((str(details[index][0])),))
                    cur.execute('delete from Emailid where srno=(?)',((str(details[index][0])),))
                    con.commit()
                    entry1.insert(0,str(details[index][1]))
                    entry2.insert(0,str(details[index][2]))
                    entry3.insert(0,str(details[index][3]))
                    entry4.insert(0,str(details[index][4]))
                    entry5.insert(0,str(details[index][5]))
                    entry6.insert(0,str(details[index][6]))
                    entry7.insert(0,str(details[index][7]))
                    entry8.insert(0,str(details[index][8]))
                    entry9.insert(0,str(details[index][9]))
                    entry10.insert(0,str(details1[0][2]))
                    entry11.insert(0,str(details2[0][2]))
                    if str(details1[0][1])=='Home':
                        v1.set(1)
                    elif str(details1[0][1])=='Office':
                        v1.set(2)
                    elif str(details1[0][1])=='Mobile':
                        v1.set(3)
                    else:
                        v1.set(0)
                    if str(details2[0][1])=='Personal':
                        v2.set(1)
                    elif str(details2[0][1])=='Office':
                        v2.set(2)
                    else:
                        v2.set(0)
                    
                    root3.destroy()
                
            Button(root3,text='Update',command=update).grid(row=5,column=0)
            Button(root3,text='Delete Record',command=delete2).grid(row=5,column=2)
        lb1.bind("<Double-Button-1>",detail)
    root3.bind("<KeyPress>",find)



    def delete1():
        root3.destroy()
    Button(root3,text='Close',command=delete1).grid(row=5,column=1)   
Button(root2,text='Submit',command=insert).grid(row=14,column=0)   
Button(root2,text='Search',command=search).grid(row=14,column=2)
Button(root2,text='Close',command=delete).grid(row=14,column=3)
Button(root2,text='Clear All',command=clear).grid(row=14,column=4)
root2.mainloop()
