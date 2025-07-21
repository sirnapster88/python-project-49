from brain_games.scripts.greeting import greet, results
from brain_games.scripts.logic import *
import random
import prompt




def is_prime(num):
    if num <= 1:
        return False
    
    for i in range(2,int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def brain_prime():
    cnt = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    name = greet()
    while cnt < 3:
        num= random.randint(1,50)
        if is_prime(num):
            comp_answ = 'yes'
        else:
            comp_answ = 'no'
        print(f"Question: {num}")
        hum_answ = prompt.string('Your answer: ')
        flag= check(hum_answ, comp_answ)
        if flag == False:
            print(f"{hum_answ} is wrong answer ;(. Correct answer was {comp_answ}.")
            print(f"Let's try again, {name}!")
            break  
        cnt +=1
    if flag == True:
        print(f"Congratulations, {name}!")

def main():
    brain_prime()


if __name__ == '__main__':
    main()

