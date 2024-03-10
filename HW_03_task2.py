import random
def get_numbers_ticket(min: int, max: int, quantity: int):
    # перевірка чисел
    all_num = []
    if quantity <= max and quantity >= min and max <= 1000 and min >=1:
        for num in range (min, max):
            all_num.append(num)
        lottery_numbers = random.sample(all_num, quantity)
        lottery_numbers.sort()
        return lottery_numbers
    else:
        return all_num
lottery_numbers = get_numbers_ticket(1, 55, 6)
print("Ваші лотерейні числа:", lottery_numbers)
