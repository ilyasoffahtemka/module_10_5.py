import time
from multiprocessing import Pool

# Функция для считывания данных из файла
def read_info(name):
    all_data = []  # Локальный список для хранения данных
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, прекращаем чтение
                break
            all_data.append(line)  # Добавляем строку в список (эмуляция обработки данных)


if __name__ == "__main__":
    # Список файлов
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]  # Замените на актуальные имена файлов

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f"Линейный вызов: {end_time - start_time:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)  # map вызывает read_info для каждого файла
    end_time = time.time()
    print(f"Многопроцессный вызов: {end_time - start_time:.6f} секунд")