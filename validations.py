from datetime import time,timedelta,datetime,date

def check_valid_menu_choise(choise,nums:list):
    if choise in nums:
        return True
    return False

def check_empty(user_input):
    if user_input.strip():
        return True
    return False

def check_number(number):
    try:
        return int(number) > 0
    except ValueError:
        return False

def check_id_exists(room_id,rooms):
    for room in rooms:
        if room["room_id"] == room_id:
            return True
    return False

def check_nin_max_player(min,max):
    return int(min)<int(max)

def check_activity(rooms,room_id):
    for room in rooms:
        if room["room_id"] == room_id:
            return room["is_active"]

def check_players(room,players):
    if int(room["max_players"]) >= players and players >= int(room["min_players"]):
        return True
    return False


