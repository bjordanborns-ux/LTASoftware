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

# Revision settings
current_revision = vehicle["revision"]
revision_number = int(current_revision.split("-")[1])
next_revision = f"REV-{revision_number+1:03d}"

# Input validation
def get_number(prompt, allow_negative):
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

def add_component(vehicle):
    print("REGISTER NEW COMPONENT")
    comp_id = input("Enter component ID: ").strip().upper()
    if not comp_id:
        print("Error: Component ID required.")
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
    }   
    
    vehicle["components"].append(component)
    save_vehicle(vehicle)
    print(f"Component {comp_id} registered successfully.")
    return True

def edit_component(vehicle):
    print(vehicle["components"])
    edit_id = input("Enter ID of component to edit: ").strip().upper()
    for component in vehicle["components"]:
        if component["id"] != edit_id:
            print("Component not found.")
    
    else:
        print(vehicle["components"])
        print("Edit options: 1 - Change Name 2 - Change Category 3 - Change mass 4 - Change cost 5 - Change position 6 - Change mass exclusion 7 - Cancel")
        option_select = get_number("Choose 1-7: ")
        if option_select == 1:
            new_name = input("Enter new name: ")
            if component["name"] == new_name:
                print("Name unchanged.")
                return
            else:
                component["name"] = new_name
                print(f"Component name updated to: {new_name}")
                return

        elif option_select == 2:
            new_cat = input("Enter new category: ")
            if component["category"] == new_cat:
                print("Category unchanged.")
                return
            else:
                component["category"] = new_cat
                print(f"Component category updated to: {new_cat}")
                return

        