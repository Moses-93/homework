import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
def normalize_phone(phone_number):
    try:
        regex = "[^0-9]" # регулярний вираз для символів, які ми хочемо видалити
        phone_number = ["+38" + re.sub(regex, "", number.replace("38", "")) for number in raw_numbers] # Видаляємо непотрібні символи з кожного номера в списку, та додаємо +38
    except Exception:
        print(f"Програма не може розпізнати ваш номер телефону!")
    return phone_number

print(normalize_phone(raw_numbers))

