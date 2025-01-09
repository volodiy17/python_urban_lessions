first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (
    len(first_el) - len(second_el)
    for first_el, second_el in zip(first, second)
    if len(first_el) != len(second_el)
)

second_result = (
    len(first[index]) == len(second[index])
    for index in range(0, len(first) if len(first) <= len(second) else len(second))
)

print(list(first_result))
print(list(second_result))
