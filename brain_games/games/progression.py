import random

"""This module implements the game logic for determining
the next number in the progression"""

GAME_OBJ = 'What number is missing in the progression?'


def play_game():
    """Function with main game logic that
    generate random numbers for progression
    get hidden element of progression and
    hide it for user, and then returns correct
    answer"""
    # generate parametrs of random progression
    start = random.randint(1, 10)  
    step = random.randint(1, 5)  
    lenght = random.randint(5, 10)  
    # get hidden element of progression
    hid_num = random.randint(0, lenght - 1)  

    progression = []
    # fill progression with elements
    for index in range(lenght):
        current_element = start + index * step
        progression.append(str(current_element))
    # get hidden element of progression and correct answer
    comp_answ = progression[hid_num]  
    progression[hid_num] = '..'
    question = " ".join(progression)
    return comp_answ, question, 


