import random

"""This module implements the logic of the game to determine a
prime number"""

GAME_OBJ = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(num):
    """Function with main game logic,
    that check number is it prime or not"""
    if num <= 1:
        return False
    # cicle where realise main logic of checkin for prime
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def play_game():
    """Function with logic that
    generate random numbers from 1 to 50
    and return correct answer"""
    comp_an = None
    num = random.randint(1, 50)
    if is_prime(num):
        comp_an = 'yes'
    else:
        comp_an = 'no'
    return comp_an, num
    

