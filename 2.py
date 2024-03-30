with open('game.txt', 'r', encoding='utf-8') as file:
    data = [line.strip().split('$') for line in file]

# Сортировка данных по столбцу игры
data_sorted = sorted(data, key=lambda x: x[0])

# Подсчет количества багов в каждой игре
game_bugs = {}
for row in data_sorted:
    game = row[0]
    if game not in game_bugs:
        game_bugs[game] = 1
    else:
        game_bugs[game] += 1

# Вывод отчета
with open('report.txt', 'w', encoding='utf-8') as report_file:
    for game, count in game_bugs.items():
        report_file.write(f"{game} - количество багов: {count}\n")
