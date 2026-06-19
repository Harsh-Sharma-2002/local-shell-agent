import requests

def get_weather(lat,long):
    """
    This is a publicly available API that return weather for given latitide and longitude
    """

    response  = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m")

    data = response.json()
    return data["current"]


ans = get_weather(0,0)

print(ans)