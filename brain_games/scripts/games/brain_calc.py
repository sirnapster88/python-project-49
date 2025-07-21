import random

import prompt

from brain_games.scripts.greeting import greet
from brain_games.scripts.logic import check


def calculator():
    name = greet()
    print("What is the result of the expression?")
    operators = ['+', '-', '*']
    flag = True
    cnt = 0
    while cnt < 3:
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        oper_symb = random.choice(operators)
        print(f"Question: {num1} {oper_symb} {num2}")
        hum_an = prompt.integer('Your answer: ')
        if oper_symb == '+':
            comp_an = num1 + num2
        if oper_symb == '-':
            comp_an = num1 - num2
        if oper_symb == '*':
            comp_an = num1 * num2
        flag = check(hum_an, comp_an) 
        if not flag:
            print(f"{hum_an} is wrong answer ;(. Correct answer was {comp_an}.")
            print(f"Let's try again, {name}!")
            break 
        cnt += 1
    if flag:
        print(f"Congratulations, {name}!")


def main():
    calculator()


if __name__ == '__main__':
    main()