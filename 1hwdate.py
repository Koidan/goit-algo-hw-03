import datetime #Імпортуємо потрібні інструменти з бібліотеки

def get_days_from_today(date): #Створюємо функцію з одним параметром
    while True: #Для того, щоб якщо виникла помилка код не закінчувався 
        try: #Пробуємо без помилок 
            date = input("YYYY-MM-DD: ") #Просимо дату від користувача
            usr_date = datetime.datetime.strptime(date, "%Y-%m-%d").date() #str -> datetime з правильним форматом і тільки датою без часу
            today = datetime.date.today() #Дізнаємося сьогоднішню дату
            diff = today - usr_date #Віднімаємо дати
            print(f"Разница в днях: {diff.days}") #Виводимо результат
            break #Закінчуємо цикл
        except ValueError: #Якщо виникла помилка
            print("YYYY(0001-9999)-MM(1-12)-DD(1-31)") #Підсказуємо як правильно ввести дату


get_days_from_today('') #Викликаємо функцію, а то для чого ми її писали
