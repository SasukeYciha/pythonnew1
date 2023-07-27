def simple():
    i = 2
    counter = 0
    NOT_SIMPLE = 1
    MIN = 0
    MAX = 100000
    while True:
        number = int(input('Введите число в диапозоне от 1 до 100000: '))
        if MIN < number < MAX:
            while i <= number - 1:
                if number % i == 0:
                    counter += 1
                i += 1
            if counter >= NOT_SIMPLE:
                print('Число составное')
            else:
                print('Число простое')
            break
        else:
            print('Недопустимое значение:')