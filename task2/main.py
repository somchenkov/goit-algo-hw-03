import random

def get_numbers_ticket(min, max, quantity):
    numbers = []
    try:
        #check if the min and max are within the parameters, and the quantity is not more then the actual numbers
        if min >= 1 and max <= 1000 and min < max and max - min > quantity:
            numbers = random.sample(range(min, max), quantity) # get the unique numbers in a range of min and max
            return sorted(numbers) #sort numbers and return the value
    except ValueError:
        return numbers


print(get_numbers_ticket(-4, 53, 5))