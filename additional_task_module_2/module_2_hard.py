def get_password(number: int):
    result = []
    if number < 3 or number > 20:
        raise ValueError("Number must be greater or equal then 3 and less or equal than 20.")
    for i in range(1, 20):
        for j in range(1, 20):
            if number % (i + j) == 0 and i is not j:
                is_copy = False
                for el in result:
                    if el == f"{i}{j}" or el == f"{j}{i}":
                        is_copy = True
                        break
                if not is_copy:
                    result.append(f"{i}{j}")
    return ''.join(result)


first_number = input("Enter a number from first panel: ")
try:
    print(get_password(int(first_number)))
except ValueError as e:
    print(e)