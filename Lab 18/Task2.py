import requests
import json

def get_weather_with_error_handling():
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
        
        # Make the API request with timeout
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse and display the JSON response
        weather_data = response.json()
        print("\nWeather Details (JSON format):")
        print(json.dumps(weather_data, indent=4))
        
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
        
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching weather data: {e}")
        
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    get_weather_with_error_handling()
