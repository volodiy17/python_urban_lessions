import os
import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    file_count = 4
    filenames = [f'./file {number}.txt' for number in range(1, file_count + 1)]
    for filename in filenames:
        if not os.path.exists(filename):
            print(f"Файл {filename} не найден.")
            exit(1)

    start_time = time.perf_counter()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.perf_counter() - start_time
    print(f"Линейный вызов: {linear_duration:.6f} секунд")

    start_time = time.perf_counter()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.perf_counter() - start_time
    print(f"Многопроцессный вызов: {parallel_duration:.6f} секунд")
