from datetime import datetime
def get_days_from_today():
    try:
        date = input("Enter the date in the format YYYY-MM-DD: ")
        target_day = datetime.strptime(date, "%Y-%d-%m")
        target_day = target_day.date()

        current_date = datetime.now()
        current_date = current_date.date()

        delta_date = target_day - current_date

        print(f"The {delta_date.days} days left after today")
        return delta_date.days
        print(f"The {delta_date.days} day(s) left after today")
    except ValueError:
        print("*** the date isn't correct ***")
        return get_days_from_today()

get_days_from_today()
