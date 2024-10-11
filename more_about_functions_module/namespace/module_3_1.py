calls = 0


def count_calls():
    global calls
    calls += 1
    return


def string_info(string: str):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return result


def is_contains(string: str, list_to_search: list):
    count_calls()
    for el in list_to_search:
        if string.lower() == el.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
