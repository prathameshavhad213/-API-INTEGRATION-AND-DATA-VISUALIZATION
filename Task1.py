import requests
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_weather_data(city):
    """Fetch weather data for Mumbai (since Open-Meteo API uses coordinates)."""
    try:
        # Mumbai's latitude and longitude
        url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&daily=temperature_2m_max&timezone=Asia/Kolkata"
        response = requests.get(url)
        response.raise_for_status()  # Raises error for bad response
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def visualize_temperature(data):
    """Visualize temperature data."""
    try:
        temperatures = data['daily']['temperature_2m_max']
        days = range(1, len(temperatures) + 1)

        sns.set(style="darkgrid")
        plt.figure(figsize=(10, 6))
        plt.plot(days, temperatures, marker='o', color='blue', linestyle='--')
        plt.title('Temperature Forecast for Mumbai')
        plt.xlabel('Days')
        plt.ylabel('Temperature (°C)')
        plt.xticks(days)
        plt.tight_layout()
        plt.show()
    except KeyError:
        print("Error: Could not extract temperature data. Check the API response structure.")

# Main Execution (Fixed for Mumbai)
city = "Mumbai"
weather_data = fetch_weather_data(city)
if weather_data:
    visualize_temperature(weather_data)
