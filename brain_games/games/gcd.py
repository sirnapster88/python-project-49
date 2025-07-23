import random


game_obj = 'Find the greatest common divisor of given numbers.'


def nod(num1, num2):
    if num2 == 0:
        return num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def game():
    comp_an = None
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    comp_an = nod(num1, num2)
    return comp_an, f"{num1} {num2}"
    



    


