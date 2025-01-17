import datetime #Імпортуємо потрібні інструменти з бібліотеки

def get_days_from_today(date): #Створюємо функцію з одним параметром
        try: #Пробуємо без помилок 

            usr_date = datetime.datetime.strptime(date, "%Y-%m-%d").date() #str -> datetime з правильним форматом і тільки датою без часу
            today = datetime.date.today() #Дізнаємося сьогоднішню дату
            diff = today - usr_date #Віднімаємо дати
            return diff.days
        except ValueError: #Якщо виникла помилка

            return "Invalid date format. Use YYYY(0001-9999)-MM(01-12)-DD(01-31)"


result = get_days_from_today("2200-12-12")
print(f"Difference is  {result}")

