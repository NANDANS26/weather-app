# Weather App

This Weather App fetches and displays the current temperature, as well as the high and low temperatures for the day, for a given city using the OpenWeatherMap API. Users can input city names and coordinates, choose the temperature units (Celsius, Fahrenheit, or Kelvin), and view the weather data for the specified location.

## Features

- **Fetch Weather Data**: Retrieve weather information for any city using its coordinates (latitude and longitude).
- **Temperature Display**: Show the current temperature, daily high, and daily low temperatures.
- **Multiple Units Support**: Display temperatures in Kelvin, Celsius, or Fahrenheit.
- **Example Usage**: Includes a demonstration with a predefined city (Portland) in different units.

## Requirements

- **Python 3.x**: This application requires Python 3.x. Online compilers are not suitable as they do not allow the installation of external libraries such as `requests`.
- **requests Library**: Install this library to enable HTTP requests to the OpenWeatherMap API.

You can install the `requests` library using pip:

```bash
pip install requests
```

## Usage

1. **Clone the Repository**:

```bash
git clone https://github.com/yourusername/weather-app.git
cd weather-app
```

2. **Run the Application**:

```bash
python weather_app.py
```

3. **Follow the Prompts**:
   - Enter the city name.
   - Enter the latitude.
   - Enter the longitude.
   - Choose the temperature units (Celsius, Fahrenheit, or Kelvin).

## Code Overview

### City Class

The `City` class represents a city and contains methods to fetch and display weather data.

- **Attributes**:
  - `name`: Name of the city.
  - `lat`: Latitude of the city.
  - `lon`: Longitude of the city.
  - `units`: Units for temperature (optional).
  - `temp`: Current temperature.
  - `temp_min`: Minimum temperature of the day.
  - `temp_max`: Maximum temperature of the day.

- **Methods**:
  - `__init__(self, name, lat, lon, units=None)`: Initializes the City object and fetches weather data.
  - `get_data(self)`: Fetches weather data from the OpenWeatherMap API.
  - `temp_print(self)`: Prints the temperature data in the specified units.

### Functions

- `get_user_input()`: Collects user input for city name, latitude, longitude, and temperature units.
- `given_ex()`: Demonstrates the functionality of the `City` class using Portland as an example.
- `main()`: Entry point of the application, handles user interactions and controls the flow of the program.

## Example

The app includes an example with the city of Portland, showing temperatures in Celsius, Fahrenheit, and Kelvin.

```python
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
```

## Acknowledgements

- **OpenWeatherMap**: For providing the weather data API.

## Contributing

If you want to contribute to this project, please fork the repository and create a pull request. I welcome all improvements, bug fixes, and feature additions.

## Contact

For any questions or suggestions, please contact:

- **Email**: nandans123456321@gmail.com
- **Phone**: +91-9108285647

---

Happy coding!
