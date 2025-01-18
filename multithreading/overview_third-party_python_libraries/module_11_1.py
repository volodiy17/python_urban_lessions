import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Numpy
array = np.array([1, 2, 3, 4, 5])
print("Массив:", array)

squared = array ** 2
sum_array = np.sum(array)
print("Квадраты элементов массива:", squared)
print("Сумма элементов массива:", sum_array)

random_data = np.random.normal(loc=0, scale=1, size=1000)
print("Пример случайных данных (5 элементов):", random_data[:5])

# 2. Pandas
data = pd.DataFrame({"Value": random_data})

mean_value = data["Value"].mean()
std_value = data["Value"].std()
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_value)

data["Category"] = pd.cut(data["Value"], bins=3, labels=["Low", "Medium", "High"])
grouped = data.groupby("Category").size()
print("Распределение по категориям:")
print(grouped)

# 3. Matplotlib
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(array, squared, label="y = x^2", color="blue")
plt.title("Линейный график")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(random_data, bins=30, color="green", alpha=0.7)
plt.title("Гистограмма случайных данных")
plt.xlabel("Значение")
plt.ylabel("Частота")

plt.tight_layout()
plt.show()
