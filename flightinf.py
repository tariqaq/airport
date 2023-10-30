import csv
from prettytable import PrettyTable

globalCenter = 100

def inputFlightInf(csvfile):
    f1 = open(csvfile, 'a+', newline='')
    f1writer = csv.writer(f1)
    
    time = input(f"Enter TIME: ")
    dest = input(f"Enter DESTINATION: ")
    flightNo = input(f"Enter FLIGHT #: ")
    airline = input(f"Enter AIRLINE: ")
    terminal = input(f"Enter TERMINAL: ")
    gate = input(f"Enter GATE: ")
    flightStat = input(f"Enter STATUS: ")   
    
    tmpRow= [time,dest,flightNo,airline,terminal,gate,flightStat]
    f1writer.writerow(tmpRow)
    f1.close() # SAVES file
    
def showAllInf():
    f1 = open('departures.csv', 'r', newline='')
    f2 = open('arrivals.csv', 'r', newline='')
    f1reader = csv.reader(f1)
    f2reader = csv.reader(f2)
    
    table = PrettyTable() # departures
    table.field_names = ['TIME','DESTINATION', 'FLIGHT #', 'AIRLINE', 'TERMINAL', 'GATE', 'STATUS']
    for row in f1reader:
        table.add_row(row)
    print('-'*100)
    print()
    print('DEPARTURES'.center(globalCenter))
    print()
    print('-'*100)
    print(table)
    
    table = PrettyTable() # arrivals
    table.field_names = ['TIME','DESTINATION', 'FLIGHT #', 'AIRLINE', 'TERMINAL', 'GATE', 'STATUS']
    for row in f2reader:
        table.add_row(row)
    print('-'*100)
    print()
    print('ARRIVALS'.center(globalCenter))
    print()
    print('-'*100)
    print(table) 
    
    f1.close()
    
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
            '4. (ph)\n'
            '5. Go back')
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            
            inputFlightInf('departures.csv')
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 2 :
            
            inputFlightInf('arrivals.csv')
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 3 :
            
            showAllInf()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 4 :
            
            print('-ph-')
            
            input('---Press ENTER to go back.')

        elif usrChoice == 5 :
            
            break
        
        else:
            input('Error : Wrong choice. Press ENTER to go back.')