import requests


def get_weather(city):
    api_key = "91ed4d78c461672888c654a356f35bcd"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()

        print(f"Дата: {weather_data['dt']}")
        print(f"Погода: {weather_data['weather'][0]['description']}")
        print(f"Иконка: https://openweathermap.org/img/w/{weather_data['weather'][0]['icon']}.png")
        print(f"Текущая температура: {weather_data['main']['temp']}°C")
        print(f"Минимальная температура: {weather_data['main']['temp_min']}°C")
        print(f"Максимальная температура: {weather_data['main']['temp_max']}°C")
        print(f"Скорость ветра: {weather_data['wind']['speed']} м/с")
        print(f"Влажность: {weather_data['main']['humidity']}%")
        print(f"Давление: {weather_data['main']['pressure']} гПа")
    else:
        print(f"Ошибка: не удалось получить данные для города {city}.")


if __name__ == "__main__":
    city = input("Введите название города: ")
    get_weather(city)
