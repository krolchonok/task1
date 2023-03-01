
def clear():
    print('\n' * 50)
    
def getnumber():
    print('''Выберите тип вагона:
            1 - Плацкартный вагон
            2 - Купейный вагон
            3 - Вагон СВ
            ''')
    a = input('Введите цифру: ')
    if check(a) == False:
        return False
    else:
        return(a)

def getnubmerplace(c):
    if c == 1:
        n = input('Выберите номер места (1-54): ')
    elif c == 2:
        n = input('Выберите номер места (1-36): ')
    elif c == 3: 
        n = input('Выберите номер места (1-18): ')
    if checknubmerplace(c, n) == False:
        return False
    else:
        return n

def checknubmerplace(c, n):
    try:
        int(n)
    except:
        clear()
        print('\nНу написанно, ввести цифру, давайте по новой, я верю что получится!\n')
        return False
    n = int(n)
    if c == 1:
        if n not in range(1, 55):
            clear()
            print('Не попали, пробуем по новой')
            return False
    elif c == 2:
        if n not in range(1, 37):
            clear()
            print('Не попали, пробуем по новой')
            return False
    elif c == 3:
        if n not in range(1,19):
            clear()
            print('Не попали, пробуем по новой')
            return False

def check(a):
    typelist = [1,2,3]
    
    try:
        int(a)
    except:
        clear()
        print('\nНу написанно, ввести цифру, давайте по новой, я верю что получится!\n')
        return False
    if int(a) in typelist:
        return 'OK'
    else:
        clear()
        print('\nНадеюсь просто опечатка, давайте еще раз!\n')
        return False
    
def calc(c,v):
    print('\nИнформация о месте:\n====================')
    if c == 1:
        if v < 37:
            print('Номер места: ' + str(v))
            if v % 4 == 0:
                print('Номер купе: ' + str(v // 4))
            else:
                print('Номер купе: ' + str(v // 4 + 1))
            if v % 2 == 0:
                print('Полка: Верхняя')
            else:
                print('Полка: Нижняя')
        else:
            print('Номер места: ' + str(v))
            v = v - 36
            if v % 2 == 0:
                print('Номер купе: ' + str(10 - (v // 2)))
                print('Полка: Верхняя')
            else:
                print('Номер купе: ' + str(10 - (v // 2 + 1)))
                print('Полка: Нижняя')
    elif c == 2:
        print('Номер места: ' + str(v))
        if v % 4 == 0:
            print('Номер купе: ' + str(v // 4))
        else:
            print('Номер купе: ' + str(v // 4 + 1))
        if v % 2 == 0:
            print('Полка: Верхняя')
        else:
            print('Полка: Нижняя')
    else:
        print('Номер места: ' + str(v))
        if v % 2 == 0:
            print('Номер купе: ' + str(v // 2))
            print('Полка: Правая')
        else:
            print('Номер купе: ' + str(v // 2 + 1))
            print('Полка: Левая')
    print('====================')
    
def main():
    clear()
    
    c = False
    while c == False:
        c = getnumber()
    c = int(c)
    v = False
    while v == False:
        v = getnubmerplace(c)
    v = int(v)
    calc(c,v)
    

if __name__ == '__main__': # просто красиво и чтобы не пойми откуда не вызывали
    main()
