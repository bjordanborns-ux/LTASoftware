# Imports
from vehicle import (
    load_vehicle,
    add_component,
    edit_component,
    remove_component,
    view_components,
    calculate_mass,
    calculate_cost,
    new_revision,
    view_revisions
)
from physics import (
    calculate_volume,
    calculate_buoyancy,
    calculate_weight,
    calculate_net_lift,
    calculate_drag,
    calculate_thrust_to_weight,
    calculate_acceleration,
    calculate_flight_time
)
import sys

# Choose main function or physics function
def main_menu():   
    while True:
        print("LTA ANALYSIS SOFTWARE")
        print("1 - Main Menu 2 - Physics Menu 3 - Exit Software")
        menu_choice = input("Enter Menu Choice (1-3): ").strip()
        if menu_choice == "1":
            main()
        elif menu_choice == "2":
            physics()
        elif menu_choice == "3":
            print("Shutting down LTA Analysis Software...")
            sys.exit(0)
        else:
            print("Error: Must Enter 1-3")

# main function
def main():
    while True:
        print(f"\n")
        print("================================")
        print("LTA Main Functions")
        print("================================")
        print(f"Vehicle: {vehicle['name']}")
        print(f"Active Revision: {vehicle['revision']}")
        print("--------------------------------")
        print("1 - View Components")
        print("2 - Register New Component")
        print("3 - Edit Component")
        print("4 - Remove Component")
        print("5 - Calculate Mass")
        print("6 - Calculate Cost")
        print("7 - Finalize Revision")
        print("8 - View Revision History")
        print("9 - Return to Main Menu")
        print("================================")

        selection = input("Select option 1-9: ").strip()
        if selection == "1":
            view_components(vehicle)
        elif selection == "2":
            add_component(vehicle)
        elif selection == "3":
            edit_component(vehicle)
        elif selection == "4":
            remove_component(vehicle)
        elif selection == "5":
            calculate_mass(vehicle)
        elif selection == "6":
            calculate_cost(vehicle)
        elif selection == "7":
            new_revision(vehicle)
        elif selection == "8":
            view_revisions()
        elif selection == "9":
            break
        else:
            print("Error: Select 1-9")


def physics():
    while True:
        print("================================")
        print("LTA Physics Tools")
        print("================================")
        print(f"Vehicle: {vehicle['name']}")
        print(f"Active Revision: {vehicle['revision']}")
        print("--------------------------------")
        print("1 - Calculate Balloon Volume")
        print("2 - Calculate Buoyant Force")
        print("3 - Calculate Vehicle Weight")
        print("4 - Calculate Net Lift")
        print("5 - Calculate Aerodynamic Drag")
        print("6 - Calculate Thrust to Weight")
        print("7 - Calculate Acceleration")
        print("8 - Estimate Flight Time")
        print("9 - Return to Main Menu")

        selection = input("Select option 1-9: ").strip()
        if selection == "1":
            calculate_volume()
        elif selection == "2":
            volume = calculate_volume()
            if volume is not None:    
                calculate_buoyancy(volume)
        elif selection == "3":
            calculate_weight(vehicle)
        elif selection == "4":
            volume = calculate_volume()
            if volume is not None:
                calculate_net_lift(vehicle, volume)
        elif selection == "5":
            calculate_drag()
        elif selection == "6":
            calculate_thrust_to_weight(vehicle)
        elif selection == "7":
            calculate_acceleration(vehicle)
        elif selection == "8":
            calculate_flight_time()
        elif selection == "9":
            break
        else:
            print("Error: Select 1-9")

# Start of program run:
# Vehicle settings and constants
if __name__ == "__main__":
    vehicle = load_vehicle()

    if vehicle is None:
        print("Error: Vehicle not able to be loaded")
        print("Application start aborted.")
        sys.exit(1)

    main_menu()



