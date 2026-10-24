import math
from vehicle import calculate_mass

# Physical constants
GRAVITY = 9.81 # m/s^2
AIR_DENSITY = 1.225 #kg/m^3
HELIUM_DENSITY = 0.1786 #kg/m^3
PI = 3.14159

# Calculate balloon volume
def calculate_volume():
    print("Balloon Volume Calcuulator")
    print("1 - Spherical Balloon 2 - Ellipsoidal Balloon")
    shape = input("Enter choice 1 or 2: ")
    if shape == "1":
        diam = float(input("Enter balloon diameter in meters: "))
        if diam <= 0:
            print("Error: Diameter must be positive")
            return None

        radius = diam/2
        volume = (4/3)*PI*(radius**3)

    elif shape == "2":
        length = float(input("Enter balloon length in meters: "))
        width = float(input("Enter balloon width in meters"))
        height = float(input("Enter balloon height in meters:"))

        if length <= 0 or width <= 0 or height <= 0:
            print("Error: Dimensions must be positive.")
            return None

        a = length/2
        b = width/2
        c = height/2

        volume = (4/3)*PI*a*b*c

    else:
        print("Error: Must enter 1 or 2")
        return None
    print(f"Volume of balloon: {volume}m^3")
    return volume

# Calculate buoyant force
def calculate_buoyancy(volume):
    if volume <= 0:
        print("Error: Invalid balloon volume")
        return None

    buoyant_force = AIR_DENSITY*GRAVITY*volume
    print(f"Buoyant Force: {buoyant_force}N")
    return buoyant_force

# Calculate vehicle weight
def calculate_weight(vehicle):
    _,total_flight_mass = calculate_mass(vehicle)
    mass_kg = total_flight_mass/1000
    weight = mass_kg*GRAVITY
    print(f"Vehicle weight: {weight}N")
    return weight

# Calculate vehicle net lift
def calculate_net_lift(vehicle,volume):
    buoyant_force = calculate_buoyancy(volume)
    vehicle_weight = calculate_weight(vehicle)
    if buoyant_force is None or vehicle_weight is None:
        return None
    helium_mass = HELIUM_DENSITY * volume
    helium_weight = helium_mass * GRAVITY
    net_lift = buoyant_force - helium_weight - vehicle_weight
    print(f"Net lift: {net_lift}N")

    if net_lift > 0:
        print("Vehicle has positive lift.")
    elif net_lift == 0:
        print("Vehicle is neutrally buoyant")
    else:
        print("Vehicle has negative lift.")
    return net_lift

# Calculate aerodynamic drag
def calculate_drag():
    print("Aerodynamic Drag Calculator")
    velocity = float(input("Enter velocity in m/s: "))
    drag_coef = float(input("Enter drag coefficient (Cd): "))
    reference_area = float(input("Enter reference area in meters squared: "))
    if drag_coef < 0 or reference_area <=0:
        print("Error: Invalid aerodynamic parameters.")
        return None

    drag = .5*AIR_DENSITY*(velocity**2)*drag_coef*reference_area
    print(f"Drag Force: {drag}N")
    return drag

# Calculate thrust to weight ratio
def calculate_thrust_to_weight(vehicle):
    thrust = float(input("Enter total propulsion thrust in N: "))
    total_vehicle_mass = calculate_weight(vehicle)
    if total_vehicle_mass <= 0:
        print("Error: Cannot calculate ratio")
        return None

    ratio = thrust/total_vehicle_mass
    print(f"Thrust to Weight Ratio: {ratio}")
    return ratio

# Calculate accelaration
def calculate_acceleration(vehicle):
    print("Acceleration Calculator")
    thrust = float(input("Enter total propulsion thrust in N: "))
    op_drag = float(input("Enter opposing drag in N: "))
    _,total_vehicle_mass = calculate_weight(vehicle)
    mass = total_vehicle_mass/1000

    if mass <= 0:
        print("Error: Mass must be positive.")
        return None

    net_force = thrust - op_drag
    acceleration = net_force/mass
    print(f"Acceleration: {acceleration}m/s^2")
    return acceleration

# Estimate flight time
def calculate_flight_time():
    print("Flight Endurance Estimator")
    batt_cap = float(input("Enter battery capacity in mAh: "))
    avg_cur = float(input("Enter average electrical current in mA: "))
    if batt_cap <= 0 or avg_cur <= 0:
        print("Error: Invalid battery values")
        return None

    flight_hours = batt_cap/avg_cur
    flight_minutes = flight_hours*60
    print(f"Estimated flight time: {flight_minutes}")
    return flight_minutes
