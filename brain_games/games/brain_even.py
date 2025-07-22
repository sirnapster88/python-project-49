from random import randint


def even(random_num):
    if random_num % 2 == 0:
        comp_an = 'yes'
    else:
        comp_an = 'no'
    return comp_an


def is_even():
    comp_an = None
    random_num = randint(1, 100) 
    comp_an = even(random_num)
    return comp_an, random_num
