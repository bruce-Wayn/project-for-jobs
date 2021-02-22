import sqlite3
from tkinter import *
from tkinter import messagebox as mb
from datetime import date
# creating root for gui
root = Tk()
root.title('Gate Pass Authorization')
# creating cursor for DB
conn = sqlite3.connect('master.db')
cur = conn.cursor()

company = Label(root, text='Company: ').grid(row=0, column=0)
entry1 = Entry(root, width= 30, bg='orange', borderwidth=5)
entry1.grid(row=0, column=1)
entry1.insert(0, 'No Input')
def comprecords():
    cur.execute("SELECT count(*) FROM mastercom")
    count = cur.fetchone()[0]
    companylist = []
    compverify = 0
    cur.execute('''SELECT name FROM mastercom ORDER BY id''')
    for n in range(count):
        name = cur.fetchone()[0]
        companylist.append(name)
    if entry1.get().lower() in companylist:
        compverify = 1
        print('Found!')
        mb.showinfo('Found one!', 'Verified')
    else:
        compverify = 2
        mb.showerror('ERROR!', 'Sorry no company in database found')
    print(companylist)
buttonA = Button(root, text='check records', width=1, padx=50, borderwidth=0.5, bg='white', fg='blue', command=comprecords).grid(row=0, column=2)

Date = Label(root, text='Date: ').grid(row=0, column=3)
today = date.today()
dateval= Label(root, text=today).grid(row=0, column=4)

vehno = Label(root, text='Vehicle number: ').grid(row=0, column=5)
entry3 = Entry(root, width= 30, bg='orange', borderwidth=5)
entry3.grid(row=0, column=6)
entry3.insert(0, 'No input')

time = Label(root, text='Time: ').grid(row=1, column=0)
entry4 = Entry(root, width=30, bg='orange', borderwidth=5)
entry4.grid(row=1, column=1)
entry4.insert(0, 'No input')

con_person = Label(root, text='Contact Person: ').grid(row=1, column=2)
entry5 = Entry(root, width=30, bg='orange', borderwidth=5)
entry5.grid(row=1, column=3)
entry5.insert(0, 'No input')

item = Label(root, text='Item: ').grid(row=2, column=0)
entry6 = Entry(root, width=30, bg='orange', borderwidth=5)
entry6.grid(row=3, column=0)
entry6.insert(0, 'No input')
# using master to verify
class itemms():
    def itemrecords():
        cur.execute("SELECT count(*) FROM items WHERE mastercom_id=(?)",(entry1.get(),))
        count = cur.fetchone()[0]
        itemlist = []
        itemverify = 0
        cur.execute('SELECT name FROM items WHERE mastercom_id=(?)', (entry1.get(),))
        for n in range(count):
            name = cur.fetchone()[0]
            itemlist.append(name)

        if entry6.get() in itemlist:
            itemverify = 1
            cur.execute("SELECT qty FROM items WHERE name=(?)", (entry6.get(),))
            totqty = cur.fetchone()[0]
            mb.showinfo('Found one!', 'Verified'+'\nTotal quantity='+str(totqty))
        else:
            itemverify = 2
            mb.showerror('ERROR!', 'Sorry no company in database found')

        print(totqty)
    def cmd():
        cur.execute("SELECT count(*) FROM items WHERE mastercom_id=(?)", (entry1.get(),))
        count = cur.fetchone()[0]
        itemlist = []
        itemverify = 0
        cur.execute('SELECT name FROM items WHERE mastercom_id=(?)', (entry1.get(),))
        for n in range(count):
            name = cur.fetchone()[0]
            itemlist.append(name)

        if entry6.get() in itemlist:
            itemverify = 1
            cur.execute("SELECT qty FROM items WHERE name=(?)", (entry6.get(),))
            totqty = cur.fetchone()[0]
        else:
            itemverify = 2
        mb.showinfo('Found!', 'Verified' + '\nTotal quantity=' + str(totqty-int(entry7.get())))
        cur.execute("UPDATE items SET qty=(?) WHERE name=(?) AND mastercom_id=(?)",(totqty - int(entry7.get()), str(entry6.get()), str(entry1.get())))

        print(totqty)

    def staffrecords():
        stafflist = []
        staffverify = 0
        cur.execute("SELECT count(*) FROM master_staff")
        count = cur.fetchone()[0]
        cur.execute("SELECT name FROM master_staff ORDER BY id")
        for n in range(count):
            name = cur.fetchone()[0]
            stafflist.append(name)
        if entry10.get() in stafflist:
            staffverify = 1
            cur.execute("SELECT id FROM master_staff WHERE name=(?)", (entry10.get(),))
            mb.showinfo('Attended package', 'Verified')
        else:
            staffverify = 2
            mb.showerror('ERROR!', 'Sorry no staff in database found')
    def func():
        '''

        mastercomname = str(entry1.get())
        daatee = str(today)
        vehnoo = entry3.get()
        tiimee = str(entry4.get())
        conn_person = entry5.get()
        eitemid = entry6.get()
        eitemqty = entry7.get()
        eitemuom = entry8.get()
        remarkes = entry9.get()
        eitemtotqty = totqty
        print(totqty)
        chckdby = entry10.get()
        stateus = var.get()
        print(var.get())
        cur.execute("""INSERT INTO masterlog (mastercomname, date, vehno, time, contperson, item, rem_qty, uome, remarks, tot_qty, staff, status) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",(mastercomname, daatee, vehnoo, tiimee, conn_person, eitemid, eitemqty, eitemuom, remarkes, eitemtotqty, chckdby, stateus))
        '''
        #cur.execute("UPDATE items SET qty=(?) WHERE name=(?) AND mastercom_id=(?)",(int(totqty)-int(entry7.get()),str(entry6.get()),str(entry1.get())))
        mb.showinfo('coming soon', 'hello user this feature will soon be updated when out of bugs until then please wait! Thanks for staying with us.')

#print(entry1.get(), today, entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(),entry8.get(), entry9.get(), entry10.get(), var.get())

buttonB = Button(root, text='check records', width=1, padx=50, borderwidth=0.5, bg='white', fg='blue', command=itemms.itemrecords).grid(row=4, column=0)

qty = Label(root, text='Qty: ').grid(row=2, column=1)
entry7 = Entry(root, width=30, bg='orange', borderwidth=5)
entry7.grid(row=3, column=1)
entry7.insert(0, 'No input')

uom = Label(root, text='UOM: ').grid(row=2, column=2)
entry8 = Entry(root, width=30, bg='orange', borderwidth=5)
entry8.grid(row=3, column=2)
entry8.insert(0, 'No input')

remarks = Label(root, text='Remarks: ').grid(row=2, column=3)
entry9 = Entry(root, width=30, bg='orange', borderwidth=5)
entry9.grid(row=3, column=3)
entry9.insert(0, 'remark')

#cur.execute('CREATE TABLE master_log (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE  )')
totqty = Label(root, text='Total Qty: ').grid(row=5, column=0)
evaltotalqty = Button(root, text='see after updating', width=1, padx=50, borderwidth=0.5, bg='white', fg='blue', command=itemms.cmd).grid(row=5, column=1)

checkedby = Label(root, text='Checked by: ').grid(row=5, column=2)
entry10 = Entry(root, width=30, bg='orange', borderwidth=5)
entry10.grid(row=5, column=3)
entry10.insert(0, 'No input')
buttonChkd = Button(root, text='attendance', width=1, padx=50, borderwidth=0.5, bg='white', fg='blue', command=itemms.staffrecords).grid(row=6, column=3)

status = Label(root, text='Status:').grid(row=6, column=0)
options = {'1 not selected':'Not selected','2 returnable':'Returnable','3 non returnable':'Non Returnable','4 personal belonging':'Personal Belonging', '5 others':'Others'}
mainframe = Frame(root)
var = StringVar(root)
w = OptionMenu(root, var, *options)
w.grid(row=6, column=1)
var.set('1 not selected')

# definining function to seek out Company,Item,uom,Checked by fields and Link/fetch from Master

class finalexec():

    def warning():
        mb.showinfo('Under development', 'Sorry the module you request is under development, please stick with the developer for upcoming updates!')


# add if else for both these statements if any input is missing
upcomfeat = Label(root, text="Upcoming Features:-").grid(row=7,column=0)
button1 = Button(root, text='Save and update', width=1, padx=50, borderwidth=0.5, bg='#FFD700', fg='blue', command=itemms.func).grid(row=7, column=1)
button2 = Button(root, text='Save for print', width=1, padx=50, borderwidth=0.5, bg='Green', fg='White', command=finalexec.warning).grid(row=7, column=2)
print(var.get())

root.mainloop()
