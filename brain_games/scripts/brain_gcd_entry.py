from brain_games.games import brain_gcd
from brain_games.scripts import engine

game_objective = 'Find the greatest common divisor of given numbers.'


def main():
    engine.engine_logic(brain_gcd.gcd, game_objective)


if __name__ == '__main__':
    main()