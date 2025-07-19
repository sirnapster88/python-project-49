import random
import prompt, operator


def calculator():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f"{"Hello,"} {name}{"!"}")
    print("What is the result of the expression?")
    operators = ['+','-','*']
    flag = True
    cnt = 0
    while cnt < 3:
        num1= random.randint(1, 5)
        num2= random.randint(1, 5)
        oper_symb= random.choice(operators)
        print(f"Question: {num1}{oper_symb}{num2}")
        hum_answ = prompt.integer('Your answer: ')
        if oper_symb == '+':
            comp_answ = num1 + num2
        if oper_symb == '-':
            comp_answ = num1 - num2
        if oper_symb == '*':
            comp_answ = num1 * num2
        if hum_answ == comp_answ:
            print('Correct!')
        else:
            print(f"{hum_answ} is wrong answer ;(. Correct answer was {comp_answ}.")
            print(f"Let's try again, {name}!")
            flag = False
            break
        cnt +=1
    if flag == True:
        print(f"Congratulations, {name}!")

def main():
    calculator()


if __name__ == '__main__':
    main()