# railway-reservation-system

total_seats = 50
available_seats = total_seats
bookings = {}

def check_availability():
    print("\nAvailable Seats:", available_seats)

def book_ticket():
    global available_seats

    if available_seats <= 0:
        print("\nNo seats available!")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    booking_id = len(bookings) + 1
    seat_no = total_seats - available_seats + 1

    bookings[booking_id] = {
        "name": name,
        "age": age,
        "seat_no": seat_no
    }

    available_seats -= 1

    print("\nTicket Booked Successfully!")
    print("Booking ID:", booking_id)
    print("Seat Number:", seat_no)

def view_ticket():
    booking_id = int(input("Enter Booking ID: "))

    if booking_id in bookings:
        ticket = bookings[booking_id]
        print("\n--- Ticket Details ---")
        print("Name:", ticket["name"])
        print("Age:", ticket["age"])
        print("Seat No:", ticket["seat_no"])
    else:
        print("\nBooking not found!")

def cancel_ticket():
    global available_seats

    booking_id = int(input("Enter Booking ID to cancel: "))

    if booking_id in bookings:
        del bookings[booking_id]
        available_seats += 1
        print("\nTicket Cancelled Successfully!")
    else:
        print("\nBooking ID not found!")

while True:
    print("\n===== Ticket Booking System =====")
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
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
