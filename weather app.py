import requests
import time

class City:
    def __init__(self, name, lat, lon, units=None):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units 
        self.get_data()

    def get_data(self):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid=eacfde86635c5e88131506e48da0da48"
            if self.units:
                url += f"&units={self.units}"
            response = requests.get(url)
            response_json = response.json()

            if "main" in response_json:
                self.temp = response_json["main"]["temp"]
                self.temp_min = response_json["main"]["temp_min"]
                self.temp_max = response_json["main"]["temp_max"]
            else:
                print(f"Could not retrieve weather data for {self.name}. Please check the city name or coordinates.")
                self.temp = self.temp_min = self.temp_max = None
        except:
            print("No internet access or invalid API request.")
            self.temp = self.temp_min = self.temp_max = None

    def temp_print(self):
        if self.temp is not None:
            if self.units == "imperial":
                units_symbol = "F"
            elif self.units == "metric":
                units_symbol = "C"
            else:
                units_symbol = "K"
            print(f"In {self.name}, the current temperature is {self.temp}°{units_symbol}")
            print(f"Today's High: {self.temp_max}°{units_symbol}")
            print(f"Today's Low: {self.temp_min}°{units_symbol}")
        else:
            print(f"Temperature data is not available for {self.name}.")

def get_user_input():
    
    time.sleep(1)
    print("Enter the name and coordinates accurately!!")
    time.sleep(1)
    name = input("Enter the city name: ")
    lat = float(input("Enter the latitude: "))
    lon = float(input("Enter the longitude: "))
    units = input("Enter the units (type 'imperial' for Fahrenheit, 'metric' for Celsius and leave blank for Kelvin): ").strip().lower()
    time.sleep(1)
    if units not in ["imperial", "metric", ""]:
        units = None  # Default to Kelvin if invalid input
    return name, lat, lon, units

def given_ex():
    print("This city's temperature is just for an example")
    time.sleep(1)
    Ex_City = City("PORTLAND", 45.52345000, -122.67621000, "metric")
    Ex_City1 = City("PORTLAND", 45.52345000, -122.67621000, "imperial")
    Ex_City2 = City("PORTLAND", 45.52345000, -122.67621000)
    print("In Celsius")
    time.sleep(0.5)
    Ex_City.temp_print()
    time.sleep(0.5)
    print("In Fahrenheit")
    time.sleep(0.5)
    Ex_City1.temp_print()
    time.sleep(0.5)
    print("In Kelvin")
    time.sleep(0.5)
    Ex_City2.temp_print()
    time.sleep(1)
        
def main():
    given_ex()
    choice = input("Do you want the temperature of another city of your choice? (yes/no): ").strip().lower()
    if choice not in ["yes", "y"]:
        time.sleep(0.5)
        print("Thank you for your time. Have a nice day!!")
        return 0
    while True:
        name, lat, lon, units = get_user_input()
        if name is None:  # If the user chooses not to enter another city
            break
            
        user_city = City(name, lat, lon, units)
        user_city.temp_print()
        
        another1 = input("Do you want to check the temperature for another city? (yes/no): ").strip().lower()
        if another1 not in ["yes", "y"]:
            time.sleep(0.5)
            print("Thank you for your time. Have a nice day!!")
            break
if __name__ == "__main__":
    main()

