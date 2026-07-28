import tkinter as tk
from turtle import color

from sqlalchemy import false
import database

root = tk.Tk()

app_width = 1280
app_height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - app_width) / 2
y = (screen_height - app_height) / 2

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
root.title("Expense Tracker")
root.resizable(False,False)

mainWindow = tk.Frame(root,bg="pink")
mainWindow.pack(fill=tk.BOTH,expand=True)
mainWindow.pack_propagate(False)

insights = tk.Frame(mainWindow,bg = "yellow",height=100)
insights.pack(fill=tk.X,expand=True,anchor="n")
insights.pack_propagate(False)

def createInsights(textL : str) -> tk.Frame: 
    insights_i = tk.Frame(insights, bg = "white",width=300)
    insights_i.pack(fill=tk.Y,anchor="w",side="left",expand=True)
    insights_i.pack_propagate(False)
    tk.Label(insights_i,text=textL).pack()
    return insights_i

labelInsights = ["PNB","Cash","SBI","Total"]
frameInsights = []
for eachLabel in labelInsights:
    frameInsights.append(createInsights(eachLabel))

def updateInsights(details : tuple = (0,0,0)):
    if details == (0,0,0):
        print("hello")

updateInsights()

header = ["Transaction Date", "Withdrawal", "Deposit", "Balance", "Catogrey", "Source"]

headerFrame = tk.Frame(mainWindow,height=40,bg="blue")
headerFrame.pack(fill=tk.X)
headerFrame.pack_propagate(False)
tk.Label(headerFrame,text="abc").pack()

tansHist = tk.Frame(mainWindow,bg = "black",height=530,width=1280)
tansHist.pack()
tansHist.pack_propagate(False)

canvas = tk.Canvas(tansHist, bg="white", highlightthickness=0)
# scrollbar = ttk.Scrollbar(tansHist,orient="vertical",command=canvas.yview)
transFrame = tk.Frame(canvas)
transFrame.bind("<Configure>", lambda e:canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0),window=transFrame,anchor="nw",width=1280)
# canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
# scrollbar.pack(side=RIGHT,fill=Y)

is_mouse_over_canvas = False

def on_enter(event):
    global is_mouse_over_canvas
    is_mouse_over_canvas = True

def on_leave(event):
    global is_mouse_over_canvas
    is_mouse_over_canvas = False

def mouse_scroll(event):
    if(is_mouse_over_canvas):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)
canvas.bind("<Enter>", on_enter)
canvas.bind("<Leave>", on_leave)

for i in range(0,25):
    x = tk.Frame(transFrame,height=32,bg="pink")
    x.pack(fill=tk.X, padx=4,pady=8)
    x.pack_propagate(False)
    tk.Label(x,text=i+1).pack()

functionBtn = tk.Frame(mainWindow,bg = "yellow",height=50)
functionBtn.pack(fill=tk.X,expand=True,anchor="s")
functionBtn.pack_propagate(False)

def createButton(textL : str) -> tk.Button:
    btn = tk.Button(functionBtn,text=textL)
    btn.pack(pady=6,side="left",padx=(10,0))
    return btn

def delteteTop():
    add_trans.config(state="normal")
    top.destroy()

def addTrans():
    add_trans.config(state="disabled")
    app_width = 250
    app_height = 180
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - app_width) / 2
    y = (screen_height - app_height) / 2
    global top
    top = tk.Toplevel()
    top.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
    top.resizable(False,False)
    tk.Label(top,text="Transaction Date").grid(row=0,column=0)
    dateTrans = tk.Entry(top)
    dateTrans.grid(row=0,column=1)
    tk.Label(top,text="Withdrawal").grid(row=1,column=0)
    withd = tk.Entry(top)
    withd.grid(row=1,column=1)
    tk.Label(top,text="Deposit").grid(row=2,column=0)
    depo = tk.Entry(top)
    depo.grid(row=2,column=1)
    tk.Label(top,text="Catogrey").grid(row=3,column=0)
    cato = tk.Entry(top)
    cato.grid(row=3,column=1)
    options = ["PNB","SBI","Cash"]
    choosedoptions = tk.StringVar()
    choosedoptions.set(options[0])
    tk.Label(top,text="Source").grid(row=4,column=0)
    sour = tk.OptionMenu(top,choosedoptions,*options)
    sour.grid(row=4,column=1)
    submit = tk.Button(top,text="Add",command=delteteTop)
    submit.grid(row=5)
    top.protocol("WM_DELETE_WINDOW", delteteTop)
    top.mainloop()

add_trans = createButton("Add Tranction")
add_trans.configure(command=addTrans)
fetch_trans = createButton("Fetch Tranction")
update_value = createButton("Update the cash")

database.intializeDatabase()

root.mainloop()