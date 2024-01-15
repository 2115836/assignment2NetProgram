import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherstack.com/current"
    params = {
        "access_key": api_key,
        "query": city
    }