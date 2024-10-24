def custom_write(file_name: str, strings: list[str]):
    result = {}
    file = open(file_name, 'w+', encoding="utf-8")
    for i in range(1, len(strings) + 1):
        result.update({(i, file.tell()): strings[i - 1]})
        file.write(strings[i - 1] + '\n')
    file.close()
    return result


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
