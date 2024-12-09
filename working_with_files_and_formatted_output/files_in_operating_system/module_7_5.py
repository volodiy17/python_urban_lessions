import os
import time

directory = "./"

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        modification_time = os.path.getmtime(file_path)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time))
        file_size = os.path.getsize(file_path)
        parent_directory = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_directory}')
