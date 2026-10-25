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

# Choose main function or physics function
print("1 - Main Menu 2 - Physics Menu")
menu_choice = input("Enter Menu Choice (1 or 2)")
if menu_choice == "1":
    # main function
    def main():
        vehicle = load_vehicle()
        if vehicle is None:
            print("Error: Vehicle not able to be loaded")
            print("Application start aborted.")
            return
        while True:
            name = vehicle["name"]
            revision = vehicle["revision"]
            print(f"\n")
            print("================================")
            print("Main Functions")
            print("================================")
            print(f"Vehicle: {name}")
            print(f"Active Revision: {revision}")
            print("--------------------------------")
            print("1 - View Components")
            print("2 - Register New Component")
            print("3 - Edit Component")
            print("4 - Remove Component")
            print("5 - Calculate Mass")
            print("6 - Calculate Cost")
            print("7 - Finalize Revision")
            print("8 - View Revision History")
            print("9 - Exit")
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
                print("Exiting LTA Software")
                break
            else:
                print("Error: Select 1-9")

elif menu_choice == "2":
    

if __name__ == "__main__":
    main()