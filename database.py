#this is simple database code that will help me in handilng the database command
import sqlite3
import os

## this will use to intizlie the database command
def intializeDatabase():
    global connectDatabase
    global cur
    if "database.db" not in os.listdir():
        connectDatabase = sqlite3.connect('database.db')
        cur = connectDatabase.cursor()
        cur.execute("CREATE TABLE Transactions (transaction_date TEXT, withdrawal FLOAT, deposit FLOAT,catogrey TEXT,source TEXT)")
        connectDatabase.commit()
        connectDatabase.close()
    
    connectDatabase = sqlite3.connect('database.db')
    cur = connectDatabase.cursor()

## this will help in adding the tranction in database
def addTransactions(transaction : tuple):
    try:
        cur.execute("INSERT INTO Transactions VALUES (?,?,?,?,?)",transaction)
        connectDatabase.commit()
    except:
        print("Error...")

## this will help in deleting the database 
def deleteTransactions(transaction : tuple):
    try:
        cur.execute("DELETE FROM Transactions WHERE transaction_date=(?) AND withdrawal=(?) AND deposit=(?) AND catogrey=(?) AND source=(?)",transaction)
        connectDatabase.commit()
    except:
        print("item does not exist...")

## this will return the whole database
def showAllTransactions():
    cur.execute("SELECT rowid, * FROM Transactions")
    transaction = cur.fetchall()
    return transaction

## close the connection from the database
def closeDatabase():
    connectDatabase.close()

def weekTransactions():
    cur.execute("SELECT rowid, * FROM Transactions ORDER BY rowid DESC LIMIT 7")
    transaction = cur.fetchall()
    return transaction