import prompt


def greet():  # данная функция осуществляет вывод приветсвенных сообщений
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f"Hello, {name}!")
    return name
