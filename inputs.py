from validations import check_empty,check_number,check_valid_menu_choise
from datetime import date,time

def get_input(massage,user_input):
    valid = False
    while not valid:
        data = input(massage)
        if check_empty(data):
            return data
        print(f"{user_input} can not be empty")

def get_number(massage,user_input):
    valid = False
    while not valid:
        number = get_input(massage,user_input)
        if user_input.lower() == "minutes":
            return number
        else:
            if check_number(number):
                return number
            print(f"{user_input} must be a positive number")

def get_room_id():
    return get_input("\nEnter room id: ","Room id")

def get_room_name():
    return get_input("Enter room name: ","Room name")

def get_difficulty():
    valid = False
    while not valid:
        difficulty =  get_input("Enter difficulty (hard, easy, medium): ","Difficulty")
        if check_valid_menu_choise(difficulty.lower(),["hard","easy","medium"]):
            return difficulty.capitalize()
        print("Not valid choise")

def get_duration():
    return get_number("Enter duration: ","Duration")

def get_min_players():
    return get_number("Enter min players: ","Players")

def get_max_players():
    return get_number("Enter max players: ","Players")

def get_price_per_player():
    return get_number("Enter price for player: ","Price")

def get_name():
    return get_input("\nEnter your name: ","Name")

def get_year():
    return get_number("\nYear: ","Year")
def get_month():
    return get_number("\nMonth: ","Month")
def get_day():
    return get_number("\nDay: ","Day")

def get_date():
    while True:
        year = get_year()
        month = get_month()
        day = get_day()
        try:
            booking_date = date(year=int(year),month=int(month),day=int(day))
            if booking_date <= date.today():
                print("\nNot valid date\n")
            else:
                return booking_date
        except ValueError:
            print("Date must be a regular date")
        
def get_hour():
    return get_number("\nHour: ","Hour")
def get_minutes():
    return get_number("\nMinutes: ","Minutes")

def get_start_time():
    hour = get_hour()
    minutes = get_minutes()
    try:
        start_time = time(hour=int(hour),minute=int(minutes),second=00)
        return start_time
    except ValueError:
        print("Time must be Clock time numbers")

def get_players():
    return get_number("\nEnter number of players: ","Players")

def get_order_id():
    return get_input("\nEnter order id: ","Order id")

def get_enter():
    input("enter to return: ")

