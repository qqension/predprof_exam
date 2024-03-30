def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = []

    # Бинарный поиск
    while left <= right:
        mid = (left + right) // 2
        if arr[mid][1] == target:
            result.append(arr[mid][0])
            # Поиск индексов всех элементов с данным значением
            i = mid - 1
            while i >= 0 and arr[i][1] == target:
                result.append(arr[i][0])
                i -= 1
            i = mid + 1
            while i < len(arr) and arr[i][1] == target:
                result.append(arr[i][0])
                i += 1
            return result[:5] if len(result) > 5 else result
        elif arr[mid][1] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


# Считывание данных из файла и формирование списка
with open('game.txt', 'r', encoding='utf-8') as file:
    data = [line.strip().split('$') for line in file]

# Сортировка данных по имени персонажа для бинарного поиска
data.sort(key=lambda x: x[1])

# Ввод имени персонажа и поиск соответствующих игр
while True:
    search_name = input("Введите имя персонажа (для выхода введите 'game'): ")
    if search_name == 'game':
        break

    result = binary_search(data, search_name)

    if result:
        print(f"Персонаж {search_name} встречается в играх:")
        for game in result:
            print(game)
    else:
        print("Этого персонажа не существует.")
