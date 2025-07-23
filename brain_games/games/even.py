from random import randint


game_obj = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def even(random_num):
    if random_num % 2 == 0:
        return True
    else:
        return False
    


def game():
    comp_an = None
    random_num = randint(1, 100) 
    comp_an = even(random_num)
    if even(random_num):
        comp_an = 'yes'
    else:
        comp_an = 'no'
    return comp_an, random_num
