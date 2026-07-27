from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

BG = "#716C8E"
CARD = "#2B2640"
SIDEBAR = "#251F38"
PURPLE = "#8B5CF6"
PURPLE_HOVER = "#A78BFA"
TEXT = "#FFFFFF"
SUBTEXT = "#B9B4D0"
RED = "#EF4444"

root = Tk()
root.geometry("1424x801")
root.iconbitmap("icon.ico")
root.title("Expense Tracker")
root.resizable(False,False)

image = Image.open("background.png")
image = image.resize((1424, 801), Image.LANCZOS)   # Match window size
bg_image = ImageTk.PhotoImage(image)

bg_label = Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

main = Frame(root, bg = "")
main.place(x=0, y=0, relwidth=1, relheight=1)

sidebar = Frame(main,width=151, bg = "")
sidebar.pack(fill=Y,side=LEFT,padx=5,pady=5)
sidebar.pack_propagate(False)

def sidebarBtn(text : str) -> Button:
    btn = Button(sidebar,text=text,width=15);
    btn.pack(anchor="n",pady=5)
    return btn

hello = sidebarBtn("hello")
bye = sidebarBtn("bye")

if True:
    insigts = Frame(main ,height=300, bg = "")
    insigts.pack(fill=X,side=TOP,anchor="n")
    insigts.pack_propagate(False)
    insigts0 = Frame(insigts ,height=35)
    insigts0.pack(fill=X,side=TOP,anchor="n")
    insigts0.pack_propagate(False)
    Label(insigts0,text="Insights").pack(anchor="nw",padx = (5,0),pady=(5,0))

    insigts1 = Frame(insigts ,height=132.5)
    insigts1.pack(fill=X,side=TOP,anchor="n")
    insigts1.pack_propagate(False)

    insigts2 = Frame(insigts ,height=132.5)
    insigts2.pack(fill=X,side=TOP,anchor="n")
    insigts2.pack_propagate(False)

    pnb = Frame(insigts1  , width=250)
    pnb.pack(fill = Y, expand=True,anchor="w", padx = 20, pady = 2.5, side=LEFT)

    sbi = Frame(insigts1  , width=250)
    sbi.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5, side=LEFT)

    cash = Frame(insigts1  , width=250)
    cash.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5, side=LEFT)

    totalBlan = Frame(insigts1  , width=250)
    totalBlan.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side = LEFT)

    loan= Frame(insigts2  , width=250)
    loan.pack(fill = Y, expand=True,anchor="w", padx = 20, pady = 2.5, side=LEFT)

    donate = Frame(insigts2  , width=250)
    donate.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side=LEFT)

    credit = Frame(insigts2  , width=250)
    credit.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side=LEFT)

    spent = Frame(insigts2  , width=250)
    spent.pack(fill = Y, expand=True,anchor="w", padx = 2.5, pady = 2.5,side=LEFT)
Label(main,text="hello this tranction block how do you do" ).pack(anchor="w")

tansHist = Frame(main)
tansHist.pack(fill=BOTH,expand=True)

canvas = Canvas(tansHist )
# scrollbar = ttk.Scrollbar(tansHist,orient="vertical",command=canvas.yview)
transFrame = Frame(canvas )
transFrame.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0),window=transFrame,anchor="nw",width=900)
# canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT,fill=BOTH,expand=True)
# scrollbar.pack(side=RIGHT,fill=Y)

def mouse_scroll(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)

for i in range(0,25):
    x = Frame(transFrame,height=32)
    x.pack(fill=X, padx=4,pady=8)
    x.pack_propagate(False)

root.mainloop()