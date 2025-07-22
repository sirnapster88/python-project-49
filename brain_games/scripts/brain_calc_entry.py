from brain_games.games import brain_calc
from brain_games.scripts import engine

game_objective = 'What is the result of the expression?'


def main():
    engine.engine_logic(brain_calc.calculator, game_objective)


if __name__ == '__main__':
    main()