from random import randint

import prompt

from brain_games.scripts.greeting import greet
from brain_games.scripts.logic import check


def is_even():
    name = greet()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    flag = True
    cnt = 0  # счетчик для определения кол-ва раундов
    while cnt < 3: 
        random_num = randint(1, 100)  # генерируем random число
        print(f"Question: {random_num}")
       
        if random_num % 2 == 0:
            comp_an = 'yes'
        else:
            comp_an = 'no'
        
        hum_an = prompt.string('Your answer: ')
        flag = check(hum_an, comp_an)
        if not flag:
            print(f"{hum_an} is wrong answer ;(. Correct answer was {comp_an}.")
            print(f"Let's try again, {name}!")
            break 
        cnt += 1
    if flag:
        print(f"Congratulations, {name}!")


def main():
    is_even()


if __name__ == '__main__':
    main()