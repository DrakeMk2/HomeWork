def custom_write(file_name, strings):
    with open(file_name, 'w', encoding='utf-8') as file:
        strings_positions = {}
        string_pos, byte_pos = 1, 0
        for string in strings:
            file.write(string + '\n')
            strings_positions[(string_pos, byte_pos)] = string
            string_pos += 1
            byte_pos = file.tell()
        return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
