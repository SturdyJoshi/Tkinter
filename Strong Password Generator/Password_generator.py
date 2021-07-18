from tkinter import *
from tkinter import messagebox
import _sqlite3
from tkinter import ttk
db = _sqlite3.connect("password_generator.db")
cr = db.cursor()
root = Tk()

root.geometry("400x400")
root.resizable(0,0)
root.title("password generator")
root.configure(background= "#091e42")

def home():
    f1 = Frame(bg = "#091e42")
    f1.place(x=0, y=0, height=400, width=400)
    # f1.configure(background="silver")
    b1 = Button(f1, text="NEW USER", font=("Arial",), command=new_user, bg = "#091e42", fg= "white")
    b1.place(x=120, y=130, height=30, width=150)
    b2 = Button(f1, text="EXISTING USER", font=("Arial",), command=existing_user, bg = "#091e42", fg= "white")
    b2.place(x=120, y=200, height=30, width=150)


def new_user():
    en1, en2, en3 = StringVar(), StringVar(), StringVar()
    f2= Frame(bg = "#091e42")
    # f2.configure(background="silver")
    f2.place(x=0, y=0, height= 400, width= 400)

    l1 = Label(f2, text= "Enter name", font=("Arial", ), bg = "#091e42", fg= "white")
    l1.place(x= 80, y= 100)
    e1 = Entry(f2, font= ("Arial",), textvariable= en1)
    e1.place(x= 220, y= 100, height= 30, width= 150)

    l2 = Label(f2, text="Enter password", font=("Arial",), bg = "#091e42", fg= "white")
    l2.place(x= 80, y= 150)
    e2 = Entry(f2, font=("Arial",), textvariable= en2)
    e2.place(x= 220, y= 150, height= 30, width= 150)

    l3 = Label(f2, text="Confirm password", font=("Arial",), bg = "#091e42", fg= "white")
    l3.place(x=80, y=200)
    e3 = Entry(f2, font=("Arial",), textvariable= en3)
    e3.place(x=220, y=200, height=30, width=150)

    def regis():
        # print("hello neeraj")

        x, y, z = en1.get(), en2.get(), en3.get()
        cr.execute("insert into registration values('"+x+"', '"+y+"', '"+z+"')")  # var is not in the form of integer
        en1.set("")
        en2.set("")
        en3.set("")
        db.commit()
        # db.close()
        messagebox.showinfo('Title', 'Registration sucessful').title("Sucess")
    b_new_user = Button(f2, text= "Create", bg = "#091e42", fg= "white", command = regis)
    b_new_user.place(x=220, y=240, height= 30, width= 50)

    b_back = Button(f2, text="<--", command= home, bg = "#091e42", fg= "white")
    b_back.place(x=5, y=2, width=50, height=25)

def existing_user():
    en4, en5 = StringVar(), StringVar()
    f3 = Frame(bg = "#091e42")
    # f3.configure(background="silver")
    f3.place(x=0, y=0, height=400, width=400)

    l4 = Label(f3, text="Enter name", font=("Arial",), bg = "#091e42", fg= "white")
    l4.place(x=80, y=100, height=25)
    e4 = Entry(f3, font=("Arial",), textvariable= en4)
    e4.place(x=220, y=100, height=30, width=150)

    l5 = Label(f3, text="Enter password", font=("Arial",), bg = "#091e42", fg= "white")
    l5.place(x=80, y=150, height=25)
    e5 = Entry(f3, font=("Arial",), show="*", textvariable= en5)
    e5.place(x=220, y=150, height=30, width=150)
    # def show_data(n):
        # print("inside show_data")
        # r =cr.execute("select ACCOUNT, PASSWORD from password where UNAME= '"+en4.get()+"'")
        # for r1 in r:
        #     Label(n, "text = r1[0], r1[1]")
        # print("inside show_data_down")
    def table():
        n = ttk.Notebook()
        n.place(x=0, y=0, width=400, height=400)
        f4 = Frame(bg="#091e42")
        n.add(f4, text="Table")
        # show_data(n)
        print("inside show_table")

    def login():
        un, up = en4.get(), en5.get()
        log = cr.execute("select * from registration where UNAME='"+un+"' and UPASS='"+up+"' ")
        for i in log:
            table()
            messagebox.showinfo("valid user")
            break
        else:
            messagebox.showinfo("invalid user")
        db.commit()
        # db.close()
        en4.set("")
        en5.set("")
    b_existing = Button(f3, text="Login", bg = "#091e42", fg= "white", command= login)
    b_existing.place(x=220, y=200, height=30, width=50)

    b_backk = Button(f3, text="<--", command=home, bg = "#091e42", fg= "white")
    b_backk.place(x=5, y=2, width=50, height=25)

home()
# db.close()
root.mainloop()