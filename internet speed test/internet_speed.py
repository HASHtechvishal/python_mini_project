from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/ (10 ** 6) ,3))+ " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x700")
sp.config(bg="gray")
lab = Label(sp,text="internet speed test", font=("time new roman",20,"bold"),bg="gray",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed", font=("time new roman",20,"bold"),bg="gray",fg="white")
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp,text="00", font=("time new roman",20,"bold"),bg="gray",fg="white")
lab_down.place(x=60,y=200,height=50,width=380)

lab = Label(sp,text="Upload speed", font=("time new roman",20,"bold"),bg="gray",fg="white")
lab.place(x=60,y=300,height=50,width=380)

lab_up = Label(sp,text="00", font=("time new roman",20,"bold"),bg="gray",fg="white")
lab_up.place(x=60,y=400,height=50,width=380)

button = Button(sp,text="check speed",font=("time new roman",30,"bold"),bg="black",relief=RAISED,command=speedCheck)
button.place(x=60, y=500 , height= 50, width=380 )

sp.mainloop()