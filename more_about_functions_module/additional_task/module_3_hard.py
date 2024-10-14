def calculate_structure_sum(*args):
    result = 0
    for arg in args:
        if isinstance(arg, int):
            result += arg
        elif isinstance(arg, float):
            result += arg
        elif isinstance(arg, str):
            result += len(arg)
        elif isinstance(arg, tuple):
            result += calculate_structure_sum(*arg)
        elif isinstance(arg, set):
            result += calculate_structure_sum(*arg)
        elif isinstance(arg, list):
            result += calculate_structure_sum(*arg)
        elif isinstance(arg, dict):
            for key, value in arg.items():
                result += calculate_structure_sum(key, value)
        else:
            raise ValueError(f'Unsupported type: {type(arg)}')
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
try:
    result = calculate_structure_sum(data_structure)
    print(result)
except ValueError as e:
    print(e)
