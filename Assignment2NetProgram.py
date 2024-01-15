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
            
        else:
            print(f"Error: {data['error']['info']}")

    