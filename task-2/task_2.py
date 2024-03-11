import random 

try:
    def get_numbers_ticket(min, max, quantity): # створення функції 
        lottery_num = random.sample(range(min, max), k=quantity) # sample - вказує роозмір списку. range - Задає потрібний діапазон
        lottery_num.sort() # сортування списку з числами
        if min < 1:
            lottery_num = []
        elif max > 1000:
            lottery_num = []
        return lottery_num # повернення відсортованого списку с функції

    # введіть числа в такому форматі: '1, 10, 5'. Останнє число повинно бути більше попереднього
    result = get_numbers_ticket(0, 1000, 5) # викликаємо функцію і вказуємо аргументи
    print(result)    

except Exception: # перехоплення всіх помилок 
    print("Ви вказали невірний формат данних. Потрібно ввести цілі числа, як вказано в прикладі!")
    



    