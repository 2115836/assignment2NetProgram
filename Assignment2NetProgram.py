import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": city
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['current']['temperature']}°C")
            print(f"Description: {data['current']['weather_descriptions'][0]}")
            print(f"Humidity: {data['current']['humidity']}%")
            print(f"Wind Speed: {data['current']['wind_speed']}

        else:
            print(f"Error: {data['error']['info']}")

    except requests.RequestException as e:
        print(f"Error making the request: {e}")

if __name__ == "__main__":
    api_key = '89319aa1d74d99208c59efb20c39e5e1'
    city = input('Please enter the city name:')

    get_weather(api_key, city)