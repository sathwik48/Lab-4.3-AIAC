import requests

def get_city_weather(city_name):
    """
    Get weather details for a specified city
    Args:
        city_name (str): Name of the city to get weather information for
    """
    # API configuration
    api_key = "19f75497408502a05d8fb5f75205c16b"  # Replace with your actual OpenWeatherMap API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    try:
        # Set up the parameters for the API request
        params = {
            "q": city_name,
            "appid": api_key,
            "units": "metric"  # For temperature in Celsius
        }
        
        # Make the API request with timeout
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse the response
        weather_data = response.json()
        
        # Extract relevant information
        temperature = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']
        
        # Display formatted weather information
        print("\nWeather Information")
        print("=" * 30)
        print(f"City: {city_name.title()}")
        print(f"Temperature: {temperature:.1f}°C")
        print(f"Feels like: {feels_like:.1f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
        print("=" * 30)
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API key. Please check your API key.")
        elif response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
        else:
            print(f"HTTP Error occurred: {http_err}")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Please check your network connection.")
        
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

def main():
    while True:
        # Get city name from user
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        
        # Check if user wants to quit
        if city.lower() == 'quit':
            print("Thank you for using the weather service!")
            break
            
        # Get and display weather for the entered city
        get_city_weather(city)

if __name__ == "__main__":
    main()
