import random


game_obj = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def game():
    comp_an = None
    num = random.randint(1, 50)
    if is_prime(num):
        comp_an = 'yes'
    else:
        comp_an = 'no'
    return comp_an, num
    

