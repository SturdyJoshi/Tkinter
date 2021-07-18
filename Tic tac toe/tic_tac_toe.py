# Tic tac toe  by Neeraj Joshi

from tkinter import *
root = Tk()
root.title("Tic Tac Toe")
count=0
root.geometry("270x275")
root.resizable(0,0)

def show(b):
    if b["text"] == " ":
        global count
        if count %2 == 0:
            b["text"]= "O"
        else:
            b["text"]= "X"
        if check(b):
            print(b["text"], "is winner")
            # import sys
            # sys.exit()
        count +=1


def check(b):
    if(    (b1["text"]== b["text"] and b2["text"]== b["text"] and b3["text"]== b["text"])
        or (b1["text"]== b["text"] and b4["text"]== b["text"] and b7["text"]== b["text"])
        or (b2["text"]== b["text"] and b5["text"]== b["text"] and b8["text"]== b["text"])
        or (b3["text"]== b["text"] and b6["text"]== b["text"] and b9["text"]== b["text"])
        or (b4["text"]== b["text"] and b5["text"]== b["text"] and b6["text"]== b["text"])
        or (b7["text"]== b["text"] and b8["text"]== b["text"] and b9["text"]== b["text"])
        or (b1["text"]== b["text"] and b5["text"]== b["text"] and b9["text"]== b["text"])
        or (b3["text"]== b["text"] and b5["text"]== b["text"] and b7["text"]== b["text"])):
        return True;

    return False


b1 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b1))
b1.grid(row=0, column=0)

b2 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b2))
b2.grid(row=0, column=1)

b3 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b3))
b3.grid(row=0, column=2)

b4 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b4))
b4.grid(row=1, column=0)

b5 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b5))
b5.grid(row=1, column=1)

b6 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b6))
b6.grid(row=1, column=2)

b7 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b7))
b7.grid(row=2, column=0)

b8 = Button(root, text=" ", width= 10, height= 5, font= ("Arial", 10), command= lambda:show(b8))
b8.grid(row=2, column=1)

b9 = Button(root, text=" ", width= 10, height= 5, font= ("Arial",10), command= lambda:show(b9))
b9.grid(row=2, column=2)

root.mainloop()