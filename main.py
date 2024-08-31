def calc(line):
    '''
    Считываем файл calc.txt и выводим значения выражений.

    А также выводим информацию, на каких строках выражения некорректны.
    '''
    operand_1, operation, operand_2 = line.split()
    operand_1, operand_2 = int(operand_1), int(operand_2)
    if operation == '+':
        print(f'Результат: {operand_1 + operand_2}')
    if operation == '-':
        print(f'Результат: {operand_1 - operand_2}')
    if operation == '/':
        print(f'Результат: {operand_1 / operand_2}')
    if operation == '//':
        print(f'Результат: {operand_1 // operand_2}')
    if operation == '%':
        print(f'Результат: {operand_1 % operand_2}')
    if operation == '*':
        print(f'Результат: {operand_1 * operand_2}')


with open('calc.txt') as file:
    cnt = 0
    for i in file:
        try:
            cnt += 1
            calc(i)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Ошибка в линии {cnt}, недостаточно значений для распаковки')
            else:
                print(f'Ошибка в линии {cnt}, значение нельзя перевести в число')

