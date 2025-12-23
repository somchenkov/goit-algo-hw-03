import random

def get_numbers_ticket(min, max, quantity):
    numbers = random.sample(range(min, max), quantity) # get the unique numbers in a range of min and max
    return sorted(numbers) #sort numbers and return the value


print(get_numbers_ticket(5, 99, 10))