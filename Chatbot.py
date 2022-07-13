from tkinter import *

root = Tk()

def send():
     send = "You - "+e.get()
     txt.insert(END,"\n"+send)
     if(e.get()=="Hello"):
        txt.insert(END,"\n"+"Bot - Hi")
     elif(e.get()=="Hi"):
         txt.insert(END,"\n"+"Bot - Hello")
     elif(e.get()=="How are you doing?"):
         txt.insert(END,"\n"+"Bot - Doing incredibly great!   "" how about you?") 
     elif(e.get()=="I am very fine"):
         txt.insert(END,"\n"+"Bot - That is Awesome")
     else:
          txt.insert(END,"\n"+"Bot - So sorry, i don't have such information to give you now. I am still working on improving myself") 
     e.delete(0,END)
txt=Text(root)
txt.grid(row=0, column=0, columnspan=2)
e = Entry(root, width=100)
send = Button(root,text="Send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("ChatBot")
root.mainloop()
