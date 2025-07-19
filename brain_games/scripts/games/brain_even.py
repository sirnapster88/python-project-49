from random import randint
import prompt


def is_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have Your name? ')
    print(f"{"Hello,"} {name}{"!"}")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    flag = True
    cnt = 0 #счетчик для определения кол-ва раундов
    while cnt < 3: 
        random_num = randint(1, 100) #генерируем random число
        print(f"Question: {random_num}")
        hum_answ= prompt.string('Your answer: ')
        
        if random_num % 2 == 0:
            comp_answ = 'yes'
        else:
            comp_answ = 'no'
        
        # если число четное и ответ "yes" или число нечетное и ответ "no", пишем "Correct" 
        if hum_answ == comp_answ:
            print('Correct!')
        #если число четное и ответ "no" или число нечетное и ответ "yes", пишем, что игрок ошибся и закрываем игру
        else:
            print(f"{hum_answ} is wrong answer ;(. Correct answer was {comp_answ}.")
            print(f"Let's try again, {name}!")
            flag = False
            break
        #выполняем проверку что если счетчик правильных ответов = 3, то выводим сообщение- поздравление.
        cnt +=1
    if flag == True:
        print(f"Congratulations, {name}!")
                   
def main():
    is_even()

if __name__ == '__main__':
    main()