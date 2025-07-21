import random, prompt

def check(hum_answ, comp_answ):  # данная функция будет выполнять сверку рез-та
    flag = True
    if hum_answ == comp_answ:
        print('Correct!')
        return flag
    else:
        flag = False
        return flag


def brain_calc():
    operators = ['+', '-', '*']
    flag = True
    cnt = 0
    while cnt < 3:
        num1 = random.randint(1, 5)
        num2 = random.randint(1, 5)
        oper_symb = random.choice(operators)
        print(f"Question: {num1} {oper_symb} {num2}")
        hum_an = prompt.integer('Your answer: ')
        if oper_symb == '+':
            comp_an = num1 + num2
        if oper_symb == '-':
            comp_an = num1 - num2
        if oper_symb == '*':
            comp_an = num1 * num2
        flag = check(hum_an, comp_an)
        if not flag:
            print(f"{hum_an} is wrong answer ;(. Correct answer was {comp_an}.")
            return False
            exit 
        cnt += 1
    return flag