import requests

def display_weather_info():
    api_key = "19f75497408502a05d8fb5f75205c16b"  # Replace with your actual OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        # Get city name from user
        city_name = input("Enter city name: ")
        
        # Parameters for the API request
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"  # For temperature in Celsius
        }
        
        # Make the API request
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        # Get the weather data
        weather_data = response.json()
        
        # Extract specific fields
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        
        # Display in a user-friendly format
        print("\nWeather Information:")
        print("=" * 20)
        print(f"City: {city_name.title()}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
        elif response.status_code == 404:
            print("Error: City not found. Please check the city name.")
        else:
            print(f"HTTP Error occurred: {http_err}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your network connection.")
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    display_weather_info()
