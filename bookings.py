from validations import check_valid_menu_choise,check_activity,check_players
from inputs import get_name,get_room_id,get_date,get_start_time,get_players,get_enter,get_order_id
from manage_rooms import find_room_by_id
from storage import save_bookings
from helpers import get_next_booking_id,check_weekday,check_collision,check_time,change_type_time_date
from helpers import get_ready_for_json,find_order_by_data,show_update_menu,insure_cancel
from helpers import calc_cancellation_fee,check_cancelling_time

def show_booking_menu():
    while True:
        choise = input("""
1. Create new order
2. Show all orders
3. Find order by id
4. Show order by costumer
5. Show orders by date
6. Update order
7. Cancel oreder

Choose option: """)
        if check_valid_menu_choise(choise,["1","2","3","4","5","6","7"]):
            return choise
        print("Not valid choise\n\n")

# option 1 create new order


def create_order(booking_id,customer_name,room_id,booking_date,start_time,players):
    return     {
        "booking_id": booking_id,
        "customer_name": customer_name,
        "room_id": room_id,
        "booking_date": booking_date,
        "start_time": start_time,
        "players":players,
    }

def calc_subtotal(room,order):
        return int(room["price_per_player"]) * int(order["players"])

def calc_discount(price,players):
    if players <= 4:
        return price
    elif players < 7:
        return price - price / 100 * 10
    elif players >= 7:
        return price - price / 100 * 15 

def get_weekend_price(price):
    return price + price / 100 * 15
    
def add_price_to_order(order,price):
    order["total_price"] = round(price,2)
    order["status"] = "Active"
    order["cancellation_fee"] = 0.0



def run_create_order(bookings:list,rooms):
    if bookings:
        bookings = change_type_time_date(bookings)
    booking_id = get_next_booking_id(bookings)
    customer_name = get_name()
    room_id = get_room_id()
    room = find_room_by_id(rooms,room_id)
    if not room:
        print("\nRoom not found\n")
        return 
    if not check_activity(rooms,room_id):
        print("\nRoom is not active\n")
        return
    if not rooms:
        print("\nNo roons yet! ")
        return
    booking_date = get_date()
    start_time = get_start_time()
    if check_time(room,start_time):
        if bookings:
            if not check_collision(bookings,room,start_time,booking_date,booking_id):
                print("\nNot valid time, could cause a collision\n\n")
                return
        players = get_players()
        if check_players(room,int(players)):
            booking = create_order(booking_id,customer_name,room_id,booking_date,start_time,players)
            subtotal = calc_subtotal(room,booking)
            total_price = calc_discount(subtotal,int(booking["players"]))
            if check_weekday(booking_date,start_time):
                price = get_weekend_price(total_price)
            else:
                price = total_price
            add_price_to_order(booking,price)
        else:
            print("\nNot valid players number\n")
            return
    else:
        print("\nNot valid time - must end by 22:00 and start from 10:00\n")
        return
    if bookings:
        for order in bookings:
            get_ready_for_json(order)
    get_ready_for_json(booking)
    bookings.append(booking)
    save_bookings(bookings)
    print("\n------ ORDER ADDED SUCCESSFULLY ------\n")

# option 2 show all orders

def show_all_orders(bookings):
    if bookings:
        for booking in bookings:
            print(f"{booking}\n")
    else:
        print("\nNo bookings found\n\n")

# option 3 find order by id

def run_find_order_by_id(bookings):
    order_id = get_order_id()
    order = find_order_by_data(bookings,"booking_id",order_id)
    if order:
        print(f"\n{order}\n\n")
    else:
        print("\nOrder not found\n\n")

# option 4 find order by cystomer name

def run_find_order_by_customer(bookings):
    name = get_name()
    order = find_order_by_data(bookings,"customer_name",name)
    if order:
        print(f"\n{order}\n\n")
    else:
        print("\nOrder not found\n\n")

# option 5 show order by date

def show_orders_by_date(bookings):
    sorted_orders = sorted(bookings,key=lambda b: b["booking_date"])
    print("\n\n".join(map(str,sorted_orders)))

# option 6 update order 

def run_update_order(bookings,rooms):
    if not bookings:
        print("No bookings yet!")
        return
    bookings = change_type_time_date(bookings)
    booking_id = get_order_id()
    order = find_order_by_data(bookings,"booking_id",booking_id)
    if not order:
        print("\nOrder not found\n\n")
        return
    if not check_activity(rooms,order["room_id"]):
        print("\nRoom is not active\n")
        return
    room = find_room_by_id(rooms,order["room_id"])
    choise = show_update_menu()
    if choise == "1":
        booking_date = get_date()
        order["booking_date"] = booking_date
    elif choise == "2":
        start_time = get_start_time()
        if not check_time(room,start_time):
            print("\nNot valid time - must end by 22:00 and start from 10:00\n\n")
            return
        order["start_time"] = start_time
    elif choise == "3":
        players = get_players()
        if not check_players(room,int(players)):
            print("\nNot valid players number\n")
            return
        order["players"] = players
    subtotal = calc_subtotal(room,order)
    total_price = calc_discount(subtotal,int(order["players"]))
    if check_weekday(order["booking_date"],order["start_time"]):
        price = get_weekend_price(total_price)
    else:
        price = total_price
    add_price_to_order(order,price)

    if not check_collision(bookings,room,order["start_time"],order["booking_date"],order["booking_id"]):
        print("\nnNot valid time, could cause a collision\n\n")
        return
    for booking in bookings:
        get_ready_for_json(booking)
    save_bookings(bookings)
    print("\n\n------------- THE ORDER UPDATED SUCCESSFULLY -------------\n\n")

# option 7 cancel order

def change_cancellation_fee(order,fee):
    order["cancellation_fee"] = round(fee,2)

def run_cancel_order(bookings):
    bookings = change_type_time_date(bookings)
    order_id = get_order_id()
    order = find_order_by_data(bookings,"booking_id",order_id)
    if not order:
        print("\nOrder not found\n\n")
        return
    if not check_cancelling_time(order):
        print("\nCan not cancel the order, time over!\n\n")
        return
    if order["status"] != "Active":
        print("The order is already cancelled!")
        return
    choise = insure_cancel()
    if choise == "1":
        print("\n---- your booking is safe! ----")
    elif choise == "2":
        order["status"] = "Cancelled"
        cancellation_fee = calc_cancellation_fee(order)
        change_cancellation_fee(order,cancellation_fee)
        for booking in bookings:
            get_ready_for_json(booking)
        save_bookings(bookings)
        print("\n------------- THE ORDER CANCELD SUCCESSPULLY -------------\n\n")