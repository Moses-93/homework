from datetime import datetime, timedelta

def calculate_congratulation_dates(users):
    today = datetime.today().date()
    congratulation_dates = []

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = datetime(today.year, user_birthday.month, user_birthday.day).date()

        if birthday_this_year < today:
            birthday_this_year = datetime(today.year + 1, user_birthday.month, user_birthday.day)


        if birthday_this_year.weekday() in [5, 6]:
                birthday_this_year + timedelta(days=1) if birthday_this_year.weekday() == 5 else 2

                
            
        congratulation_dates.append({"name": user["name"], "congratulation_date": birthday_this_year})

        
        # congratulation_dates.append({"name": user["name"], "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")})

    return congratulation_dates

# Example usage
users = [
    {"name": "Alice", "birthday": "2000.05.15"},
    {"name": "Bob", "birthday": "2000.03.10"},
    # Add more users here
]

result = calculate_congratulation_dates(users)
for entry in result:
    print(f"{entry['name']} - {entry['congratulation_date']}")



