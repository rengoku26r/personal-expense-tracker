import tkinter as tk
from tkinter import messagebox
from datetime import datetime
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

def createInsights(textL : str) -> tk.Label: 
    insights_i = tk.Frame(insights, bg = "white",width=300)
    insights_i.pack(fill=tk.Y,anchor="w",side="left",expand=True)
    insights_i.pack_propagate(False)
    tk.Label(insights_i,text=textL).pack()
    x = tk.Label(insights_i,text=0.0)
    x.pack()
    return x

labelInsights = ["PNB","Cash","SBI","Total"]
insightsLabel = []
for eachLabel in labelInsights:
    insightsLabel.append(createInsights(eachLabel))

def updateInsights():
    for i in range(0,3):
        insightsLabel[i].configure(text = database.get_config(labelInsights[i]))
    insightsLabel[3].configure(text = (database.get_config(labelInsights[0]) + database.get_config(labelInsights[1]) + database.get_config(labelInsights[2])))

header = ["Transaction Date", "Withdrawal", "Deposit", "Catogrey", "Source",""]

headerFrame = tk.Frame(mainWindow,height=40,bg="blue")
headerFrame.pack(fill=tk.X)
headerFrame.pack_propagate(False)

for textL in header:
    x = tk.Frame(headerFrame,width=190)
    x.pack(side="left",fill=tk.Y,expand=True,padx=(10,0),anchor="w")
    x.pack_propagate(False)
    tk.Label(x,text=textL).pack()

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
    if(is_mouse_over_canvas and len(trans) > 11):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", mouse_scroll)
canvas.bind("<Enter>", on_enter)
canvas.bind("<Leave>", on_leave)

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
    root.lift()
    root.focus_force()

def addthevalue():
    try:
        datetime.strptime(dateTranstion.get(), "%d/%m/%Y")
    except:
        messagebox.showerror(title="Invalid Format",message="Date is not in the valid format.Use DD/MM/YYYY format.")
        top.lift()
        top.focus_force()
        return
    try:
        float(withdrawal.get())
    except:
        messagebox.showerror(title="Invalid Format",message="Withdrawal should be decimal or intger in ruppes.")
        top.lift()
        top.focus_force()
        return
    try:
        float(deposite.get())
    except:
        messagebox.showerror(title="Invalid Format",message="Deposite should be decimal or intger in ruppes.")
        top.lift()
        top.focus_force()
        return
    if(deposite.get() > 0 and withdrawal.get() > 0):
        messagebox.showerror(title="Invalid Tranctions",message="Deposite and Withdrawl cannot be done together.")
        top.lift()
        top.focus_force()
        return
    if(deposite.get() == 0 and withdrawal.get() == 0):  
        messagebox.showerror(title="Invalid Tranctions",message="Both cannot be zero at ones.")
        top.lift()
        top.focus_force()
        return
    if withdrawal.get() != 0:
        if(database.get_config(choosedoptions.get())-withdrawal.get() < 0):
            messagebox.showerror(title="Invalid Tranctions",message="Insufficent balnce")
            top.lift()
            top.focus_force()
            return 
        else:
            database.set_config(choosedoptions.get(),database.get_config(choosedoptions.get())-withdrawal.get())
    else:
        database.set_config(choosedoptions.get(),database.get_config(choosedoptions.get())+deposite.get())
    now = datetime.now()
    z = now.strftime("%H%M%S")
    y = datetime.strptime(dateTranstion.get(), "%d/%m/%Y").strftime("%Y%m%d")
    database.addTransactions((int(y+z),dateTranstion.get(),float(withdrawal.get()),float(deposite.get()),catogrey.get(),choosedoptions.get()))
    fetchTranction()
    updateInsights()
    delteteTop()      
    
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
    global dateTranstion
    now = datetime.now()
    dateTranstion = tk.StringVar(value=now.strftime("%d/%m/%Y"))
    dateTrans = tk.Entry(top,textvariable=dateTranstion)
    dateTrans.grid(row=0,column=1)
    tk.Label(top,text="Withdrawal").grid(row=1,column=0)
    global withdrawal
    withdrawal = tk.DoubleVar(value=0.0)
    withd = tk.Entry(top,textvariable=withdrawal)
    withd.grid(row=1,column=1)
    tk.Label(top,text="Deposit").grid(row=2,column=0)
    global deposite
    deposite = tk.DoubleVar(value=0.0)
    depo = tk.Entry(top,textvariable=deposite)
    depo.grid(row=2,column=1)
    tk.Label(top,text="Catogrey").grid(row=3,column=0)
    global catogrey
    catogrey = tk.StringVar(value="food,cloths,etc..")
    cato = tk.Entry(top,textvariable=catogrey)
    cato.grid(row=3,column=1)
    options = ["PNB","SBI","Cash"]
    global choosedoptions
    choosedoptions = tk.StringVar()
    choosedoptions.set(options[0])
    tk.Label(top,text="Source").grid(row=4,column=0)
    sour = tk.OptionMenu(top,choosedoptions,*options)
    sour.grid(row=4,column=1)
    submit = tk.Button(top,text="Add",command=addthevalue)
    submit.grid(row=5)
    top.update_idletasks()
    top.lift()    
    top.focus_force()
    dateTrans.focus_set()
    top.protocol("WM_DELETE_WINDOW", delteteTop)
    top.mainloop()

def delteteTop1():
    top1.destroy()
    root.lift()
    root.focus_force()
    add_trans.config(state="normal")
    fetch_trans.config(state="normal")
    updateInsights()

def addtheblance(): 
    try:
        float(pnbcash.get())
        float(sbicash.get())
        float(cashcash.get())
    except:
        messagebox.showerror(title="Invalid Format",message="Amount should be decimal or intger in ruppes.")
        top1.focus_force()
        top1.lift()
        return
    database.set_config("PNB",pnbcash.get())
    database.set_config("SBI",sbicash.get())
    database.set_config("Cash",cashcash.get())
    delteteTop1() 

def addBlance():
    add_trans.config(state="disabled")
    fetch_trans.config(state="disabled")
    app_width = 250
    app_height = 180
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - app_width) / 2
    y = (screen_height - app_height) / 2
    global top1
    top1 = tk.Toplevel()
    top1.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
    top1.resizable(False,False)
    top1.title("Opening Blance!!")
    tk.Label(top1,text="PNB").grid(row=0,column=0)
    global pnbcash
    pnbcash = tk.DoubleVar(value=0.0)
    withd = tk.Entry(top1,textvariable=pnbcash)
    withd.grid(row=0,column=1)
    tk.Label(top1,text="SBI").grid(row=1,column=0)
    global sbicash
    sbicash = tk.DoubleVar(value=0.0)
    withd1 = tk.Entry(top1,textvariable=sbicash)
    withd1.grid(row=1,column=1)
    tk.Label(top1,text="Cash").grid(row=2,column=0)
    global cashcash
    cashcash = tk.DoubleVar(value=0.0)
    withd11 = tk.Entry(top1,textvariable=cashcash)
    withd11.grid(row=2,column=1)
    submit = tk.Button(top1,text="Add",command=addtheblance)
    submit.grid(row=3)
    top1.update_idletasks()
    top1.lift()    
    top1.focus_force()
    withd.focus_set()
    top1.protocol("WM_DELETE_WINDOW", delteteTop1)
    top1.mainloop()

def fetchTranction():
    x = 0
    for i in range(0,len(labelInsights)-1):
        x += int(database.get_config(labelInsights[i]))
    global trans
    trans = database.showAllTransactions()
    if x == 0 and len(trans) == 0:
        addBlance()
        return
    for widget in transFrame.winfo_children():
        widget.destroy()
    pnb_balance = 0
    sbi_balance = 0
    cash_blance = 0
    if(len(trans) == 0):
        print("No tranction")
    else:
        for item in reversed(trans):
            if(item[5] == "PNB"):
                if(item[2] != 0):
                    pnb_balance -= item[2]
                else:
                    pnb_balance += item[3]
            elif(item[5] == "SBI"):
                if(item[2] != 0):
                    sbi_balance -= item[2]
                else:
                    sbi_balance += item[3]
            else:
                if(item[2] != 0):
                    cash_blance -= item[2]
                else:
                    cash_blance += item[3]
        for item in trans:
            x = tk.Frame(transFrame,height=32,bg="pink")
            x.pack(fill=tk.X, padx=4,pady=8)
            x.pack_propagate(False)
            for i in range(1,len(item)):
                y = tk.Frame(x,width=190)
                y.pack(side="left",fill=tk.Y,expand=True,padx=(10,0),anchor="w")
                y.pack_propagate(False)
                tk.Label(y,text=item[i]).pack()
            y = tk.Frame(x,width=190)
            y.pack(side="left",fill=tk.Y,expand=True,padx=(10,0),anchor="w")
            y.pack_propagate(False)
            tk.Label(y,text="Delete").pack()
    updateInsights()

add_trans = createButton("Add Tranction")
add_trans.configure(command=addTrans)
fetch_trans = createButton("Fetch Tranction")
fetch_trans.config(command=fetchTranction)

database.intializeDatabase()
fetchTranction()

root.mainloop()