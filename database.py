#this is simple database code that will help me in handilng the database command
import sqlite3
import os
from typing import Any

## this will use to intizlie the database command
def intializeDatabase():
    global connectDatabase
    global cur
    if "database.db" not in os.listdir():
        connectDatabase = sqlite3.connect('database.db')
        cur = connectDatabase.cursor()
        cur.execute("CREATE TABLE Transactions (unique_id INT,transaction_date TEXT, withdrawal FLOAT, deposit FLOAT,catogrey TEXT,source TEXT)")
        connectDatabase.commit()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS config (
                key TEXT PRIMARY KEY,
                value FLOAT
            )
        ''')
        connectDatabase.commit()
        x = ["PNB","SBI","Cash"]
        for i in x:
            set_config(i,0.0)
        connectDatabase.close()
    
    connectDatabase = sqlite3.connect('database.db')
    cur = connectDatabase.cursor()

def set_config(key, value):
    cur.execute('''
        INSERT OR REPLACE INTO config (key, value) 
        VALUES (?, ?)
    ''', (key, value))
    connectDatabase.commit()

def get_config(key):
    cur.execute('SELECT value FROM config WHERE key = ?', (key,))
    row = cur.fetchone()
    return row[0]

## this will help in adding the tranction in database
def addTransactions(transaction : tuple):
    try:
        cur.execute("INSERT INTO Transactions VALUES (?,?,?,?,?,?)",transaction)
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
def showAllTransactions(lastDays : int = -1) -> list[Any]:
    if(lastDays == -1):
        cur.execute("SELECT * FROM Transactions ORDER BY unique_id DESC")
    else:
        q = f"SELECT * FROM Transactions ORDER BY unique_id DESC LIMIT {lastDays}"
        cur.execute(q)
    transaction = cur.fetchall()
    return transaction

## close the connection from the database
def closeDatabase():
    connectDatabase.close()