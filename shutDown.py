from tkinter import *
import os

def Restart():
    os.system("sudo shutdown /r /t 1")
def Restart_time():
    os.system("sudo shutdown /r /t 20")
def Log_out():
    os.system("sudo shutdown -1")
def shutDown():
    os.system("sudo shutdown -h now")# code for mac 

st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")
r_button = Button(st,text="Restart",font=("Time new roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart time",font=("Time new roman",20,"bold"),relief=RAISED,cursor="plus",command=Restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st,text="Log-out",font=("Time new roman",20,"bold"),relief=RAISED,cursor="plus",command=Log_out)
lg_button.place(x=150,y=270,height=50,width=200)

sh_button = Button(st,text="shutDown",font=("Time new roman",20,"bold"),relief=RAISED,cursor="plus",command=shutDown)
sh_button.place(x=150,y=370,height=50,width=200)


st.mainloop()