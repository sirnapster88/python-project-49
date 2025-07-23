from brain_games import engine
from brain_games.games import gcd

"""Данный модуль является вводточкой входа в программу
brain-gdc, игры по определению наибольшего общего делителя"""


def main():
    engine.engine_logic(gcd)


if __name__ == '__main__':
    main()