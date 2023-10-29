import os

#print("Current directory:", os.getcwd())
import csv

# Define user roles and their corresponding passwords
users = {
    "admin": "admin_password",# Set the password for the admin role
    "staff": "staff_password",
}

# Sets the user roles as None
user_role = None


### BEGINNING OF CONTROLS ###
##

#!!!FOR CHOICE 01: MANAGE STAFF!!!
# Initialize the CSV file for staff records
STAFF_CSV_FILE = "staff.csv"

# Load staff records from the CSV file
def load_staff_records():
    staff_records = []
    try:
        with open(STAFF_CSV_FILE, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                staff_records.append(row)
    except FileNotFoundError:
        print(f"{STAFF_CSV_FILE} not found. Please make sure the file exists.")
    return staff_records


# Save staff records to the CSV file
def save_staff_records(staff_records):
    with open(STAFF_CSV_FILE, "w", newline="") as file:
        fieldnames = ["Roll Number", "Name", "Role", "Department"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(staff_records)


# Staff Management
def manage_staff():
    staff_records = load_staff_records()  # Load existing staff records
    
    while True:
        print("_"*109)
        print(" "*15)
        print(" "*40,"STAFF MANAGEMENT MENU")
        print("_"*109)
        print(" "*109)
        print("1) Add Staff Member")
        print("2) View Staff List")
        print("3) Delete Staff Member")
        print("4) Exit")
        print(" "*109)
        choice = input("Enter your choice: ")

        if choice == "1":
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Staff Member's Name: ")
            role = input("Enter Staff Member's Role: ")
            department = input("Enter Staff Member's Department: ")

            # Create a staff record as a dictionary
            staff_member = {
                "Roll Number": roll_number,
                "Name": name,
                "Role": role,
                "Department": department,
            }

            staff_records.append(staff_member)  # Add the staff member to the list

            print("Staff member added successfully!")

        elif choice == "2":
            if not staff_records:
                print("No staff members found.")
            else:
                print("_"*109)
                print(" "*15)
                print(" STAFF LIST:")
            for staff in staff_records:
                    print(" "*15)
                    print(
                        f" ROLL NUMBER: {staff['Roll Number']}\n NAME: {staff['Name']}\n ROLE: {staff['Role']}\n DEPARTMENT: {staff['Department']}\n"
                    )

        elif choice == "3":
            roll_number_to_delete = input(
                "Enter the Roll Number of the staff member to delete: "
            )
            records_before_deletion = len(staff_records)
            staff_records = [
                staff
                for staff in staff_records
                if staff["Roll Number"] != roll_number_to_delete
            ]
            records_after_deletion = len(staff_records)

            if records_before_deletion == records_after_deletion:
                print(
                    f"Staff member with Roll Number {roll_number_to_delete} not found. Please try again."
                )
            else:
                print(
                    f"Staff member with Roll Number {roll_number_to_delete} deleted successfully."
                )

        elif choice == "4":
            save_staff_records(staff_records)  # Save records to the CSV file
            break

        else:
            print("Invalid choice. Please try again.")
            
            
#!!!FOR CHOICE 02 INPUT FLIGHT INFORMATION!!!
# Initialize CSV files for arrival and departure flights
DEPARTURE_CSV_FILE = "departure_flights.csv"
ARRIVAL_CSV_FILE = "arrival_flights.csv"

# Load flight records from the CSV file
def load_flight_data(csv_file):
    flight_data = []
    try:
        with open(csv_file, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                flight_data.append(row)
    except FileNotFoundError:
        print(f"{csv_file} not found. Please make sure the file exists.")
    return flight_data


# Save flight records to the CSV file
def save_flight_data(flight_data, csv_file):
    with open(csv_file, "w", newline="") as file:
        fieldnames = [
            "TIME",
            "DESTINATION",
            "FLIGHT #",
            "AIRLINE",
            "TERMINAL",
            "GATE",
            "STATUS",
        ]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(flight_data)

# Function to display flight list for departure or arrival
def display_flight_list(csv_file):
    flights = load_flight_data(csv_file)
    
    for flight in flights:
        print(f" FLIGHT: {flight['FLIGHT #']}\n AIRLINE: {flight['AIRLINE']}\n DEPARTURE: {flight['TIME']}\n GATE:{flight['GATE']}\n"
        )


# Function to input flight information for departure or arrival
def input_flight_information(csv_file, status):
    flight_data = load_flight_data(csv_file)

    time = input(f"Enter TIME for {status}: ")
    destination = input(f"Enter DESTINATION for {status}: ")
    flight_number = input(f"Enter FLIGHT # for {status}: ")
    airline = input(f"Enter AIRLINE for {status}: ")
    terminal = input(f"Enter TERMINAL for {status}: ")
    gate = input(f"Enter GATE for {status}: ")
    flight_status = input(f"Enter STATUS for {status}: ")

    # Create a flight record as a dictionary
    flight_record = {
        "TIME": time,
        "DESTINATION": destination,
        "FLIGHT #": flight_number,
        "AIRLINE": airline,
        "TERMINAL": terminal,
        "GATE": gate,
        "STATUS": flight_status,
    }

    flight_data.append(flight_record)  # Add the flight record to the list
    save_flight_data(flight_data, csv_file)  # Save the updated data
    
def main():
    while True:
        print("_"*109)
        print(" "*15)
        print(" "*45,"FLIGHT INFORMATION MENU")
        print("_"*109)
        print(" "*15)
        print("1) Input Departure Flight Information")
        print("2) Input Arrival Flight Information")
        print("3) View Flight Information")
        print("4) Exit")
        print(" "*15)
        choice = input("Enter your choice: ")
        print(" "*15)

        if choice == "1":
            input_flight_information(DEPARTURE_CSV_FILE, "Departure")
        elif choice == "2":
            input_flight_information(ARRIVAL_CSV_FILE, "Arrival")
        elif choice == "3":
            print("\nDEPARTURE FLIGHTS:")
            print(" "*15)
            display_flight_list(DEPARTURE_CSV_FILE)
            print("\nARRIVAL FLIGHTS:")
            print(" "*15)
            display_flight_list(ARRIVAL_CSV_FILE)
        else:
            break
        

#!!!FOR CHOICE 03: AIRCRAFT AVAILABILITY/ RESERVATIONS!!!
# CSV file for aircraft availability

# Constants for CSV files
AIRCRAFT_CSV_FILE = "aircraft.csv"

# Load aircraft data from the CSV file
def load_aircraft_data():
    aircraft_data = []
    try:
        with open(AIRCRAFT_CSV_FILE, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                aircraft_data.append(row)
    except FileNotFoundError:
        print(f"{AIRCRAFT_CSV_FILE} not found. Please make sure the file exists.")
    return aircraft_data


# Save aircraft data to the CSV file
def save_aircraft_data(aircraft_data):
    with open(AIRCRAFT_CSV_FILE, "w", newline="") as file:
        fieldnames = ["Aircraft ID", "Name", "Type", "Available", "Reservation"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(aircraft_data)


# Function to display available aircraft
def display_available_aircraft():
    aircraft = load_aircraft_data()
    print("AVAILABLE AIRCRAFT:")
    print(" "*15)
    for a in aircraft:
        if a["Available"] == "1":
            print(
                f" AIRCRAFT ID: {a['Aircraft ID']}\n NAME: {a['Name']}\n TYPE: {a['Type']}\n"
            )


# Function to make a reservation for an aircraft
def make_reservation(aircraft_id):
    aircraft_data = load_aircraft_data()

    for a in aircraft_data:
        if a["Aircraft ID"] == aircraft_id:
            if a["Available"] == "1":
                a["Available"] = "0"
                a["Reservation"] = "1"
                save_aircraft_data(aircraft_data)
                print(f"Aircraft ID {aircraft_id} reserved successfully.")
                return
            else:
                print(f"Aircraft ID {aircraft_id} is not available.")
                return

    print(f"Aircraft ID {aircraft_id} not found.")


# Function to cancel a reservation
def cancel_reservation(aircraft_id):
    aircraft_data = load_aircraft_data()

    for a in aircraft_data:
        if a["Aircraft ID"] == aircraft_id:
            if a["Reservation"] == "1":
                a["Available"] = "1"
                a["Reservation"] = "0"
                save_aircraft_data(aircraft_data)
                print(
                    f"Reservation for Aircraft ID {aircraft_id} canceled successfully."
                )
                return
            else:
                print(f"Aircraft ID {aircraft_id} does not have a reservation.")
                return

    print(f"Aircraft ID {aircraft_id} not found.")


# Initialize the CSV file for aircraft records with sample data
def initialize_aircraft_csv():
    with open(AIRCRAFT_CSV_FILE, "w", newline="") as file:
        fieldnames = ["Aircraft ID", "Name", "Type", "Available", "Reservation"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        sample_data = [
            {
                "Aircraft ID": "1",
                "Name": "Boeing 737",
                "Type": "Commercial",
                "Available": "5",
                "Reservation": "1",
            },
            {
                "Aircraft ID": "2",
                "Name": "Airbus A320",
                "Type": "Commercial",
                "Available": "6",
                "Reservation": "2",
            },
            {
                "Aircraft ID": "3",
                "Name": "Cessna 172",
                "Type": "Private",
                "Available": "1",
                "Reservation": "0",
            },
            {
                "Aircraft ID": "4",
                "Name": "Embraer E190",
                "Type": "Commercial",
                "Available": "0",
                "Reservation": "1",
            },
            {
                "Aircraft ID": "5",
                "Name": "Boeing 747",
                "Type": "Commercial",
                "Available": "3",
                "Reservation": "0",
            },
        ]
        csv_writer.writerows(sample_data)
        
# Aircraft Reservation Menu
def aircraft_menu():
    if __name__ == "__main__":
        initialize_aircraft_csv()
        while True:
            print("_"*109)
            print(" "*15)
            print(" "*40,"AIRCRAFT RESERVATION MENU")
            print("_"*109)
            print(" "*15)
            print("1) Display Available Aircraft")
            print("2) Make a Reservation")
            print("3) Cancel a Reservation")
            print("4) Exit")
            print(" "*15)
            choice = input("Enter your choice: ")
            print(" "*15)

            if choice == "1":
                display_available_aircraft()
            elif choice == "2":
                aircraft_id = input("Enter Aircraft ID for reservation: ")
                make_reservation(aircraft_id)
            elif choice == "3":
                aircraft_id = input("Enter Aircraft ID to cancel reservation: ")
                print(" "*15)
                cancel_reservation(aircraft_id)
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")
                
                
#!!! FOR CHOICE 04: AIRCRAFT DATABASE !!!###
# Initialize the aircraft CSV file with sample data
AIRCRAFT_CSV_FILE = "aircraft_database.csv"
initial_data = [
    {"Aircraft ID": "1", "Airline": "Indigo", "Days at Airport": "5"},
    {"Aircraft ID": "2", "Airline": "AirlineX", "Days at Airport": "1"},
    {"Aircraft ID": "3", "Airline": "Jet Airways", "Days at Airport": "10"},
    {"Aircraft ID": "4", "Airline": "Emirates", "Days at Airport": "2"},
    {"Aircraft ID": "5", "Airline": "Lufthansa", "Days at Airport": "6"},
    {"Aircraft ID": "6", "Airline": "British Airways", "Days at Airport": "3"},
    {"Aircraft ID": "7", "Airline": "Air France", "Days at Airport": "7"},
]


def initialize_aircraft_database():
    with open(AIRCRAFT_CSV_FILE, "w", newline="") as file:
        fieldnames = [
            "Aircraft ID",
            "Airline",
            "Days at Airport",
            "Last Maintenance Day",
        ]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(initial_data)


def add_aircraft_data():
    aircraft_data = []
    with open(AIRCRAFT_CSV_FILE, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            aircraft_data.append(row)
    return aircraft_data


def update_aircraft_days(aircraft_id, days):
    aircraft_data = load_aircraft_data()
    for aircraft in aircraft_data:
        if aircraft["Aircraft ID"] == aircraft_id:
            aircraft["Days at Airport"] = str(days)
    save_aircraft_data(aircraft_data)


def preserve_aircraft_data(aircraft_data):
    with open(AIRCRAFT_CSV_FILE, "w", newline="") as file:
        fieldnames = [
            "Aircraft ID",
            "Airline",
            "Days at Airport",
            "Last Maintenance Day",
        ]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(aircraft_data)


def calculate_daily_charges(airline, days):
    daily_rates = {
        "Indigo": 2000,
        "AirlineX": 1500,
        "Jet Airways": 2500,
        "Emirates": 3500,
        "Lufthansa": 1800,
        "British Airways": 2300,
        "Air France": 2700,
    }
    return daily_rates.get(airline, 0) * days


def calculate_landing_charges(airline):
    landing_charges = {
        "Indigo": 5000,
        "AirlineX": 4000,
        "Jet Airways": 6000,
        "Emirates": 8000,
        "Lufthansa": 4500,
        "British Airways": 5000,
        "Air France": 5500,
    }
    return landing_charges.get(airline, 0)


def check_maintenance_schedule(aircraft_id):
    aircraft_data = load_aircraft_data()
    for aircraft in aircraft_data:
        if aircraft["Aircraft ID"] == aircraft_id:
            days_at_airport = int(aircraft["Days at Airport"])
            last_maintenance_day = aircraft["Last Maintenance Day"]

            if last_maintenance_day:
                last_maintenance_day = int(last_maintenance_day)
            else:
                last_maintenance_day = 0

            if days_at_airport - last_maintenance_day >= 30:
                print(f"Aircraft {aircraft_id} needs maintenance.")
            else:
                print(f"Aircraft {aircraft_id} is within the maintenance schedule.")


def generate_airline_charges_report(airline_name):
    aircraft_data = load_aircraft_data()
    total_landing_charge = 0
    total_daily_charge = 0

    for aircraft in aircraft_data:
        if aircraft["Airline"] == airline_name:
            days_at_airport = int(aircraft["Days at Airport"])
            landing_charge = calculate_landing_charges(airline_name)
            daily_charge = calculate_daily_charges(airline_name, days_at_airport)
            total_landing_charge += landing_charge
            total_daily_charge += daily_charge

    print(f"Airline: {airline_name}")
    print(f"Total Landing Charges: ${total_landing_charge}")
    print(f"Total Daily Charges: ${total_daily_charge}")
    print(f"Total Charges: ${total_landing_charge + total_daily_charge}")


def aircraft_charges():
    if __name__ == "__main__":
        initialize_aircraft_database()
        aircraft_id = input("Enter Aircraft ID: ")
        days = int(input("Enter the number of days: "))

        update_aircraft_days(aircraft_id, days)
        check_maintenance_schedule(aircraft_id)
        generate_airline_charges_report(
            input("Enter Airline Name for Charges Report: ")
      )

def add_flight_data(csv_file):
    flight_data = []
    try:
        with open(csv_file, "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                flight_data.append(row)
    except FileNotFoundError:
        print(f"{csv_file} not found. Please make sure the file exists.")
    return flight_data


#Display departure screen
DEPARTURE_CSV_FILE = "departure_flights.csv"

def display_departure_screen(csv_file):
    flight= add_flight_data(csv_file)
    try:
        reader=csv.DictReader(flight)
        print("_"*109)
        print(" ")
        print(" "*40,"DEPARTURE FLIGHTS:")
        print("_"*109)

        for row in reader:
            dep_time= row[0]
            flight_number= row[1]
            destination= row[2]
            airline= row[3]
            terminal= row[4]
            gate= row[5]
                  
            print(f" TIME: {dep_time} | FLIGHT NUMBER: {flight_number} | DESTINATION: {destination} | AIRLINE: {airline} | TERMINAL: {terminal} | GATE: {gate}")
                  
    except FileNotFoundError:
            print("No departure flights found.")
            return


def select_user():
    global user_role
    a1="="*109
    s1=" "
    print(a1)
    print(s1)
    print(" "*40,"AIRPORT MANAGMENT SYSTEM")
    print(s1)
    print(a1)
    print(s1)
    print("1) Admin")
    print("2) Staff")
    print(" ")
    choice = int(input("Enter designated position (in numbers):"))

    if choice == 1:
        print(" ")
        password = input("Enter Password:")
        if (
            password == users["admin"]
        ):  # if the password matches to the one given in user
            user_role = (
                "admin"  # sets the role as admin giving admin permissions to the user
            )
        else:
            print("Invalid Password! Please try again")

    elif choice == 2:
        password = input("Enter password:")
        if password == users["staff"]:
            user_role = "staff"
        else:
            print("Invalid Password! Please try again!")


if __name__ == "__main__":
    select_user()  # Authenticate the user role

    ### A D M I N   C O N T R O L S ###
    if user_role == "admin":
        while True:
            g2=" "
            print("_"*109)
            print(g2)
            print(" "*50,"ADMIN MENU")
            print("_"*109)
            print(g2)
            print("1) Manage Staff")
            print("2) Input/Display Flight Information")
            print("3) Aircraft Reservation")
            print("4) Aircraft Charges")
            print("5) Departure")
            print(g2)
            choice = input("Enter your choice: ")
            print(g2)
            
            if choice == "1":
                manage_staff()
            elif choice == "2":
                main()
            elif choice == "3":
                aircraft_menu()
            elif choice == "4":
                aircraft_charges()
            elif choice == "5":
                display_departure_screen(DEPARTURE_CSV_FILE)
            else:
                print("Invalid choice. Please try again.")
                break

        



