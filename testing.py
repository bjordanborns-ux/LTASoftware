# Imports
import math
import json
from datetime import datetime
from pathlib import Path
from vehicle import calculate_mass, calculate_cost
from physics import calculate_net_lift, calculate_volume
from vehicle import MAX_MASS, MAX_BUDGET

# Subject to change after build.
MIN_NET_LIFT = 0.0
MIN_FLIGHT_TIME = 10.0
# File directory constants (do not change)
BASE_DIR = Path(__file__).resolve().parent
REPORT_DIR = BASE_DIR / "data" / "test_reports"
REPORT_DIR.mkdir(parents=True, exist_ok=True)

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

# Budget requirement testing
def run_budget_test(vehicle):
    print("BUDGET REQUIREMENT TEST")
    total_cost, remaining_budget = calculate_cost(vehicle)

    if total_cost <= MAX_BUDGET:
        status = "PASS"
    else:
        status = "FAILED"

    print(f"Budget Requirement Test Status: {status}")
    print(f"Total Cost: {total_cost}")
    print(f"Remaining Budget: {remaining_budget}")

    result = {
        "test": "Budget Requirement",
        "status": status,
        "measured": total_cost,
        "limit": MAX_BUDGET,
        "unit": "Gils"
    }
    return result

# Net lift test
def run_lift_test(vehicle):
    print("NET LIFT VERIFICATION TEST")
    
    volume = calculate_volume()
    if volume is None or volume <= 0:
        print("Error: Invalid volume.")
        return None
    
    net_lift = calculate_net_lift(vehicle, volume)
    if net_lift is None:
        print("Error: Lift calculation failed.")
        return None

    if net_lift >= MIN_NET_LIFT:
        status = "PASS"
    else:
        status = "FAILED"

    print(f"Net Lift Test Status: {status}")
    print(f"Net Lift: {net_lift}")

    result = {
        "test": "Net Lift",
        "status": status,
        "measured": net_lift,
        "limit": MIN_NET_LIFT,
        "unit": "N"
    }
    return result

# Propulsion/Drag test
def run_thrust_test():
    print("PROPULSION VERIFICATION TEST")
    thrust = float(input("Enter total propulsion thrust in N: "))
    drag = float(input("Enter Expected Aerodynamic Drag in N: "))
    if thrust < 0 or drag < 0:
        print("Error: Invalid values.")
        return None
    
    thrust_margin = thrust - drag
    if thrust_margin > 0:
        status = "PASS"
    else:
        status = "FAILED"

    print(f"Propulsion Verification Status: {status}")
    print(f"Thrust Margin: {thrust_margin}")

    result = {
        "test": "Propulsion/Drag",
        "status": status,
        "measured": thrust_margin,
        "limit": 0,
        "unit": "N"
    }
    return result

# Endurance test
def run_endurance_test():
    print("FLIGHT ENDURANCE TEST")
    batt_cap = float(input("Enter battery capacity in mAh: "))
    avg_cur = float(input("Enter average current in mA: "))
    if batt_cap <= 0 or avg_cur <= 0:
        print("Error: Invalid battery values.")
        return None
    estimated_minutes = (batt_cap/avg_cur)*60
    if estimated_minutes >= MIN_FLIGHT_TIME:
        status = "PASS"
    else:
        status = "FAILED"

    print(f"Flight Endurance Status: {status}")
    print(f"Estimated Flight time: {estimated_minutes}")

    result = {
        "test": "Flight Endurance",
        "status": status,
        "measured": estimated_minutes,
        "limit": MIN_FLIGHT_TIME,
        "unit": "minutes"
    }
    return result

# Component Data Check
def run_component_check(vehicle):
    print("COMPONENT DATA VERIFICATION")
    errors = []
    component_ids = set()
    required_fields = [
    "id",
    "name",
    "category",
    "mass_g",
    "cost_gils",
    "position_mm",
    "excl_status"
    ]



    for component in vehicle["components"]:
        comp_id = component.get("id")

        if not isinstance(comp_id, str) or not comp_id.strip():
            errors.append("Component has missing or invalid ID")
        elif comp_id in component_ids:
            errors.append(f"Duplicate component ID: {comp_id}")
        else:
            component_ids.add(comp_id)

        missing_fields = []

        for field in required_fields:
            if field not in component:
                missing_fields.append(field)

        if missing_fields:
            errors.append(
                f"Component {comp_id}: Missing fields: {missing_fields}"
            )
            continue

        mass = component["mass_g"]
        cost = component["cost_gils"]

        if not isinstance(mass, (int, float)) or isinstance(mass, bool):
            errors.append(f"Error {comp_id}: Mass must be a number")
        elif not math.isfinite(mass) or mass < 0:
            errors.append(f"Error {comp_id}: Mass must be finite and not negative")

        if not isinstance(cost, (int, float)) or isinstance(cost, bool):
            errors.append(f"Error {comp_id}: Cost must be a number")
        elif not math.isfinite(cost) or cost < 0:
            errors.append(f"Error {comp_id}: Cost must be finite and not negative.")

        position = component["position_mm"]

        if (
            not isinstance(position, list)
            or len(position) != 3
            or any(
                not isinstance(value, (int, float))
                or isinstance(value, bool)
                or not math.isfinite(value)
                for value in position
            )
        ):
            errors.append(f"{comp_id}: Invalid position coordinates")

        if not isinstance(component["excl_status"], bool):
            errors.append(f"{comp_id}: Invalid exclusion status")

    if not errors:
        status = "PASS"
    else:
        status = "FAILED"

    print(f"Component Check Status: {status}")
    print(f"Number of errors: {len(errors)}")

    for error in errors:
        print(error)
        
    results = {
        "test": "Component Data Check",
        "status": status,
        "errors": errors
    }
    return results

# Full test suite
def run_test_suite(vehicle):
    print("LTA - Verification Suite")
    results = []
    component_result = run_component_check(vehicle)
    results.append(component_result)
    if component_result["status"] == "FAILED":
        print("Error: Fix component data ebfore running the remaining tests.")
        return results

    mass_result = run_mass_test(vehicle)
    results.append(mass_result)

    budget_result = run_budget_test(vehicle)
    results.append(budget_result)

    lift_conf = input("Run lift test? Y/N: ").strip().upper()

    if lift_conf == "Y":
        lift_result = run_lift_test(vehicle)

        if lift_result is not None:
            results.append(lift_result)

    thrust_conf = input("Run thrust test? Y/N: ").strip().upper()
    if thrust_conf == "Y":
        thrust_result = run_thrust_test()
        if thrust_result is not None:
            results.append(thrust_result)

    endurance_conf = input("Run endurance test? Y/N: ").strip().upper()
    if endurance_conf == "Y":
        endurance_result = run_endurance_test()
        if endurance_result is not None:
            results.append(endurance_result)

    passed = 0 
    failed = 0

    for result in results:
        if result["status"] == "PASS":
            passed += 1
        elif result["status"] == "FAILED":
            failed += 1

    print("===============================")
    print("VERIFICATION SUMMARY")
    print("===============================")
    print(f"Tests run: {len(results)}")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    return results

# Save test report
def save_test_report(vehicle, results):
    print("SAVE TEST REPORT")
    if not results:
        print("No test results to save.")
        return False
    current_time = datetime.now()
    timestamp = current_time.strftime("%Y%m%d_%H%M%S")
    report_filename = vehicle["revision"] + "_" + timestamp + ".json"

    report_path = REPORT_DIR / report_filename

    report = {
        "vehicle": vehicle["name"],
        "revision": vehicle["revision"],
        "timestamp": current_time.isoformat(),
        "results": results
    }

    try:
        with open(report_path, "w") as f:
            json.dump(report, f, indent=4)

    except OSError:
        print("Error: Unable to save report")
        return False

    print("Test report saved successfully")
    print(f"Report saved to: {report_path}")

    return True