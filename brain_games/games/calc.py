import random

"""This module implements the logic of the calculator game."""

GAME_OBJ = 'What is the result of the expression?'


def calc(num1, num2, oper_symb):
    """Function with main game login
    that returns correct answer"""
    if oper_symb == '+':
        comp_an = num1 + num2
    if oper_symb == '-':
        comp_an = num1 - num2
    if oper_symb == '*':
        comp_an = num1 * num2
    return comp_an


def play_game():
    """Function, that generate the question
    to user with random numbers and
    randon arithmetic symbol from list"""
    operators = ['+', '-', '*']  # list with symbols of arithmetic operations
    comp_an = None
    # generate numbers for question
    num1 = random.randint(1, 5) 
    num2 = random.randint(1, 5)
    # generate symbol of arithmetic operation
    oper_symb = random.choice(operators)
    comp_an = calc(num1, num2, oper_symb)
    # return question for user and correct answer
    return comp_an, f"{num1} {oper_symb} {num2}"
