from brain_games import engine
from brain_games.games import progression

"""Данный модуль является вводточкой входа в программу
brain-calc, игры по определению следующего элемента
прогрессии"""


def main():
    engine.engine_logic(progression)


if __name__ == '__main__':
    main()