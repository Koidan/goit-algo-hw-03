import random #Імпортували потрібні інструменти з бібліотеки

def get_numbers_ticket(min, max, quantity): #Створюємо функцію з трьома параметрами

    if not (1 <= min <= max <= 1000): #Створюємо обмеження для min тa max
        return []
    if not (0 < quantity <= (max - min + 1)):
        return []
    
    numbers = random.sample(range(min, max + 1), quantity) #Створюємо набір рандомних чисел

    return sorted(numbers) #Повертаємо відсортований список наших рандомних чисел


lottery_numbers = get_numbers_ticket(1, 49, 6) #Створюємо змінну яка приймає нашу функцію
print("Ваші лотерейні числа:", lottery_numbers) #Виводимо результат
