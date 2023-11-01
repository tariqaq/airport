import csv
from prettytable import PrettyTable

globalCenter = 70
staffcsv = 'staff.csv'

def inputStaffInf():
    f1 = open(staffcsv, 'a+', newline='')
    f1writer = csv.writer(f1)
    
    staffno = int(input("Enter Staff Number: "))
    name = input("Enter Name: ")
    gender = input("Enter Gender: ")
    salary = int(input("Enter Salary: "))
    print('1. Airport Operations\n2. Cargo\n3. Navigation Service\n4. Ground Service')
    usrdept = int(input('Enter Department number : '))
    
    if usrdept == 1 :
        dept = 'Airport Operations'
    elif usrdept == 2  :
        dept = 'Cargo'
    elif usrdept == 3  :
        dept = 'Navigation Service'
    elif usrdept == 4  :
        dept = 'Ground Service'
    
    tmpRow= [staffno,name,gender,salary,dept]
    f1writer.writerow(tmpRow)
    f1.close() # SAVES file

def showStaffInf():
    f1 = open(staffcsv, 'r', newline='')
    f1reader = csv.reader(f1)
    
    table = PrettyTable()
    table.field_names = ['Staff #','Name', 'Gender', 'Salary', 'Department']
    for row in f1reader:
        table.add_row(row)
    print()
    print('---STAFF---'.center(globalCenter))
    print()
    print(table)
  
    f1.close()

def showStaffDept():
    f1 = open(staffcsv, 'r', newline='')
    f1reader = csv.reader(f1)
    aiops = []
    cargo = []
    navser = []
    grndser = []
    table = PrettyTable()
    table.field_names = ['Staff #','Name', 'Gender', 'Salary', 'Department']
    for row in f1reader:
        if row[4] == 'Airport Operations':
            table.add_row(row)
        
    print()
    print('---Airport Operations---'.center(globalCenter))
    print()
    print(table)
    
    flag = False    
    table = PrettyTable()
    table.field_names = ['Staff #','Name', 'Gender', 'Salary', 'Department']
    for row in f1reader:
        if row[4] == 'Cargo':
            table.add_row(row)
    print()
    print('---Cargo---'.center(globalCenter))
    print()
    print(table)
    
    table = PrettyTable()
    table.field_names = ['Staff #','Name', 'Gender', 'Salary', 'Department']
    for row in f1reader:
        if row[4] == 'Navigation Service':
            table.add_row(row)
 
    print()
    print('---Navigation Service---'.center(globalCenter))
    print()
    print(table)
    
    table = PrettyTable()
    table.field_names = ['Staff #','Name', 'Gender', 'Salary', 'Department']
    for row in f1reader:
        if row[4] == 'Ground Service':
            table.add_row(row)

    print()
    print('---Ground Service---'.center(globalCenter))
    print()
    print(table)
  
    f1.close()

def serStaffInf():
    f1 = open(staffcsv, 'r', newline='')
    f1reader = csv.reader(f1)
    
    usrQuery = input('Enter staff name to search : ')
    
    for row in f1reader:
        if row[1].lower() == usrQuery.lower():
            table = PrettyTable()
            table.field_names = ['Staff #','Name', 'Gender', 'Salary', 'Department']
            table.add_row(row)
            print(table)
            break
    else:
        print('Error: Staff data search unsuccessful.')
    
    f1.close()

def delStaffInf():
    f1 = open(staffcsv, 'r', newline='')
    f1reader = csv.reader(f1)

    usrDel = int(input('Enter Staff Number to delete: '))

    flag = False
    tempRows = []

    for row in f1reader:
        if row[0].lower() == usrDel.lower():
            flag = True
        else:
            tempRows.append(row)
            
    if flag:
        f1.close()
        f1 = open(staffcsv, 'w', newline='')
        f1writer = csv.writer(f1)
        f1writer.writerows(tempRows)
        f1.close()
        print('---Deleted successfully.')
    
    else:
        print('Error: Staff not found for deletion, hence not deleted.')

def staffMain():
    while True:
        print('-'*100)
        print()
        print('STAFF MANAGEMENT MENU'.center(globalCenter))
        print()
        print('-'*100)
        
        print('1. Input Staff Information\n'
            '2. Show all Staff Information \n'
            '3. Show All Staff by Departments\n'
            '4. Search Staff Information\n'
            '5. Delete Staff Information\n'
            '6. Go back')
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            
            inputStaffInf()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 2 :
            
            showStaffInf()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 3 :
            
            showStaffDept()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 4 :
            
            serStaffInf()
            
            input('---Press ENTER to go back.')
        
        elif usrChoice == 5 :
            
            delStaffInf()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 6 :
            
            break
            
        else:
            input('Error : Wrong choice. Press ENTER to go back.')