import requests
from datetime import datetime
from io import BytesIO
from PIL import Image

API_KEY = "091ed4d78c461672888c654a356f35bcd"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
 url = f"{BASE_URL}?q={city}&appid={API_KEY}"
 response = requests.get(url)

 if response.status_code == 200:
  return response.json()
 else:
  print(f"Ошибка: Не удалось получить данные. Код: {response.status_code}")
  return None

def display_weather(weather_data):
 if weather_data:
  city = weather_data.get('name', 'Неизвестно')
  date = datetime.fromtimestamp(weather_data.get('dt', 0)).strftime('%Y-%m-%d %H:%M:%S')
  description = weather_data['weather'][0].get('description', 'Неизвестно')
  icon = weather_data['weather'][0].get('icon')

  temp = weather_data['main'].get('temp')
  temp_min = weather_data['main'].get('temp_min')
  temp_max = weather_data['main'].get('temp_max')
  humidity = weather_data['main'].get('humidity')
  pressure = weather_data['main'].get('pressure')

  print(f"Город: {city}")
  print(f"Дата: {date}")
  print(f"Описание погоды: {description}")

  if icon:
   icon_url = f"https://openweathermap.org/img/wn/{icon}.png"
   icon_response = requests.get(icon_url)
   if icon_response.status_code == 200:
    icon_image = Image.open(BytesIO(icon_response.content))
    icon_image.show()
   else:
    print("Ошибка: Не удалось получить иконку погоды.")

  print(f"Текущая температура: {round(temp - 273.15, 2) if temp else 'Неизвестно'} °C")
  print(f"Минимальная температура: {round(temp_min - 273.15, 2) if temp_min else 'Неизвестно'} °C")
  print(f"Максимальная температура: {round(temp_max - 273.15, 2) if temp_max else 'Неизвестно'} °C")
  print(f"Влажность: {humidity if humidity else 'Неизвестно'} %")
  print(f"Давление: {pressure if pressure else 'Неизвестно'} гПа")
 else:
  print("Ошибка: Город не найден.")

city = input("Введите город: ")
weather_data = get_weather_data(city)
display_weather(weather_data)
