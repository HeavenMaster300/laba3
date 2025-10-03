from decimal import Decimal, ROUND_HALF_UP

#создайте список квадратов чисел от 1 до 10 с использованием list comprehension
squares = [x**2 for x in range(1, 11)]
print(f"\nСписок квадратов числе от 1 до 10 {squares}\n")

#с помощью list comprehesion получите список только четных чисел из диапозона range(1,20)
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print(f"\nСписок четных чисел в диапазоне от 1 до 20 {even_numbers}\n")

#Дан список слов words = ['python', 'Java', 'c++', 'Rust', 'go']
#Создайте новый список, где все слова будут в верхнем регистре и длиннее 3 слов
words = ['python', 'Java', 'c++', 'Rust', 'go']
upper_long_words = [word.upper() for word in words if len(word) > 3]
print(f"\nСписок, где все слова в верхнем регистре и длиннее 3 слов {upper_long_words}\n")

#Создайте класс-итератор Countdown, который принимает число n и при итерации возвращает числа от n до 1
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Принятие числа от пользователя
n = int(input("Введите число n для создания итерации от n до 1: "))

# Использование итератора
print(f'Итерация от {n} до 1')
for num in Countdown(n):
    print(num)

#Напиши генератор fibonacci(n), который возвращает первые n чисел Фибоначи
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Пример использования
n = int(input("\nВведите количество чисел Фибоначчи: "))
print(f'Последовательность Фибоначи для {n} чисел')
for num in fibonacci(n):
    print(num)

#Калькулятор вкладов
# Ввод данных от пользователя
P = Decimal(input("\nВведите начальную сумму вклада (в рублях): ").replace(',', '.'))
r = Decimal(input("Введите процентную ставку годовых (например, 7.5): ").replace(',', '.'))
t = Decimal(input("Введите срок вклада (в годах): "))

# Расчет итоговой суммы с ежемесячной капитализацией
S = P * (Decimal('1') + r / (Decimal('12') * Decimal('100'))) ** (Decimal('12') * t)

# Округление до 2 знаков после запятой
S = S.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

# Расчет прибыли
profit = S - P

# Вывод результатов
print(f"Итоговая сумма вклада: {S} руб.")
print(f"Общая прибыль: {profit.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)} руб.")