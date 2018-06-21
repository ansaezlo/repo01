""" This is my first program in phyton
my idea is to query a Vertica Database
using the VMart example DB 
"""

import pyodbc
import os

#Establecemos el directorio de configuracion
configdir = "configfiles"

print("Please, a value between 1-9 to perform a query to the Vertica VMart Database \n")

try:
    option = int(input("Enter 1-9: "))
except:
    print ("Your input is not a number")
    option = -1
while (1 <= option) and ( 9 >= option):
    
    """ Getting the sql from files """
    filename = "sql"+ str(option) +".sql"
    path = os.path.dirname(os.path.abspath(__file__))
    fullpathfile = path + "\\" + configdir + "\\" + filename
    #print ("Filename: ",filename)
    #print ("Path: ",path)
    #print ("configdir :",configdir)
    print ("Full path to sql file: ", fullpathfile)
    file = open(fullpathfile,"r")
    query = file.read()
    file.close()
    print ("Query to be executed: \n",query)
    input ("\n Press any key to continue... \n")

    #Executing the query
    try:
        print("Opening DB connection")
        dbconn = pyodbc.connect("DSN=c7vertican1VMart", ansi=True)
    except:
        print("Unable to get the DB connection")
    cur = dbconn.cursor()
    try:
        cur.execute(query)
    except:
        print("Error in the query execution")
    print("Output : \n")
    rows = cur.fetchall()
    for row in rows:
        print (row, "\n")
    cur.close()
    dbconn.close()

    try:
       option = int(input("Enter 1-9: "))
    except:
        print ("Your input is not a number")
        option = -1
    print("Entered: ",option)

    #End while
exit

