                            #1
def distance(x1, y1, x2, y2):
    res = ((x2-x1)//2 + (y2 - y1)//2) ** 0.5
    return res


x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
print(distance(x1, y1, x2, y2))

                            #3 Числа Фибоначчи
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input())))

                            #2
def power(a, n):
    while n > 1:
        a += a
        n -= 1
    return a

                            #4 Високосный год

while True:

    def is_year_leap(x):

        if x % 4 == 0:
            if x % 400 == 0:
                print('True')
            elif x % 100 != 0:
                print('True')
            else:
                print('False')
        else:
            print('False')


    is_year_leap(int(input('Введите год: ')))

                            #5 Квадрат
def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5

    k = (p, s, d)

    return k


print(square(16))

                            #6  Времена года

def season(moth):

    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    else:
        return "Осень"



month = input("Введите месяц(число):")

while True:
    if not month.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

month = int(month)
while True:
    if month == 0:
        print("Такого месяца несуществует")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

month = int(month)

answer = season(month)
print(answer)


                                #7 Банковский вклад

n = int(input())
m = int(input())
y = int(input())

def bank(n, m, y):
        nal = n
        year = y
        def money():
            if year >0:
                nal = n*1.1+m
                year = year -1
                return money()
            else:
                return nal

print (nal)

#8 Простые числа    

from cmath import sqrt


def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    if number == 0 or number == 1:
        return False
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:
            return False
    return True

n = int(input('Введите число: '))
print(is_prime(n))

                                #9  Правильная дата
def is_year_leap(year):

    if year % 400 == 0:
        return True

    if year % 4 == 0 and year % 100 != 0:
        return True

    return False


def date(day, month, year):
    day_in_month = {1: 31,
                    2: 29 if is_year_leap(year) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True
    return False


