import requests  # Import the requests library to handle HTTP requests

def get_weather(city_name):
    # Define the API key and base URL for the OpenWeatherMap API
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        # Send a GET request to the API
        response = requests.get(base_url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Convert the response from JSON to a Python dictionary
        data = response.json()

        # Check if the city was found in the API response
        if data["cod"] != "404":
            # Extract relevant weather data from the response
            main = data["main"]
            weather_description = data["weather"][0]["description"]
            temperature = main["temp"]
            humidity = main["humidity"]

            # Print the weather information
            print(f"City: {city_name}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather Description: {weather_description.capitalize()}")
        else:
            # Inform the user if the city was not found
            print(f"City {city_name} not found. Please check the name and try again.")

    except requests.exceptions.HTTPError as err:
        # Handle HTTP errors (e.g., network issues)
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        # Handle other potential errors (e.g., invalid input)
        print(f"An error occurred: {err}")

# Check if the script is being run directly
if __name__ == "__main__":
    # Prompt the user to enter a city name
    city = input("Enter city name: ")
    # Call the function to get and display the weather information
    get_weather(city)