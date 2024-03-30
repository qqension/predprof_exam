import csv

# Открываем файл game.txt для чтения и файл game_new.csv для записи
with open("game.txt", "r", encoding="utf-8") as file, open("game_new.csv", "w", newline='', encoding='utf-8') as new_file:
    csv_writer = csv.writer(new_file, delimiter='$')
    # Проходим по каждой строке файла game.txt
    for line in file:
        data = line.strip().split("$")
        if "55" in line: # Проверяем наличие числа 55 в строке
            game, characters, nameError, date = [item.strip() for item in data]
            # Формируем отчет
            report = f"У персонажа {characters} в игре {game} нашлась ошибка с кодом: {nameError}. Дата фиксации: {date}"
            # Заменяем значение ошибки на "Done" и дату на "0000-00-00"
            data[2] = "Done"
            data[3] = "0000-00-00"
            csv_writer.writerow(data) # Записываем измененные данные в файл game_new.csv
            print(report) # Выводим отчет на экран

print("Отчет создан и данные сохранены в файле game_new.csv.")
