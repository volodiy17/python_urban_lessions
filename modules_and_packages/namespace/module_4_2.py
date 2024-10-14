def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        return

    inner_function()
    return


# Вывалится с ошибкой, так как функция inner_function() не существует в данном пространстве имён
try:
    inner_function()
except Exception as e:
    print(e)
