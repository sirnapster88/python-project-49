from brain_games import engine
from brain_games.games import prime

"""Данный модуль является вводточкой входа в программу
brain-prime, игры по определению простого числа"""


def main():
    engine.engine_logic(prime)


if __name__ == '__main__':
    main()