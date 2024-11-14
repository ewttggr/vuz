import requests

def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()

        avatar_url = user_info.get('avatar_url', None)
            if avatar_url:
                avatar_response = requests.get(avatar_url)
                if avatar_response.status_code == 200:
                  avatar_image = Image.open(BytesIO(avatar_response.content))
                  avatar_image.show()
                else:
                  print("нет фото профиля.")
        print(f"Имя: {user_data.get('name', 'Не указано')}")
        print(f"Логин: {user_data.get('login', 'Не указано')}")
        print(f"Ссылка на GitHub: {user_data.get('html_url', 'Не указано')}")
        print(f"Город: {user_data.get('location', 'Не указано')}")
        print(f"Почта: {user_data.get('email', 'Не указано')}")
        print(f"Подписчики: {user_data.get('followers', 0)}")
        print(f"Подписки: {user_data.get('following', 0)}")
        print(f"Компания: {user_data.get('company', 'Не указано')}")
        print(f"Биография: {user_data.get('bio', 'Не указано')}")
    else:
        print(f"Ошибка: пользователь с логином {username} не найден.")

if __name__ == "__main__":
    username = input("Введите логин пользователя GitHub: ")
    get_github_user_info(username)
