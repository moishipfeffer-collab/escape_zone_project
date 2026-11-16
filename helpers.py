from validations import check_valid_menu_choise
from datetime import time,date,datetime,timedelta
import os
def get_next_booking_id(bookings):
    if bookings:
        latest_booking = max(bookings,key=lambda b: b["booking_id"][1:])
        latest_id = int(latest_booking["booking_id"][1:])
        return "B" + str(latest_id+1).zfill(3)
    return "B001"

def check_time(room,start_time,start_date = date.today()):
    minutes = int(room["duration"])
    closing_time = datetime.combine(start_date,time(hour=22))
    opening_time = datetime.combine(start_date,time(hour=10))
    start_datetime = datetime.combine(start_date,start_time)
    if start_datetime + timedelta(minutes=minutes) <= closing_time and start_datetime >= opening_time:
        return True
    return False
    

def check_collision(bookings,room,start_time,booking_date,order_id):
    minutes = int(room["duration"]) + 15
    for booking in bookings:
        if booking["room_id"] == room["room_id"]:
            if booking["booking_date"] == booking_date and booking["booking_id"] != order_id and booking["status"] == "Active":
                start_datetime = datetime.combine(booking_date,start_time)
                booking_datetime = datetime.combine(booking_date,booking["start_time"])
                datetime_game_plus = start_datetime + timedelta(minutes=minutes)
                datetime_game_minus = start_datetime - timedelta(minutes=minutes)
                if booking_datetime > start_datetime and datetime_game_plus > booking_datetime or booking_datetime < start_datetime and datetime_game_minus < booking_datetime:
                    return False
    return True 

def check_weekday(date,time):
    datetime_start = datetime.combine(date,time)
    if int(datetime_start.weekday()) in [4,5]:
        return True
    return False

def change_type_time_date(bookings):
    for booking in bookings:
        year = int(booking["booking_date"][:4])
        month = int(booking["booking_date"][5:7])
        day = int(booking["booking_date"][8:])
        hour = int(booking["start_time"][:2])
        minute = int(booking["start_time"][3:5])
        booking_date = date(year=year,month=month,day=day)
        start_time = time(hour=hour,minute=minute,second=00)
        booking["booking_date"] = booking_date
        booking["start_time"] = start_time
    return bookings

def get_ready_for_json(order):
    order["start_time"] = str(order["start_time"])
    order["booking_date"] = str(order["booking_date"])

def clean_terminal():
    os.system("cls" if os.name == 'nt' else "clear")

def find_order_by_data(bookings,data_type,data_value):
    for booking in bookings:
        if booking[data_type] == data_value:    
            return booking
    return False

def show_update_menu():
    valid = False
    while not valid:
        choise = input("""

What would you like to change? 

1. Booking date
2. Start time
3. Players number

Choose an option: """)
        if check_valid_menu_choise(choise,["1","2","3"]):
            return choise
        print("Not valid choise")

def insure_cancel():
    valid = False
    while not valid:
        choise = input("""
Are you sure you want to cancel the order? 

1. No
2. Yes

Choose an option:  """)
        if check_valid_menu_choise(choise,["1","2"]):
            return choise
        print("\nNot valid choise\n\n")

def calc_cancellation_fee(order):
    datetime_order = datetime.combine(order["booking_date"],order["start_time"])
    now = datetime.now()
    if now + timedelta(hours=24) < datetime_order:
        return 0
    elif now + timedelta(hours=6) < datetime_order:
        return int(order["total_price"]) / 100 * 25
    else:
        return int(order["total_price"]) / 100 * 50

def show_actvie_or_cancelled_orders(bookings,cancelled:str | None = None):
    for order in bookings:
        if cancelled:
            if order["status"].lower() == "cancelled":
                print(f"\n{order}\n\n")
                return
            print("\nNo active order\n\n ")
        else:
            if order["status"].lower() == "active":
                print(f"\n{order}\n\n")
                return
            print("No cancelled order\n\n")
    
            

def show_worning_json():
    valid = False
    while not valid:
        choise = input(f"""
The json is corrupted!
Do you want to continue? 
Doing so may overwrite the data contained therein.

1. Yes
2. No

Choose an option:  """)
        if check_valid_menu_choise(choise,["1","2"]):
            return choise
        print("\nNot valid option")

def show_income(bookings,active:str | None = None):
    count = 0
    for order in bookings:
        if active:
            if order["status"] == "Active":
                count += int(order["total_price"])
        else:
            if order["status"] == "Cancelled":
                count += int(order["cancellation_fee"])
    return count

def check_cancelling_time(order):
    if datetime.combine(order["booking_date"],order["start_time"]) < datetime.now():
        return False
    return True