class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        return False


class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:
    def __init__(self, username="admin", password="1234"):
        self.username = username
        self.password = password

    def login(self):
        print("Admin Login")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == self.username and password == self.password:
            print("Login successful")
            return True
        else:
            print("Invalid username or password")
            return False


class BusSystem:
    Fare = 500

    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin()

    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None

    def add_bus(self, number, route, seats):
        if self.find_bus(number):
            print("Bus with this number already exists")
            return
        if seats <= 0:
            print("Total seats must be a positive number")
            return
        bus = Bus(number, route, seats)
        self.buses.append(bus)
        print("Bus added successfully")

    def book_ticket(self, bus_number, name, phone):
        if not name:
            print("Passenger name cannot be empty")
            return
        if not phone:
            print("Passenger phone cannot be empty")
            return
        bus = self.find_bus(bus_number)
        if not bus:
            print("Bus not found")
            return
        if bus.available_seats() <= 0:
            print("No seats available on this bus")
            return
        if bus.book_seat():
            passenger = Passenger(name, phone, bus)
            self.passengers.append(passenger)
            seat_no = bus.booked_seats
            print("Ticket booked successfully")
            print("-------Ticket Details---------")
            print(f"Name: {passenger.name}")
            print(f"Phone: {passenger.phone}")
            print(f"Bus Number: {bus.number}")
            print(f"Route: {bus.route}")
            print(f"Seat No: {seat_no}")
            print(f"Fare: ৳{self.Fare}")
            print("")
        else:
            print("Unable to book seat")

    def show_buses(self):
        if not self.buses:
            print("No buses available in the system")
            return
        print("----------Available Buses---------")
        for bus in self.buses:
            print(f"Bus Number: {bus.number}, Route: {bus.route}, Total Seats: {bus.total_seats}, Available Seats: {bus.available_seats()}")
        print("")


def admin_menu(system):
    while True:
        print("Admin Menu")
        print("1.Add Bus")
        print("2.View All Buses")
        print("3.Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            number = input("Enter bus number: ")
            route = input("Enter route: ")
            while True:
                seats_input = input("Enter total seats: ")
                if not seats_input.isdigit():
                    print("Please enter a valid positive number for seats")
                else:
                    seats = int(seats_input)
                    if seats <= 0:
                        print("Seats must be greater than zero")
                    else:
                        break
            system.add_bus(number, route, seats)
        elif choice == "2":
            system.show_buses()
        elif choice == "3":
            print("Logged out from admin account")
            break
        else:
            print("Invalid choice, please try again")


def main():
    system = BusSystem()
    while True:
        print()
        print("Bangladesh Bus Ticket Booking System")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            if system.admin.login():
                admin_menu(system)
        elif choice == "2":
            if not system.buses:
                print("No buses available. Please contact admin to add buses first")
                continue
            bus_number = input("Enter bus number: ")
            name = input("Enter passenger name: ")
            phone = input("Enter passenger phone: ")
            system.book_ticket(bus_number, name, phone)
        elif choice == "3":
            system.show_buses()
        elif choice == "4":
            print("Thank you for using the Bus Ticket Booking System")
            break
        else:
            print("Invalid choice, please try again")
main()
