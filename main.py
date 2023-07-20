# завдання №2
import math
a = 1
b = 5
c = 4
x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
print (int(x1))
print (int(x2))

#завдання №3
name = input("Введіть ваше ім'я: ")
print(f"Привіт, {name}!")

#завднання №4
hryvnia = float(input("Введіть кількість гривень:"))
kyrs = 37.50
usd = hryvnia / kyrs
print(f"Станом на 15 липня 2022 року це становить {usd:.2f} Долари США.")

#завднання №5
snake_case_str = input("Введіть рядок у форматі snake_case (з 3-ма словами): ")
words = snake_case_str.split('_')
capitalized_camel_case = ''.join([word.capitalize() for word in words])
print(capitalized_camel_case)

#завднання №6 (не осилилив, потрібна допомога)


#завднання №7
#спосіб №1
number_str = input("Введіть трьохзначне число: ")
result = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
print(f"Сума цифр числа: {result}")

#спосіб №2
#Поки в роздумах


