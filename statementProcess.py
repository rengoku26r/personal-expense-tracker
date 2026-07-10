#this is the setup to process the stament and save it to the database, statement will upload manuanlly
import os
import pandas as pd
import database

def fetchState():

    database.intializeDatabase()

    pathStatements = "Statement"
    listStatements = os.listdir(pathStatements)

    for statement in listStatements:
        processedStatement = pd.read_csv(os.path.join(pathStatements,statement),skiprows=20,skipfooter=19,engine='python')
        processedStatement = processedStatement[["Transaction Date","Withdrawal","Deposit","Balance"]]
        processedStatement = processedStatement.fillna("0.00")
        # processedStatement["Transaction Date"] = pd.to_datetime(processedStatement["Transaction Date"], format="%d/%m/%Y")
        processedStatement["Transaction Date"] = processedStatement["Transaction Date"].astype(str)
        processedStatement["Deposit"] = processedStatement["Deposit"].str.replace(',', '').astype(float)
        processedStatement["Withdrawal"] = processedStatement["Withdrawal"].str.replace(',', '').astype(float)
        processedStatement["Balance"] = processedStatement["Balance"].str.replace(' Cr.', '')
        processedStatement["Balance"] = processedStatement["Balance"].str.replace(',', '').astype(float)
        processedStatement = processedStatement.iloc[::-1]

        os.remove(os.path.join(pathStatements,statement))

        for row in processedStatement.itertuples(index=False,name=None):
            database.addTransactions((row[0],row[1],row[2],row[3]))
            
    print("suiiiiiiiiiiiiiiiiiii!!!")
    database.closeDatabase()
