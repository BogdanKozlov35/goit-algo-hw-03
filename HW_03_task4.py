from datetime import datetime
def get_upcoming_birthdays(users):
    days = 7  # Кількість днів для перевірки на наближені дні народження
    today = datetime.today().date()

    prepared_users = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
            prepared_users.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            print(f'Некоректна дата народження для користувача {user["name"]}')

    upcoming_birthdays = []  # Список майбутніх днів народження
    for user in prepared_users:  # Ітерація по підготовленим користувачам
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:

            if birthday_this_year.weekday() == 6:
                birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day + 1)
            if birthday_this_year.weekday() == 5:
                birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day + 2)

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
        return upcoming_birthdays
upcoming_birthdays = get_upcoming_birthdays(users = [
    {"name": "John Doe", "birthday": "1985.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.10"}
])
print(f"Список привітань на цьому тижні: {upcoming_birthdays}")
