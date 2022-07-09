from tkinter import *
import mysql.connector as db
from datetime import datetime as dt
conn=db.connect(user='root',password='Satwik@2003',host='localhost',database='satwik')
cursor=conn.cursor()
root=Tk()
a=StringVar()
Label(root,text='enter name').grid(row=0,column=0)
b=Entry(root,textvariable=a).grid(row=0,column=1)
Label(root,text='enter amount').grid(row=1,column=0)
c=StringVar()
Entry(root,textvariable=c).grid(row=1,column=1)
Label(root,text='enter account name').grid(row=2,column=0)
d=StringVar()
Entry(root,textvariable=d).grid(row=2,column=1)
def credit():
    try:
        now=str(dt.now())
        stmt1='select amount from accounts'
        data=()
        cursor.execute(stmt1)
        s=0
        for (amount) in cursor:
            s=amount
        stmt="insert into accounts(name,amount,tdate) values (%s,%s,%s)"
        data=(a.get(),str(int(c.get())+int(s[0])),now)
        cursor.execute(stmt,data)
        cursor.execute('commit;')
    except db.Error as e:
        Label(root,text=e).grid(row=0,column=5)
def debit():
    try:
        now=str(dt.now())
        stmt1='select amount from accounts'
        data=()
        cursor.execute(stmt1)
        s=0
        for (amount) in cursor:
            s=amount
        stmt="insert into accounts(name,amount,tdate) values (%s,%s,%s)"
        data=(a.get(),str(int(s[0])-int(c.get())),now)
        cursor.execute(stmt,data)
        cursor.execute('commit;')
    except db.Error as e:
        Label(root,text=e).grid(row=0,column=5)
def getInfo():
    try:
        stmt="select * from accounts"
        cursor.execute(stmt)
        i=5
        Label(root,text="id\tname\tamount\ttdate").grid(row=4,column=0)
        for(id,name,amount,tdate) in cursor:
            Label(root,text=str(id)+'\t'+name+'\t'+str(amount)+'\t'+tdate).grid(row=i,column=0)
            i+=1
    except db.Error as e:
        Label(root,text='Error').grid(row=0,column=5)
Button(root,text="credit",command=credit).grid(row=3,column=0)
Button(root,text="Debit",command=debit).grid(row=3,column=1)
Button(root,text="get details",command=getInfo).grid(row=3,column=2)

