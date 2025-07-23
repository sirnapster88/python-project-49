from brain_games import engine
from brain_games.games import even

"""Данный модуль является вводточкой входа в программу
brain-even, игры по выявлению четного числа"""


def main():
    engine.engine_logic(even)


if __name__ == '__main__':
    main()