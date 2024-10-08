from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data[0:-1])


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов. Мой результат: 0:00:07.990697.

# start = datetime.now()
# for file in filenames:
#     read_info(file)
# end = datetime.now()
# print(f'Линейный вызов: {end - start}')


# Многопроцессный. Мой результат: 0:00:03.690931.
#
# if __name__ == '__main__':
#     start = datetime.now()
#     with multiprocessing.Pool() as pool:
#         pool.map(read_info, filenames)
#     end = datetime.now()
#     print(f'Многопроцессный: {end - start}')
