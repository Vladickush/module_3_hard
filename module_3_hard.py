#
# Подсчёт суммы всех чисел и длин всех строк
def calculate_structure_sum(data_structure):
    record = str(data_structure)  # перевод списка в строку и удаление всех скобок, пробелов и апострофов
    record = record.translate({ord(i): None for i in ' '})
    record = record.translate({ord(i): None for i in '('})
    record = record.translate({ord(i): None for i in ')'})
    record = record.translate({ord(i): None for i in '['})
    record = record.translate({ord(i): None for i in ']'})
    record = record.translate({ord(i): None for i in '{'})
    record = record.translate({ord(i): None for i in '}'})
    record = record.translate({ord(i): None for i in "'"})
    record = record.replace(':', ',')
    record = record.replace(',,', ',')
    record = record.split(',')  # перевод строки в список
    res = 0
    for i in record:
        if i.isdigit():
            res = res + int(i)  # сумма все чисел
        else:
            res = res + len(i)  # сумма длин строк
    return res

data_structure = [
    [1, 2, 3, ],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)




