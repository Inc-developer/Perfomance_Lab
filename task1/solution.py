import sys


# Генератор для получения следующего числа из массива
def circle_array(array):
    while True:
        for num in array:
            yield num


def intervals_path(n: int, m: int) -> int:
    array = [i+1 for i in range(n)]
    get_num = circle_array(array)
    intervals = []
    interval = []
    # Добавление первого интервала для дальнейшей работы алгоритма
    if len(intervals) < 1:
        for _ in range(m):
            interval.append(next(get_num))
        intervals.append(interval)
        interval = []
        interval.append(intervals[-1][-1])
    while intervals[-1][-1] != array[0]:
        if len(interval) == m:
            intervals.append(interval)
            interval = []
            interval.append(intervals[-1][-1])
        else:
            interval.append(next(get_num))
    final_path = ''
    for i in intervals:
        final_path += str(i[0])
    return final_path


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(intervals_path(int(sys.argv[1]), int(sys.argv[2])))
    else:
        print("Need 2 args (numbers)")
