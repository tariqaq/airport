from flightinf import *
from staff import *

globalCenter = 100

def main():
    
    while True:
        print('-'*100)
        print()
        print('AIRPORT MANAGEMENT SYSTEM'.center(globalCenter))
        print()
        print('-'*100)
        
        print('1. Flight Information\n'
            '2. Staff Management\n'
            '3. Exit')
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            
            flightInfMain()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 2 :
            
            staffMain()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 3 :
            
            break

        else:
            input('Error : Wrong choice. Press ENTER to go back.')
            
main()