import random

def get_numbers_ticket(min, max, quantity):
    """
    numbers = []
    while quantity != 0:
        if min >= 1 and max <= 1000:
            numbers.append(int(random.uniform(min, max)))
        quantity -= 1
    """
    numbers = random.sample(range(min, max), quantity)
    return sorted(numbers)

print(get_days_from_today("2021.10-09"))