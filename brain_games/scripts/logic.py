def check(hum_answ, comp_answ):  #данная функция будет выполнять сверку введенного пользователем рез-та
    flag = True
    if hum_answ == comp_answ:
        print('Correct!')
        return flag
    else:
        flag = False
        return flag

