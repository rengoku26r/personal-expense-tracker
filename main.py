from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1424x801")
root.iconbitmap("icon.ico")
root.title("Expense Tracker")
root.config(bg="blue")
root.resizable(False,False)

main = Frame(root, bg="purple")
main.pack(fill=BOTH,expand=True,padx=10,pady=10)

sidebar = Frame(main,bg = "green",width=151)
sidebar.pack(fill=Y,side=LEFT)
sidebar.pack_propagate(False)

def sidebarBtn(text : str) -> Button:
    btn = Button(sidebar,text=text,bg="black",fg="green",width=15);
    btn.pack(anchor="n",pady=5)
    return btn

hello = sidebarBtn("hello")
bye = sidebarBtn("bye")

if True:
    insigts = Frame(main,bg="red",height=300)
    insigts.pack(fill=X,side=TOP,anchor="n")
    insigts.pack_propagate(False)
    insigts0 = Frame(insigts,bg="red",height=35)
    insigts0.pack(fill=X,side=TOP,anchor="n")
    insigts0.pack_propagate(False)
    Label(insigts0,text="Insights").pack(anchor="nw",padx = (5,0),pady=(5,0))

    insigts1 = Frame(insigts,bg="gray",height=132.5)
    insigts1.pack(fill=X,side=TOP,anchor="n")
    insigts1.pack_propagate(False)

    insigts2 = Frame(insigts,bg="white",height=132.5)
    insigts2.pack(fill=X,side=TOP,anchor="n")
    insigts2.pack_propagate(False)

    pnb = Frame(insigts1,bg="yellow", width=250)
    pnb.pack(fill = Y, expand=True,anchor="w", padx = 20, pady = 2.5, side=LEFT)

    sbi = Frame(insigts1,bg="yellow", width=250)
    sbi.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5, side=LEFT)

    cash = Frame(insigts1,bg="yellow", width=250)
    cash.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5, side=LEFT)

    totalBlan = Frame(insigts1,bg="yellow", width=250)
    totalBlan.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side = LEFT)

    loan= Frame(insigts2,bg="yellow", width=250)
    loan.pack(fill = Y, expand=True,anchor="w", padx = 20, pady = 2.5, side=LEFT)

    donate = Frame(insigts2,bg="yellow", width=250)
    donate.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side=LEFT)

    credit = Frame(insigts2,bg="yellow", width=250)
    credit.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side=LEFT)

    spent = Frame(insigts2,bg="yellow", width=250)
    spent.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side=LEFT)
Label(main,text="hello this tranction block how do you do").pack(anchor="w")

tansHist = Frame(main,bg = "pink")
tansHist.pack(fill=BOTH,expand=True)

canvas = Canvas(tansHist,bg="darkgreen")
scrollbar = ttk.Scrollbar(tansHist,orient="vertical",command=canvas.yview)
transFrame = Frame(canvas,bg="skyblue")
transFrame.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0),window=transFrame,anchor="nw",width=900)
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT,fill=BOTH,expand=True)
scrollbar.pack(side=RIGHT,fill=Y)

def mouse_scroll(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)

root.mainloop()