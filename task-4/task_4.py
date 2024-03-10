from datetime import datetime, timedelta # Імортуємо модулі 

def get(users: list): # створюємо Ф-цію
    congratulation_dates = [] # створюємо список, в який додамо коритсувачів, яких потрібно привітати 
    for user in users: #

        todey = datetime.today().date() # теперішній день 
        format_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date() # переводимо список зі словниками до об'єкту datetime
                        
        birthday_this_year = datetime(todey.year, format_date.month, format_date.day).date() # додаємо до дати народження теперішній рік для подільшого порівняння

        if birthday_this_year - todey < timedelta(days=0): # перевіряємо чи не пройшов дань народження
            birthday_this_year = datetime(todey.year +1, birthday_this_year.month, birthday_this_year.day).date() # якщо день народження пройшов, переносим на наступний рік 

        if birthday_this_year - todey <= timedelta(days=7): # перевіряємо дні народження які випадаєють на 7 днів вперед 

            if birthday_this_year.weekday() == 6: # перевіряємо чи випадає день народження на неділю
                add_days = birthday_this_year + timedelta(days=1) # якщо так - переносим на пн 
                add_days = add_days.strftime("%Y.%m.%d") # переводи об'єкт datetime в рядок 
                congratulation_dates.append({"name":user["name"], "congratulation_date":add_days}) # додаємо користувача до списку привітань 

            elif birthday_this_year.weekday() == 5: #
                add_days = birthday_this_year + timedelta(days=2) #
                add_days = add_days.strftime("%Y.%m.%d") # 
                congratulation_dates.append({"name":user["name"], "congratulation_date":add_days}) #

            else: # якщо дн не випадає на вихідний, додаємо в список не ворматуючи дату 
                birthday_this_year = birthday_this_year.strftime("%Y.%m.%d") # переводи в рядок 
                congratulation_dates.append({"name":user["name"], "congratulation_date":birthday_this_year}) #додаємо користувача до списку привітань

    return congratulation_dates # повертаємо список зі словниками користувачів, яких потрібно привітати 
users = [
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.16"}
]
result = get(users)

print(result)
