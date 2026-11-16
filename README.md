Run the program via main.py

The program consists of three core functions: one manages the escape rooms, another handles bookings, and the third deals with ongoing reporting regarding the escape rooms.

These management functions are located in the `run_program.py` file.

The function that manages the escape rooms takes the rooms as an argument; it invokes the menu function as well as the functions responsible for executing the user's chosen actions—all of which are defined in `manage_rooms.py`.

The function that manages bookings takes the bookings (and, for certain purposes, the rooms) as arguments; it calls the booking menu function and other functions related to booking management, located in `bookings.py`.

The function that manages reports takes both bookings and rooms as arguments; it invokes the reporting menu function along with other reporting-related functions found in `reports.py`.

The `inputs.py` file contains functions for receiving user input, while `validations.py` handles input validation (and other validation tasks). The `helpers.py` file contains various utility functions used throughout the project.

All of these components are integrated within the main entry point, which calls the main menu and the program's three core functions.

by moishi pfeffer
