rods = float(input("Input a number of rods: "))
print(f"You input {rods} rods ")

def get_metres(rods):
    metres = rods * 5.0292
    return metres

def get_feet(rods):
    feet = get_metres(rods) * 0.3048
    return feet

def get_miles(rods):
    miles = get_metres(rods)/ 1609.34
    return miles

def get_furlongs(rods):
    furlongs = rods / 40
    return furlongs

def get_time(rods):
    time  = get_miles(rods)/ 3.1
    return time

def run(rods):
    print("Conversions: ")
    print(f"Metres: {get_metres(rods)}")
    print(f"Feet: {get_feet(rods)}")
    print(f"Miles: {get_miles(rods)}")
    print(f"Furlongs: {get_furlongs(rods)}")
    print(f"Minutes to walk {rods} rods {get_time(rods)}")

if __name__ == '__main__':
    run(rods)
