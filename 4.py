import csv

# Считываем данные из файла game.txt и подсчитываем количество упоминаний каждой игры
game_counts = {}
with open('game.txt', 'r',encoding="utf-8") as file:
    for line in file:
        game = line.strip()
        if game in game_counts:
            game_counts[game] += 1
        else:
            game_counts[game] = 1

# Добавляем счетчик к каждой строке файла
games_with_counter = []
with open('game.txt', 'r',encoding="utf-8") as file:
    for line in file:
        game = line.strip()
        count = game_counts[game]
        games_with_counter.append(f"{game}, {count}")

# Записываем данные в новый файл game_counter.csv с дополнительным столбцом "counter"
with open('game_counter.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['game', 'counter'])  # Записываем заголовок
    for game in games_with_counter:
        csv_writer.writerow([game])

