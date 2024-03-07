import random
def get_numbers_ticket(min, max, quantity):
    # ввід та перевірка введених чисел
    all_num = []
    if type(min) == int and type(max) == int and type(quantity) == int:

        if quantity >= 1 and quantity <= 6:

            if max >= (1 + quantity) and max <=1000:

                if min >= 1  and min < (max - quantity):
                    for num in range (min, max):
                        all_num.append(num)
                        #print(all_num)
                    lottery_numbers = random.sample(all_num, quantity)
                    lottery_numbers.sort()

                    print(f"Ваші лотерейні числа: {lottery_numbers}")
                else:
                    print("min number out of range")
            else:
                print("max number out of range")
        else:
            print("quantity out of range")

    else:
        return print("use integer numbers")

get_numbers_ticket(1, 60, 5)