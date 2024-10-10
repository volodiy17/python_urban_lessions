immutable_var = ([2, 1], "string", True)
print("Immutable tuple:", immutable_var)
# написал так, чтобы в комменте описание не писать
try:
    immutable_var[2] = "new_string"
except TypeError:
    print("ERROR: Tuple - не изменяемый тип данных")

mutable_list = [2, 3, 4]
mutable_list[0] = mutable_list[0] + mutable_list[1]
mutable_list[1] = mutable_list[1] + mutable_list[2]
mutable_list[2] = mutable_list[2] + mutable_list[0]
print("Mutable list:", mutable_list)