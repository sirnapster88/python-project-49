from random import randint
from brain_games.scripts.greeting import greet, results
from brain_games.scripts.logic import check
import prompt


def is_even():
    name = greet()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    flag = True
    cnt = 0 #счетчик для определения кол-ва раундов
    while cnt < 3: 
        random_num = randint(1, 100) #генерируем random число
        print(f"Question: {random_num}")
        #hum_answ= prompt.string('Your answer: ')
        
        if random_num % 2 == 0:
            comp_answ = 'yes'
        else:
            comp_answ = 'no'
        
        hum_answ= prompt.string('Your answer: ')
        flag = check(hum_answ, comp_answ)
        if flag == False:
            print(f"{hum_answ} is wrong answer ;(. Correct answer was {comp_answ}.")
            print(f"Let's try again, {name}!")
            break  
        cnt +=1
    if flag == True:
        print(f"Congratulations, {name}!")
                   
def main():
    is_even()

if __name__ == '__main__':
    main()