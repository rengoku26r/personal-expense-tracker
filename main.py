## this is main file that will create the dashbaord for me

from tkinter import *
from statementProcess import fetchState
import database

root  = Tk()
root.title("Expense-Tracker")
root.geometry("400x400")
root.iconbitmap("icon.ico")

def showDatabase():
    database.intializeDatabase()
    trans = database.showAllTransactions()[::-1]
    print_str = ""
    for row in trans:
        print_str += f"{row[1]} \t {row[2]} \t {row[3]} \t {row[4]} \n"

    dataTrans = Label(root,text=print_str,background="pink")
    dataTrans.grid(row=0,column=1,columnspan=4,rowspan=len(trans))
    database.closeDatabase()

fetch = Button(root,text="Fetch",command=fetchState)
fetch.grid(row = 0,column=0)

showData = Button(root,text="Show All Tranctions",command=showDatabase)
showData.grid(row = 1,column=0)

root.mainloop()