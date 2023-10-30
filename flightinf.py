import csv
from prettytable import PrettyTable

globalCenter = 70
dep = 'departures.csv'
arr = 'arrivals.csv'

def inputFlightInf(csvfile):
    f1 = open(csvfile, 'a+', newline='')
    f1writer = csv.writer(f1)
    
    time = input("Enter TIME: ")
    dest = input("Enter DESTINATION: ")
    flightNo = int(input("Enter FLIGHT #: "))
    airline = input("Enter AIRLINE: ")
    terminal = input("Enter TERMINAL: ")
    gate = int(input("Enter GATE: "))
    flightStat = input("Enter STATUS: ")   
    
    tmpRow= [time,dest,flightNo,airline,terminal,gate,flightStat]
    f1writer.writerow(tmpRow)
    f1.close() # SAVES file
    
def showAllInf():
    f1 = open(dep, 'r', newline='')
    f2 = open(arr, 'r', newline='')
    f1reader = csv.reader(f1)
    f2reader = csv.reader(f2)
    
    table = PrettyTable() # departures
    table.field_names = ['TIME','DESTINATION', 'FLIGHT #', 'AIRLINE', 'TERMINAL', 'GATE', 'STATUS']
    for row in f1reader:
        table.add_row(row)
    print()
    print('---DEPARTURES---'.center(globalCenter))
    print()
    print(table)
    
    table = PrettyTable() # arrivals
    table.field_names = ['TIME','DESTINATION', 'FLIGHT NO.', 'AIRLINE', 'TERMINAL', 'GATE', 'STATUS']
    for row in f2reader:
        table.add_row(row)
    print()
    print('---ARRIVALS---'.center(globalCenter))
    print()
    print(table) 
    
    f1.close()

def serInf(csvfile):
    f1 = open(csvfile, 'r', newline='')
    f1reader = csv.reader(f1)
    
    usrQuery = input('Enter destination to search flights: ')
    
    for row in f1reader:
        if row[1].lower() == usrQuery.lower():
            table = PrettyTable()
            table.field_names = ['TIME','DESTINATION', 'FLIGHT NO.', 'AIRLINE', 'TERMINAL', 'GATE', 'STATUS']
            table.add_row(row)
            print(table)
            break
    else:
        print('Error: City Data search unsuccessful.')
    
    f1.close()

def delInf(csvfile):
    f1 = open(csvfile, 'r', newline='')
    f1reader = csv.reader(f1)

    usrDel = input('Enter flight no. to delete: ')

    flag = False
    tempRows = []

    for row in f1reader:
        if row[2].lower() == usrDel.lower():
            flag = True
        else:
            tempRows.append(row)
            
    if flag:
        f1.close()
        f1 = open(csvfile, 'w', newline='')
        f1writer = csv.writer(f1)
        f1writer.writerows(tempRows)
        f1.close()
        print('---Deleted successfully.')
    
    else:
        print('Error: City not found for deletion, hence not deleted.')

def flightInfMain():
    while True:
        print('-'*100)
        print()
        print('FLIGHT INFORMATION MENU'.center(globalCenter))
        print()
        print('-'*100)
        
        print('1. Input Departure Flight Information\n'
            '2. Input Arrival Flight Information \n'
            '3. Show all Saved Information\n'
            '4. Search Departure Flight Information\n'
            '5. Search Arrival Flight Information\n'
            '6. Delete Departure Flight Information\n'
            '7. Delete Arrival Flight Information\n'
            '8. Go back')
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            
            inputFlightInf(dep)
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 2 :
            
            inputFlightInf(arr)
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 3 :
            
            showAllInf()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 4 :
            
            serInf(dep)
            
            input('---Press ENTER to go back.')
        
        elif usrChoice == 5 :
            
            serInf(arr)
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 6 :
            
            delInf(dep)
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 7 :
            
            delInf(arr)
            
            input('---Press ENTER to go back.')

        elif usrChoice == 8 :
            break
        
        else:
            input('Error : Wrong choice. Press ENTER to go back.')