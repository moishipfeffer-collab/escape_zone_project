from validations import check_valid_menu_choise
from helpers import show_actvie_or_cancelled_orders,show_income,change_type_time_date
from inputs import get_date,get_room_id
def report_menu():
    print("\n-------------- REPORTS MANAGEMENT --------------\n")
    valid = False
    while not valid:
        choise = input("""
1. Show all active orders
2. Show all canceld orders
3. Show income from actvie orders
4. Show cancellation fee
5. Show the populare room 
6. Show number of orders per-room
7. The occupancy rate of room by date

Coose an option:  """)
        if check_valid_menu_choise(choise,["1","2","3","4","5","6","7"]):
            return choise
        print("\nNot valid choise\n\n")

# option 1 show active orders

def show_active_orders(bookings):
    if not bookings:
        print("No orders yet!")
    else:
        show_actvie_or_cancelled_orders(bookings)

#option 2 show cancelled orders

def show_cancelled_orders(bookings):
    if not bookings:
        print("No orders yet!")
    else:
        show_actvie_or_cancelled_orders(bookings,"cancelled")

# option 3 show income

def show_active_income(bookings):
    if not bookings:
        print("No orders yet!")
    else:
        count = show_income(bookings,"active")
        print(f"\nThe total income from active orders is: {count}\n\n")

# option 4 show cancellation fee

def show_cancellation_fee(bookings):
    if not bookings:
        print("No orders yet!")
    else:
        count = show_income(bookings)
        print(f"\nThe total income from cancellation fee is: {count}\n\n")

# option 5 most popular room

def show_popular_room(rooms,bookings):
    if not bookings:
        print("No orders yet!")
    else:
        highest = 0
        for room in rooms:
            count = 0
            for order in bookings:
                if order["room_id"] == room["room_id"]:
                    count += 1
                    if count > highest:
                        highest = count
                        room_id = room["room_id"]
        print(f"\n\nThe most popular room is: room {room_id} with {highest} orders\n\n")

# option 6 orders number per-room

def show_orders_per_room(bookings):
    if not bookings:
        print("No orders yet!")
    else:
        orders_per_rooms = {}
        for order in bookings:
            room_id = order["room_id"]
            if room_id not in orders_per_rooms:
                orders_per_rooms[room_id] = 1
            else:
                orders_per_rooms[room_id] += 1
        for name,value in orders_per_rooms.items():
            print(f"\nroom {name}: {value} orders")
        print()

# option 7 show occupancy rate of a room by date

def occupancy_rate_by_date(bookings,rooms):
    if not bookings:
        print("No orders yet!")
    else:
        bookings = change_type_time_date(bookings)
        count = 0
        date = get_date()
        room_id = get_room_id()
        for order in bookings:
            if order["booking_date"] == date:
                if order["room_id"] == room_id:
                    for room in rooms:
                        if room["room_id"] == room_id:
                            count += int(room["duration"]) + 15
        print(f"\nThe occupancy rate on {date} is {round(count / (12 * 60) * 100,2)} %\n\n")

