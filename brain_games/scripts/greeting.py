import prompt

def greet(): #данная функция осуществляет вывод приветсвенных сообщений
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f"{"Hello,"} {name}{"!"}")
    return name

def results(flag, name, hum_answ = None, comp_answ = None):
    if flag == True:
        print(f"Congratulations, {name}!")
    else:
        print(f"{hum_answ} is wrong answer ;(. Correct answer was {comp_answ}.")
        print(f"Let's try again, {name}!")
        exit