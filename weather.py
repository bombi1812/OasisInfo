import datetime as dt
import requests


Base_url="https://api.openweathermap.org/data/2.5/weather?"
API_KEy='fb13947f9d278a5d43d27cdc91a3ae9f'
CITY=input("Enter city:")


def kel_to_cel(kel):
    cel=kel-273.15
    return cel


url=Base_url+"appid="+API_KEy+"&q="+CITY
response=requests.get(url).json()

temp_kel=response['main']['temp']
temp_cel=kel_to_cel(temp_kel)
feels_like_kel=response['main']['feels_like']

feels_like_cel=kel_to_cel(feels_like_kel)

humidity=response['main']['humidity']
wind=response['wind']['speed']

description=response['weather'][0]['description']
sunrise_time=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset_time=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])
print(f"Temperature in {CITY}:{temp_cel:.2f}Celsius ")
print(f"Temperature in {CITY}:{temp_cel:.2f}Celsius or {feels_like_cel}celcius")
print(f"Humidity in {CITY}:{humidity}%")
print(f"Wind Speed in {CITY}:{wind}m/s")
print(f"General Weather in {CITY}:{description}")
print(f"Sunrises in {CITY}:{sunrise_time} local time")
print(f"Sunsets in {CITY}:{sunset_time} local time")
 