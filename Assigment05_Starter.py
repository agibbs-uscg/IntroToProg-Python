# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# AGibbs, 16MAY2020, Created code to import dictionary from .txt, built option to see data,
#   add data, delete data, and save data.
# AGibbs, 17MAY2020, Tested in PYCHARM and CMD, no errors. Fixed Typos
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # An object that represents a file
strFile = "C:\_PythonClass\Assignment05\ToDoList.txt"
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)


objFile = open(strFile, 'r')
for row in objFile:
    lstRow = row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}  # brings in data into dictionary
    lstTable.append(dicRow)  # creates table of dictionaries

objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Task | Priority')
        for dicRow in lstTable:
            print(dicRow['Task'] + " | " + dicRow['Priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter task needed to complete: ")
        strPriority = (input('Enter priority number from 1(low) to 10(high): '))
        dicRow = {'Task': strTask, 'Priority': strPriority}
        lstTable.append(dicRow)  # appends lstTable with new entries
        print('Task and Priority added!')
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):  # list.remove(element)
        print('Task | Priority')
        for dicRow in lstTable:
            print(dicRow['Task'] + " | " + dicRow['Priority'])
        strRemove = input('Type in the Task you want to remove: ')
        for dicRow in lstTable:
            if (dicRow['Task'].lower() == strRemove.lower()): # .lower in care user input wrong case
                lstTable.remove(dicRow)  # list.remove(element)
                print('Task (' + strRemove + ') removed from list')
            else:
                print('That task is not on the list, please try again')  # in case user does not enter correct item
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open(strFile, 'w')
        for dicRow in lstTable:
            objFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')  # \n important for newline in txt file
        objFile.close()
        print('Your data has been saved')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Goodbye!')
        break  # and Exit the program

    else:
        print('Please select only from the menu of options')  # in case user makes a choice other than 1,2,3,4,5
