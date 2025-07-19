from brain_games.scripts.greeting import greet, results
import random, prompt

def check(hum_answ,comp_answ): #данная функция будет выполнять сверку введенного пользователем рез-та
    flag = True
    if hum_answ == comp_answ:
        print('Correct!')
        return flag
    else:
        flag = False
        return flag


def brain_calc_logic():
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
        flag = check(hum_answ, comp_answ)
        if flag == False:
            break    
        cnt +=1
    results(flag= flag, hum_answ=hum_answ, comp_answ= comp_answ)