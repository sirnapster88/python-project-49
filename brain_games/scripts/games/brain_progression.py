from brain_games.scripts.greeting import greet
from brain_games.scripts.logic import check
import random, prompt


def progression_generator():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    lenght = random.randint(5, 10)

    hid_num = random.randint(0, lenght-1)

    progression = []
    for index in range (lenght):
        current_element = start + index * step
        progression.append(str(current_element))
    
    comp_answ= progression[hid_num]
    progression[hid_num] = '..'
    question= " ".join(progression)
    return question, comp_answ

def progression():
    cnt = 0
    print('What number is missing in the progression?')
    name = greet()
    while cnt < 3:
        question, comp_answ = progression_generator()
        print(f"Question: {question}")
        hum_answ = prompt.integer('Your answer: ')
        flag = check(int(hum_answ), int(comp_answ))
        if flag == False:
            print(f"{hum_answ} is wrong answer ;(. Correct answer was {comp_answ}.")
            print(f"Let's try again, {name}!")
            break
        cnt += 1
    if flag:
        print(f"Congratulations, {name}!")


def main():
    progression()


if __name__ == '__main__':
    main()
