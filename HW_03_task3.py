import re
def normalize_phone(phone_number):
    sanitized_numbers = []
    for num in phone_number:
        num = re.sub("[^0-9+]", "",num)

        if not num.startswith("+"):
            if num.startswith("380"):
                num = "+" + num
            else:
                num = "+38" + num
        sanitized_numbers.append(num)
    return sanitized_numbers

phone_list = normalize_phone(phone_number = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
        "+380 44 123 4567"
])
print(*phone_list, sep="\n")