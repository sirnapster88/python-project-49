from brain_games.scripts.greeting import greet, results
from brain_games.scripts.logic import *
import random
import prompt


def nod(num1,num2):
    if num2 == 0:
        return num1
    while num2 != 0:
       num1, num2= num2,num1 % num2
    return num1




def gcd():
    cnt = 0
    print('Find the greatest common divisor of given numbers.')
    name= greet()
    while cnt < 3:
        num1= random.randint(0, 10)
        num2= random.randint(0, 10)
        comp_answ= nod(num1,num2)
        print(f"Question: {num1} {num2}")
        hum_answ= prompt.integer('Your answer: ')
        flag = check(hum_answ, comp_answ)
        if flag == False:
            print(f"{hum_answ} is wrong answer ;(. Correct answer was {comp_answ}.")
            print(f"Let's try again, {name}!")
            break
        cnt += 1
    if flag== True:
        print(f"Congratulations, {name}!")

def main():
    gcd()


if __name__ == '__main__':
    main()



    


