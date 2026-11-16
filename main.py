from storage import load_json_rooms,load_json_bookings
from run_program import show_menu,manage_rooms,booking_management,reports_management
from helpers import clean_terminal

def main():
    rooms = load_json_rooms()
    bookings = load_json_bookings() 
    if rooms == False or bookings == False:
        return 
    valid = False
    while not valid: 
        clean_terminal()
        choise = show_menu()
        if choise == "1":
            clean_terminal()
            manage_rooms(rooms)
        elif choise == "2":
            clean_terminal()
            booking_management(bookings,rooms)
        elif choise == "3":
            clean_terminal()
            reports_management(bookings,rooms)
        elif choise == "4":
            break

if __name__ == "__main__":
    main()

