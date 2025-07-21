from .. import cli
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f"Hello, {name}!")
    #cli.welcome_user()


if __name__ == '__main__':
    main()
    