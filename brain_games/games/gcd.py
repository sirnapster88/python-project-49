import random

"""This module implements the game logic for calculating the
greatest common divisor"""

GAME_OBJ = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    """Function with main logic
    that evaluate the GCD"""
    if num2 == 0:
        return num1
    while num2 != 0: 
        num1, num2 = num2, num1 % num2
        #calculante GCD with Evklid algorithm
    return num1


def play_game():
    """Main Function with logic
    that generate random numbers and
    getting correct answer with
    function get_gcd()"""
    comp_an = None
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    comp_an = get_gcd(num1, num2)
    return comp_an, f"{num1} {num2}"
    



    


