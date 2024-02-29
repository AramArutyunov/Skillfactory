def binary_search(array, element, left, right):
    if left > right: 
        return False
    middle = (right+left) // 2 
    if array[middle] < element and array[middle+1] >= element: 
        return middle, middle+1 
    elif array[middle] >= element: 
        return binary_search(array, element, left, middle-1)
    else: 
        return binary_search(array, element, middle+1, right)

def insertion_sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array

try:
    array = input("Введите последовательность чисел через пробел: ").split()
    array = [float(x) for x in array] 

    # Проверка на то, что минимальное и максимальное значения последовательности не равны
    if min(array) == max(array):
        print("Ошибка: минимальное и максимальное значению последовательности чисел равны.")
    else:
        number = float(input("Введите любое число: "))
        
        # Проверка на то, что введенное число больше минимального значения последовательности чисел
        if number <= min(array):
            print("Ошибка: введенное число меньше либо равно минимальному значению в последовательности чисел.")
        else:
            # Проверка на попадание в пределы последовательности чисел
            if number > max(array):
                print("Ошибка: введенное число не попадает в пределы последовательности чисел.")
            else:   
                sorted_array = insertion_sort(array)
                print("Отсортированный список:", sorted_array)
                left_index, right_index = binary_search(sorted_array, number, 0, len(sorted_array) - 1)
                    
                print("Индекс ближайшего меньшего элемента:", left_index)
                print("Индекс ближайшего большего или равного элемента:", right_index)
except ValueError:
    print("Ошибка: введены некорректные данные.")
