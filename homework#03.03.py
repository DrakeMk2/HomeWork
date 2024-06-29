def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


values_list = ['Tree', True, 3]
values_list_2 = [77, 'Two Axes']
values_dict = {'a': True, 'b': 3, 'c': 'Tree'}

print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
