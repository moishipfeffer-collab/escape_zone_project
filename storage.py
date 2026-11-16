from helpers import show_worning_json
from pathlib import Path
import json

rooms_file = Path(__file__).parent / "data/rooms.json"
bookings_file = Path(__file__).parent / "data/bookings.json"

def load_json(file):
    if file.exists():
        try:
            with open(file,"r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            if file == rooms_file:
                if show_worning_json("rooms file") == "1":
                    return []
                return False
            else:
                if show_worning_json("orders file") == "1":
                    return []
                return False
    else:
        return []

def save_to_json(file,data):
    with open(file,"w") as file:
        json.dump(data,file,indent=4)


def load_json_rooms():
    return load_json(rooms_file)

def load_json_bookings():
    return load_json(bookings_file)

def save_rooms(rooms):
    save_to_json(rooms_file,rooms)

def save_bookings(bookings):
    save_to_json(bookings_file,bookings)