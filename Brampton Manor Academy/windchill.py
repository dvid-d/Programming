def default_windchill_values():
    air_temp = 10.0
    air_speed = 15.0
    felt_temp = (35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16)
    print(f"Temperature of {air_temp} and speed of {air_speed} gives windchill of: {felt_temp}")
    air_temp = 0.0
    air_speed = 25.0
    felt_temp = (35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16)
    print(f"Temperature of {air_temp} and speed of {air_speed} gives windchill of: {felt_temp}")
    air_temp = -10.0
    air_speed = 35.0
    felt_temp = (35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16)
    print(f"Temperature of {air_temp} and speed of {air_speed} gives windchill of: {felt_temp}")

def calculate_wind_chill():
    air_temp = float(input("Input an air temperature: "))
    air_speed = float(input("Input a wind speed: "))
    felt_temp = (35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16)
    print(f"Windchill: {felt_temp}")

if __name__ == '__main__':
    default_windchill_values()
    calculate_wind_chill()
