from validations import check_valid_menu_choise
from manage_rooms import show_rooms_menu,show_all_rooms,run_show_room_details
from manage_rooms import run_add_new_room,run_update_room,chang_active
from inputs import get_enter
from bookings import show_booking_menu,run_create_order,show_all_orders,run_find_order_by_id
from bookings import run_find_order_by_customer,show_orders_by_date,run_update_order,run_cancel_order
from helpers import clean_terminal
from reports import report_menu,show_active_income,show_cancellation_fee,show_active_orders
from reports import show_cancelled_orders,show_popular_room,show_orders_per_room,occupancy_rate_by_date
def show_menu():
    while True:
        print("\n=========================")
        print(" WELCOME TO ESCAPE ZONE")
        print("=========================\n")
        choise = input("""
1. Rooms management 
2. Booking management
3. Reports
4. Exit

Choose an option: """)
        if check_valid_menu_choise(choise,["1","2","3","4"]):
            return choise
        print("Not valid choise")

# option 1 mannage rooms

def manage_rooms(rooms):
    choise = show_rooms_menu()
    if choise == "1":
        clean_terminal()
        show_all_rooms(rooms)
        get_enter()
    elif choise == "2":
        clean_terminal()
        run_show_room_details(rooms)
        get_enter()
    elif choise == "3":
        clean_terminal()
        run_add_new_room(rooms)
        get_enter()
    elif choise == "4":
        clean_terminal()
        run_update_room(rooms)
        get_enter()
    elif choise == "5":
        clean_terminal()
        chang_active(rooms)
        get_enter()

# option 2 booking management 

def booking_management(bookings,rooms):
    print("\n----------- ORDER MANEGEMENT -----------\n\n")
    choise = show_booking_menu()
    if choise == "1":
        clean_terminal()
        run_create_order(bookings,rooms)
        get_enter()
    elif choise == "2":
        clean_terminal()
        show_all_orders(bookings)
        get_enter()
    elif choise == "3":
        clean_terminal()
        run_find_order_by_id(bookings)
        get_enter()
    elif choise == "4":
        clean_terminal()
        run_find_order_by_customer(bookings)
        get_enter()
    elif choise == "5":
        clean_terminal()
        show_orders_by_date(bookings)
        get_enter()
    elif choise == "6":
        clean_terminal()
        run_update_order(bookings,rooms)
        get_enter()
    elif choise == "7":
        clean_terminal()
        run_cancel_order(bookings)
        get_enter()

# option 3 reports

def reports_management(bookings,rooms):
        choise = report_menu()
        if choise == "1":
            clean_terminal()
            show_active_orders(bookings)
            get_enter()
        elif choise == "2":
            clean_terminal()
            show_cancelled_orders(bookings)
            get_enter()
        elif choise == "3":
            clean_terminal()
            show_active_income(bookings)
            get_enter()
        elif choise == "4":
            clean_terminal()
            show_cancellation_fee(bookings)
            get_enter()
        elif choise == "5":
            clean_terminal()
            show_popular_room(bookings,rooms)
            get_enter()
        elif choise == "6":
            clean_terminal()
            show_orders_per_room(bookings)
            get_enter()
        elif choise == "7":
            clean_terminal()
            occupancy_rate_by_date(bookings,rooms)
            get_enter()