import random

import prompt

from brain_games.scripts.greeting import greet
from brain_games.scripts.logic import check


def progression_generator():
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
    return question, comp_answ


def progression():
    cnt = 0
    print('What number is missing in the progression?')
    name = greet()
    while cnt < 3:
        question, comp_an = progression_generator()
        print(f"Question: {question}")
        hum_an = prompt.integer('Your answer: ')
        flag = check(int(hum_an), int(comp_an))
        if not flag:
            print(f"{hum_an} is wrong answer ;(. Correct answer was {comp_an}.")
            print(f"Let's try again, {name}!")
            break
        cnt += 1
    if flag:
        print(f"Congratulations, {name}!")


def main():
    progression()


if __name__ == '__main__':
    main()
