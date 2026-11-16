from validations import check_valid_menu_choise,check_id_exists,check_nin_max_player
from inputs import get_room_id,get_room_name,get_duration,get_difficulty
from inputs import get_min_players,get_max_players,get_price_per_player
from storage import save_rooms
def show_rooms_menu():
    while True:
        print("\n-------- ROOMS MANAGEMENT --------\n")
        choise = input("""
1. Show all rooms
2. Show full details on room
3. Add new room
4. Update room datails
5. Activate or deactivate a room.

Choose an option: """)
        if check_valid_menu_choise(choise,["1","2","3","4","5"]):
            return choise
        print("Not valid choise")

def show_updating_menu():
    valid = False
    while not valid:
        choise = input("""
\nWhat would you like to change?

1. room_id
2. name
3. difficulty
4. duration
5. min players
6. max players
7. price per player

Choose an option: """)
        if check_valid_menu_choise(choise,["1","2","3","4","5","6","7"]):
            return choise
        print("Not valid choise")

# option 1 show all rooms

def show_all_rooms(rooms):
    if rooms:
        print("\n --- The rooms are: ---")
        for room in rooms:
            print(f"\nroom id: {room['room_id']}")
            print(f"room name: {room['name']}\n")
    else:
        print("No rooms yet!\n\n")

# option 2 show details

def find_room_by_id(rooms,room_id):
    for room in rooms:
        if str(room["room_id"]) == str(room_id):
            return room
    return False

def show_full_details(room):
    print(f"\n{room}\n\n")

def run_show_room_details(rooms):
    if not rooms:
        print("\nNo rooms!")
    else:
        room_id = get_room_id()
        room = find_room_by_id(rooms,room_id)
        if room:
            show_full_details(room)
        else:
            print("\nThe room not found\n\n")

# option 3 add room 

def create_room(room_id,name,difficulty,duration,min_players,max_players,price):
    return     {
        "room_id": room_id,
        "name": name,
        "difficulty": difficulty,
        "duration": duration,
        "min_players": min_players,
        "max_players": max_players,
        "price_per_player": price,
        "is_active": True
    }

def add_room_to_rooms(room,rooms):
    rooms.append(room)


def run_add_new_room(rooms):
    room_id = get_room_id()
    if not check_id_exists(room_id,rooms):
        name = get_room_name()
        difficulty = get_difficulty()
        duration = get_duration()
        min_players = get_min_players()
        max_players = get_max_players()
        price = get_price_per_player()
        if check_nin_max_player(min_players,max_players):
            room = create_room(room_id,name,difficulty,duration,min_players,max_players,price)
            add_room_to_rooms(room,rooms)
            save_rooms(rooms)
            print("\n---------- The room added successfully ----------\n\n")
        else:
            print("\nThe max players must be grater then min players\n\n")
    else:
        print("The room id exists allready\n\n")

# option 4 update room details

def run_update_room(rooms):
    if not rooms:
        print("No rooms!")
    else:
        room_id = get_room_id()
        room = find_room_by_id(rooms,room_id)
        if room:
            choise = show_updating_menu()
            if choise == "1":
                room["room_id"] = get_room_id()
            elif choise == "2":
                room["name"] = get_room_name()
            elif choise == "3":
                room["difficulty"] = get_difficulty()
            elif choise == "4":
                room["duration"] = get_duration()
            elif choise == "5":
                room["min_players"] = get_min_players()
            elif choise == "6":
                room["max_players"] = get_max_players()
            elif choise == "7":
                room["price_per_player"] = get_price_per_player()
            save_rooms(rooms)
            print("\n---------- Updated successfully ----------\n\n")
        else:
            print("Room not found\n\n")

# option 5 activate or deactivate a room

def chang_active(rooms):
    if not rooms:
        print("No rooms")
    else:
        room_id = get_room_id()
        room = find_room_by_id(rooms,room_id)
        if room:
            room["is_active"] = not room["is_active"]
            save_rooms(rooms)
            print("\n---------- Activity changed successfully ----------\n\n")
        else:
            print("\nRoom not found\n\n")
