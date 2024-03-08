from datetime import datetime
def get_days_from_today(date):
    current_date = datetime.now()
    current_date = current_date.date()
    try:
        target_day = datetime.strptime(date, "%Y-%d-%m")
        target_day = target_day.date()

        delta_date = target_day - current_date

        return delta_date.days

    except ValueError or TypeError:
        print("*** the date isn't correct ***")
        return None

print(get_days_from_today("2024-10-03"))
