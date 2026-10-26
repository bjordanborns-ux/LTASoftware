# Imports
import json
import datetime
from pathlib import Path
from vehicle import calculate_mass, calculate_cost
from physics import calculate_net_lift
# Constants from project
MAX_MASS = 800
MAX_BUDGET = 900
# Subject to change after build.
MIN_NET_LIFT = 0.0
MIN_FLIGHT_TIME = 10.0
# File directory constants (do not change)
BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "data" / "test_reports"

# Mass requirement testing
def run_mass_test(vehicle):
    print("MASS REQUIREMENT TEST")
    regulated_mass, total_mass = calculate_mass(vehicle)
    margin = MAX_MASS-regulated_mass

    if regulated_mass <= MAX_MASS:
        status = "PASS"
    else:
        status = "FAILED"

    print(f"Mass Requirement Test Status: {status}")
    print(f"Regulated Mass: {regulated_mass}")
    print(f"Mass Margin: {margin}")

    result = {
        "test": "Mass Requirement",
        "status": status,
        "measured": regulated_mass,
        "limit": MAX_MASS,
        "unit": "g"
    }
    return result

