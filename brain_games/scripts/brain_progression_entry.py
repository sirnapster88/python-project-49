from brain_games.games import brain_progression
from brain_games.scripts import engine

game_objective = 'What number is missing in the progression?'


def main():
    engine.engine_logic(brain_progression.progression, game_objective)


if __name__ == '__main__':
    main()