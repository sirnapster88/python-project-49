import random


game_obj = 'What number is missing in the progression?'


def game():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    lenght = random.randint(5, 10)

    hid_num = random.randint(0, lenght - 1)

    progression = []
    for index in range(lenght):
        current_element = start + index * step
        progression.append(str(current_element))
    
    comp_answ = progression[hid_num]
    progression[hid_num] = '..'
    question = " ".join(progression)
    return comp_answ, question, 


