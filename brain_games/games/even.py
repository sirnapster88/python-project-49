from random import randint

"""This module implements the game logic for detecting an even number."""

GAME_OBJ = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def is_even(random_num):
    """Function with main game logic
    than check is number even or not, 
    and returns True or False"""
    if random_num % 2 == 0:
        return True
    else:
        return False
    

def play_game():
    """Main Function with game logic
    that generate random numbers and
    getting correct answer with
    function is_even()"""
    comp_an = None
    random_num = randint(1, 100) 
    # generate random number from 1 to 100
    if is_even(random_num):
        comp_an = 'yes'
    else:
        comp_an = 'no'
    return comp_an, random_num
