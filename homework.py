# 1. Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок
# и постарайтесь устранить ошибку.

number = None

while True:
    number = int(input('Введите число: '))
    if number > 0 and number <= 10:
        break
    print('Попробуйте ввести другое число')
print('Все правильно число больше 0 и меньше или равно 10')