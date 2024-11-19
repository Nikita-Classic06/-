from time import sleep, time
import threading

# Объявление функции write_words
def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза в 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")

# Взятие текущего времени перед вызовом функций
start_time = time()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени после вызова функций
end_time = time()
print(f"Работа потоков {end_time - start_time:.6f} секунд")

# Взятие текущего времени перед запуском потоков
start_time_threads = time()

# Создание потоков
threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))
thread.join()
# Запуск потоков
for thread in threads:
    thread.start()

# Ожидание завершения всех потоков
for thread in threads:
    thread.join()

# Взятие текущего времени после завершения потоков
end_time_threads = time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")