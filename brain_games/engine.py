import prompt

"""Данный модуль осуществляет выполнение роль движка всех
игр используемых в проекте brain_games"""

ROUND_COUNT = 3


def engine_logic(game_module):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game_module.GAME_OBJ)
    win = True
    cnt = 0
    while cnt < ROUND_COUNT:
        corr_an, question = game_module.play_game()
        print(f"Question: {question}")
        hum_an = prompt.string('Your answer: ')
        if str(corr_an) != hum_an:
            print(f"{hum_an} is wrong answer ;(. Correct answer was {corr_an}.")
            print(f"Let's try again, {name}!")
            win = False
            break 
        else:
            print('Correct!')
            cnt += 1
    if win:
        print(f"Congratulations, {name}!")

