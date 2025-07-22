from brain_games.scripts import engine
from brain_games.games import brain_even


game_objective = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def main():
    engine.engine_logic(brain_even.is_even, game_objective)


if __name__ == '__main__':
    main()