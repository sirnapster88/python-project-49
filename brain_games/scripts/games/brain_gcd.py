import random

import prompt

from brain_games.scripts.greeting import greet
from brain_games.scripts.logic import check


def nod(num1, num2):
    if num2 == 0:
        return num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1


def gcd():
    cnt = 0
    print('Find the greatest common divisor of given numbers.')
    name = greet()
    while cnt < 3:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        comp_an = nod(num1, num2)
        print(f"Question: {num1} {num2}")
        hum_an = prompt.integer('Your answer: ')
        flag = check(hum_an, comp_an)
        if not flag:
            print(f"{hum_an} is wrong answer ;(. Correct answer was {comp_an}.")
            print(f"Let's try again, {name}!")
            break
        cnt += 1
    if flag:
        print(f"Congratulations, {name}!")


def main():
    gcd()


if __name__ == '__main__':
    main()



    


