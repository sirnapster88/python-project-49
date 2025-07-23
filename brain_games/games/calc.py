import random


game_obj = 'What is the result of the expression?'


def game():
    operators = ['+', '-', '*']
    comp_an = None
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    oper_symb = random.choice(operators)
    if oper_symb == '+':
        comp_an = num1 + num2
    if oper_symb == '-':
        comp_an = num1 - num2
    if oper_symb == '*':
        comp_an = num1 * num2
    return comp_an, f"{num1} {oper_symb} {num2}"
