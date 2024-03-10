from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    days = 7  # Кількість днів для перевірки на наближені дні народження
    today = datetime.today().date()
    upcoming_birthdays = []  # Список майбутніх днів народження

    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')
            continue

        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= days:
            if birthday_this_year.weekday() >= 5:  # Якщо день припадає на суботу або неділю, перемістимо його на наступний понеділок
                delta = (7 - birthday_this_year.weekday())
                birthday_this_year += timedelta(days=delta)

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays
upcoming_birthdays = get_upcoming_birthdays(users=[
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.10"},
    {'name': 'Mohel Smith', 'birthday': '1995.03.06'},
    {'name': 'John Dark', 'birthday': '1985.03.07'},
    {'name': 'Mary Dark', 'birthday': '1985.03.08'},
    {'name': 'Derek Dark', 'birthday': '1985.03.09'},
    {'name': 'Jane Smith', 'birthday': '1990.03.10'},
    {'name': 'Nick Darsel', 'birthday': '1984.03.11'},
    {'name': 'Liam Smith', 'birthday': '1995.03.12'},
    {'name': 'Mohel Smith', 'birthday': '1995.03.13'},
    {'name': 'John Dark', 'birthday': '1985.03.14'},
    {'name': 'Mary Dark', 'birthday': '1985.03.15'},
    {'name': 'Derek Dark', 'birthday': '1985.03.16'},
    {'name': 'Jane Smith', 'birthday': '1990.03.17'},
])

print("Список привітань на цьому тижні:")
print(*upcoming_birthdays, sep="\n")