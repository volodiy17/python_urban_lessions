def apply_all_func(int_list: list[int | float], *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
