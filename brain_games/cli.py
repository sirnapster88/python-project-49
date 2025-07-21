import prompt


def welcome_user():
    name = prompt.string('May I have Your name? ')
    print('Welcome to the Brain Games!')
    print(f"Hello, {name}!")