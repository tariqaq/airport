globalCenter = 100

def main():
    
    while True:
        print('-'*100)
        print()
        print('AIRPORT MANAGEMENT SYSTEM'.center(globalCenter))
        print()
        print('-'*100)
        
        print('1. Flight Information\n'
            '2. Aircraft Reservation\n'
            '3. Aircraft Charges\n'
            '4. Departure (?__?)\n'
            '5. Exit')
        usrChoice = int(input('Enter choice : '))
        
        if usrChoice == 1:
            
            #flightInfMain()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 2 :
            
            #reserveMain()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 3 :
            
            #chargesMain()
            
            input('---Press ENTER to go back.')
            
        elif usrChoice == 4 :
            
            #departure()
            
            input('---Press ENTER to go back.')

        elif usrChoice == 5 :
            
            print('---Exiting Program.---')
            
            break
        
        else:
            input('Error : Wrong choice. Press ENTER to go back.')
            
main()