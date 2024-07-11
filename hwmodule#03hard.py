data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    summa = 0
    if isinstance(data, str):
        return len(data)
    elif isinstance(data, (int, float)):
        return data
    elif isinstance(data, (list, set, tuple)):
        for i in data:
            summa += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for k, v in data.items():
            summa += calculate_structure_sum(k)
            summa += calculate_structure_sum(v)
    return summa


result = calculate_structure_sum(data_structure)
print(result)
