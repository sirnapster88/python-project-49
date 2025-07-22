from brain_games.games import brain_even
from brain_games.scripts import engine

game_objective = "Answer \"yes\" if the number is even, otherwise answer \"no\""


def main():
    engine.engine_logic(brain_even.is_even, game_objective)


if __name__ == '__main__':
    main()