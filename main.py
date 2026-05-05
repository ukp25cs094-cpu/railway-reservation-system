import random

total_seats = 50
available_seats = total_seats
reservations = {}


def check_availability():
    print("\n----- Seat Availability -----")
    print("Available Seats:", available_seats)


def book_ticket():
    global available_seats

    if available_seats == 0:
        print("\nSorry! No seats available.")
        return

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))

    booking_id = "B" + str(random.randint(1000, 9999))

    while booking_id in reservations:
        booking_id = "B" + str(random.randint(1000, 9999))

    seat_number = total_seats - available_seats + 1

    reservations[booking_id] = {
        "name": name,
        "age": age,
        "seat": seat_number
    }

    available_seats -= 1

    print("\nTicket booked successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat_number)


def view_ticket():
    booking_id = input("\nEnter Booking ID: ")

    if booking_id in reservations:
        ticket = reservations[booking_id]
        print("\n----- Ticket Details -----")
        print("Name:", ticket["name"])
        print("Age:", ticket["age"])
        print("Seat Number:", ticket["seat"])
        print("Booking ID:", booking_id)
    else:
        print("Booking not found.")


def cancel_ticket():
    global available_seats

    booking_id = input("\nEnter Booking ID to cancel: ")

    if booking_id in reservations:
        del reservations[booking_id]
        available_seats += 1
        print("Ticket cancelled successfully!")
    else:
        print("Booking ID not found.")


while True:
    print("\n===== Railway Reservation System =====")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        check_availability()
    elif choice == "2":
        book_ticket()
    elif choice == "3":
        view_ticket()
    elif choice == "4":
        cancel_ticket()
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Try again.")
