import random

import prompt

from brain_games.scripts.greeting import greet
from brain_games.scripts.logic import check


def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def brain_prime():
    cnt = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = greet()
    while cnt < 3:
        num = random.randint(1, 50)
        if is_prime(num):
            comp_an = 'yes'
        else:
            comp_an = 'no'
        print(f"Question: {num}")
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
    brain_prime()


if __name__ == '__main__':
    main()

