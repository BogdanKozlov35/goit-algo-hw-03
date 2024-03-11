import random
def get_numbers_ticket(min: int, max: int, quantity: int):

    all_num = []
    if max <= 1000:
        if min >= 1:
            if 1 <= quantity <= (max - min + 1):
                for num in range(min, (max +1)):
                    all_num.append(num)
                lottery_numbers = random.sample(all_num, quantity)
                lottery_numbers.sort()
                return lottery_numbers
    else:
        return all_num

lottery_numbers = get_numbers_ticket(10, 20, 5)
print("Ваші лотерейні числа:", lottery_numbers)
