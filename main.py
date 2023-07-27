a = input("a storona")
b = input("Введите сторону b: ")
c = input("Введите сторону c: ")
if a + b > c and b + c > a and a + c > b:
        print('Треугольник существует')
        if a == b == c:
            print('Треугольник равносторонний')
        elif a == b or b == c or c == a:
            print('Треугольник равнобедренный')
        else:
            print('Треугольник разносторонний')
else:
        print('Такого треугольника не существует')