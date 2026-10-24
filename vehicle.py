import json
from pathlib import Path
from copy import deepcopy

MAX_MASS = 800
MAX_BUDGET = 900

# file paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REVISION_DIR = DATA_DIR / "revisions"
VEHICLE_FILE = DATA_DIR / "vehicle.json"

DATA_DIR.mkdir(parents=True, exist_ok=True)
REVISION_DIR.mkdir(parents=True, exist_ok=True)

# Vehicle configuration settings
vehicle = {
    "name": "LTA McQueen",
    "revision": "REV-001",
    "revision_description": "Initial prelim. design",
    "components": []
}

# Input validation
def get_number(prompt, allow_negative=False):
    while True:
        try:
            number = float(input(prompt))
            if number < 0 and not allow_negative:
                print("Error: Negative value not allowed.")
                continue
            return number
        except ValueError:
            print("Error: Enter valid number.")

# Save vehicle
def save_vehicle(vehicle):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(VEHICLE_FILE, "w") as file:
        json.dump(vehicle, file, indent=4)
    print("Vehicle configuration saved.")
    return True

# Load vehicle
def load_vehicle():
    if VEHICLE_FILE.is_file():
        try:
            with open(VEHICLE_FILE, "r") as file:
                vehicle_data = json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Unable to load vehicle.")
            print("Saved file needs inspection.")
            return None
        if not isinstance(vehicle_data, dict):
            print("Invalid vehicle data.")
            return None

        required_fields = ["name", "revision", "components"]
        for field in required_fields:
            if field not in vehicle_data:
                print(f"Missing required field: {field}")
                return None

        if not isinstance(vehicle_data["components"], list):
            print("Invalid components list.")
            return None
        return vehicle_data
    else:
        new_vehicle = deepcopy(vehicle)
        save_vehicle(new_vehicle)
        return new_vehicle

# Component adding menu
def add_component(vehicle):
    print("REGISTER NEW COMPONENT")
    comp_id = input("Enter component ID: ").strip().upper()
    if not comp_id:
        print("Error: Component ID required.")
        return False
    for component in vehicle["components"]:
        if component["id"] == comp_id:
            print("Error: Duplicate component")
            return False
    
    comp_name = input("Enter component name: ").strip()
    comp_cat = input("Enter component category: ").strip()
    if not comp_name or not comp_cat:
        print("Error: Required field missing.")
        return False
    comp_mass = get_number("Enter mass: ")
    comp_cost = get_number("Enter cost: ")
    
    comp_x = get_number("Enter coordinate (X): ", True)
    comp_y = get_number("Enter coordinate (Y): ", True)
    comp_z = get_number("Enter coordinate (Z): ", True)

    while True:
        excluded_input = input("Exclude from competition mass? (Y/N): ").strip().upper()
        if excluded_input in ("Y", "N"):
            excluded = excluded_input == "Y"
            break
        print("Error: Enter Y or N")

    component = {
    "id": comp_id,
    "name": comp_name,
    "category": comp_cat,
    "mass_g": comp_mass,
    "cost_gils": comp_cost,
    "position_mm": [comp_x, comp_y, comp_z],
    "excl_status": excluded
    }   
    
    vehicle["components"].append(component)
    save_vehicle(vehicle)
    print(f"Component {comp_id} registered successfully.")
    return True

# Component edit menu
def edit_component(vehicle):
    print(vehicle["components"])
    edit_id = input("Enter ID of component to edit: ").strip().upper()
    found_component = None

    for component in vehicle["components"]:
        if component["id"] == edit_id:
            found_component = component
            break

    if found_component is None:
        print("Component not found.")
        return False

    component = found_component
    print(component)
    print("Edit options: 1 - Change Name 2 - Change Category 3 - Change mass 4 - Change cost 5 - Change position 6 - Change mass exclusion 7 - Cancel")
    option_select = get_number("Choose option 1-7: ")

    if option_select == 1:
        new_name = input("Enter new name: ")
        if component["name"] == new_name:
            print("Name unchanged.")
            return
        else:
            component["name"] = new_name
            save_vehicle(vehicle)
            print(f"Component name updated to: {new_name}")
            return

    elif option_select == 2:
        new_cat = input("Enter new category: ")
        if component["category"] == new_cat:
            print("Category unchanged.")
            return
        else:
            component["category"] = new_cat
            save_vehicle(vehicle)
            print(f"Component category updated to: {new_cat}")
            return

    elif option_select == 3:
        new_mass = get_number("Enter new mass in g: ")
        if component["mass_g"] == new_mass:
            print("Mass unchanged.")
            return
        else:
            component["mass_g"] = new_mass
            save_vehicle(vehicle)
            print(f"Component mass updated to: {new_mass}")
            return

    elif option_select == 4:
        new_cost = get_number("Enter new cost: ")
        if component["cost_gils"] == new_cost:
            print("Cost unchanged.")
            return
        else:
            component["cost_gils"] = new_cost
            save_vehicle(vehicle)
            print(f"Component cost updated to: {new_cost}")
            return

    elif option_select == 5:
        print("Position edit options: 1 - X Axis 2 - Y Axis 3 - Z Axis")
        pos_select = get_number("Choose option 1-3: ")

        if pos_select == 1:
            new_x = get_number("Enter new X position: ", True)
            if new_x == component["position_mm"][0]:
                print("X position unchanged.")
                return
            else:
                component["position_mm"][0] = new_x
                save_vehicle(vehicle)
                print(f"X position updated to: {new_x}")

        elif pos_select == 2:
            new_Y = get_number("Enter new Y position: ", True)
            if new_Y == component["position_mm"][1]:
                print("Y position unchanged.")
                return
            else:
                component["position_mm"][1] = new_Y
                save_vehicle(vehicle)
                print(f"Y position updated to: {new_Y}")

        elif pos_select == 3:
            new_z = get_number("Enter new Z position: ", True)
            if new_z == component["position_mm"][2]:
                print("Z position unchanged.")
                return
            else:
                component["position_mm"][2] = new_z
                save_vehicle(vehicle)
                print(f"Z position updated to: {new_z}")

        else:
            print("Error: Must Select 1-3")
            return

    elif option_select == 6:
        while True:
            excluded_input = input("Exclude from competition mass? (Y/N): ").strip().upper()
            if excluded_input in ("Y", "N"):
                new_status = excluded_input == "Y"
                break
            print("Error: Enter Y or N")

        if component.get("excl_status", False) == new_status:
            print("Mass exclusion status unchanged.")
            return
        else:
            component["excl_status"] = new_status
            save_vehicle(vehicle)
            print("Mass exclusion status updated.")
            return

    elif option_select == 7:
        return

    else:
        print("Error: Must Select 1-7")
        return False

# Remove component from components list
def remove_component(vehicle):
    print(vehicle["components"])
    remove_id = input("Enter ID of component to remove: ").strip().upper()
    found_component = None

    for component in vehicle["components"]:
        if component["id"] == remove_id:
            found_component = component
            break

    if found_component is None:
        print("Component not found.")
        return False

    component = found_component
    print(component)
    while True:
        remove_conf = input("Are you sure you want to remove? (Y/N): " ).strip().upper()
        if remove_conf == "Y":
            vehicle["components"].remove(component)
            save_vehicle(vehicle)
            print(f"Component {remove_id} removed successfully.")
            return True
        elif remove_conf == "N":
            print("Remove cancelled")
            return
        else:
            print("Enter Y or N.")
        
# Calculates mass
def calculate_mass(vehicle):
    regulated_mass = 0
    total_flight_mass = 0

    for component in vehicle["components"]:
        total_flight_mass += component["mass_g"]
        if component.get("excl_status", False) == False:
            regulated_mass += component["mass_g"]

    mass_margin = MAX_MASS - regulated_mass
    print(f"Regulated Mass: {regulated_mass}g")
    print(f"Total Flight Mass: {total_flight_mass}g")
    print(f"Mass Margin: {mass_margin}g ")

    if regulated_mass > MAX_MASS:
        print(f"WARNING: MASS LIMIT EXCEEDED BY {-mass_margin}g")

    else:
        print("Mass requirement satisfied")
    return regulated_mass, total_flight_mass

# Calculate cost
def calculate_cost(vehicle):
    total_cost = 0
    for component in vehicle["components"]:
        total_cost += component["cost_gils"]
    budget_remaining = MAX_BUDGET - total_cost
    print(f"Total Cost: ${total_cost} gils")
    print(f"Budget remaining: ${budget_remaining} gils")

    if total_cost > MAX_BUDGET:
        print(f"WARNING: BUDGET EXCEEDED BY ${-budget_remaining}")
    else:
        print("Within project budget")  
    return total_cost, budget_remaining

# Finalize revision
def new_revision(vehicle):
    current_revision = vehicle["revision"]
    revision_number = int(current_revision.split("-")[1])
    next_revision = f"REV-{revision_number + 1:03d}"

    revision_file = REVISION_DIR / f"{current_revision}.json"

    if revision_file.exists():
        print("Revision already finalized.")
        return False

    while True:
        confirmation = input(f"Finalize {current_revision}? (Y/N)").strip().upper()
        if confirmation == "Y":
            break
        elif confirmation == "N":
            print("Revision finalization cancelled.")
            return
        else:
            print("Error: Y or N")

    snapshot = deepcopy(vehicle)
    try:
        with open(revision_file, "x") as file:
            json.dump(snapshot,file,indent=4)
    except FileExistsError:
        print("Revision already finalized.")
        return False
    except OSError:
        print("Error: Unable to save revision snapshot.")
        return False

    description = input("Enter description for next revision: ")
    if not description:
        description = "New working revision"

    vehicle["revision"] = next_revision
    vehicle["revision_description"] = description

    save_vehicle(vehicle)
    print(f"Revision {current_revision} finalized.")
    print(f"New active revision: {next_revision}")
    return True

# View revision history
def view_revisions():
    revision_files = sorted(REVISION_DIR.glob("*.json"), key=lambda file: int(file.stem.split("-")[1]))
    if not revision_files:
        print("No finalized revisions found.")
        return []

    revision_list = []

    for file in revision_files:
        with open(file, "r") as revision_file:
            revision_data = json.load(revision_file)

        revision_number = revision_data["revision"]
        revision_description = revision_data["revision_description"]
        component_count = len(revision_data["components"])

        print(f"Revision: {revision_number}")
        print(f"Description: {revision_description}")
        print(f"Component Count: {component_count}")
        print("-----------------------------")

        revision_list.append(revision_data)

    return revision_list

# View component details
def view_components(vehicle):
    if not vehicle["components"]:
        print("No components registered.")
        return
    for component in vehicle["components"]:
        id_view = component["id"]
        name_view = component["name"]
        cat_view = component["category"]
        mass_view = component["mass_g"]
        cost_view = component["cost_gils"]
        pos_view = component["position_mm"]

        print(f"ID: {id_view}")
        print(f"Name: {name_view}")
        print(f"Category: {cat_view}")
        print(f"Mass: {mass_view}")
        print(f"Cost: {cost_view}")
        print(f"Position (X,Y,Z): {pos_view}")

    return


