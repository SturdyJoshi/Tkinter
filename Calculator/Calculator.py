from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("245x315")
root.resizable(0, 0)
root.configure(background="black")
s = StringVar()
def show1(c):
    if (c == 'C'):
        s.set("")
    elif (c == '='):
        ex = s.get()
        s.set(eval(ex))
    else:
        s.set(s.get() + c)
e1 = Entry(root, justify="right", font=("Arial", 30), textvariable=s)
e1.place(x=0, y=0, width="245", height="50")
b = [Button] * 16
data = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "+", "C", "0", "=", "-"]
X,Y,k = 5,55,0
for i in range(4):
    for j in range(4):
        b[k] = Button(root, text=data[k], font=("Arial",), fg="black", bg="gray", activebackground="yellow", activeforeground="blue")
        b[k].place(x=X, y=Y, height=60, width=55)
        k = k + 1
        X = X + 60
    Y = Y + 65
    X = 5
b[0].configure(command=lambda :show1(data[0]))
b[1].configure(command=lambda:show1(data[1]))
b[2].configure(command=lambda:show1(data[2]))
b[3].configure(command=lambda:show1(data[3]))
b[4].configure(command=lambda:show1(data[4]))
b[5].configure(command=lambda:show1(data[5]))
b[6].configure(command=lambda:show1(data[6]))
b[7].configure(command=lambda:show1(data[7]))
b[8].configure(command=lambda:show1(data[8]))
b[9].configure(command=lambda:show1(data[9]))
b[10].configure(command=lambda:show1(data[10]))
b[11].configure(command=lambda:show1(data[11]))
b[12].configure(command=lambda:show1(data[12]))
b[13].configure(command=lambda:show1(data[13]))
b[14].configure(command=lambda:show1(data[14]))
b[15].configure(command=lambda:show1(data[15]))
root.mainloop()
