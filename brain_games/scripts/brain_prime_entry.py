from brain_games.games import brain_prime
from brain_games.scripts import engine

game_obj = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def main():
    engine.engine_logic(brain_prime.brain_prime, game_obj)


if __name__ == '__main__':
    main()