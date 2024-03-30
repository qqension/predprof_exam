import csv
import re

def char_to_num(char):
    if char.islower():  # lowercase letters a-z
        return ord(char) - ord('a') + 1
    elif char.isupper():  # uppercase letters A-Z
        return ord(char) - ord('A') + 27
    elif char.isdigit():  # digits
        return int(char) + 52
    elif char == ':':
        return 64
    elif char == '-':
        return 65

def custom_hash(s):
    p = 65
    m = 109 + 9

    n = len(s)
    hash_val = 0

    for i in range(n):
        char_val = char_to_num(s[i])

        if char_val is not None:
            hash_val += char_val * (p ** i)

    return hash_val % m

game_character_hash = {}

with open("game.txt", "r", encoding="utf-8") as file:
    for line in file:
        delimiter = re.findall(r'[^\w\s]', line)[0]  # находим первый символ, который не является буквой, цифрой или пробелом
        data = line.strip().split(delimiter)
        if len(data) == 2:
            game, character = [item.strip() for item in data]
            key = game.replace(" ", "") + character
            game_character_hash[key] = custom_hash(key)
        else:
            print(f"Ignoring line: {line.strip()} - Incorrect format.")




with open("game_with_hash2.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Hash', 'Game', 'Character'])
    for key, hash_val in game_character_hash.items():
        game, character = key[:-len(character)], key[-len(character):]
        writer.writerow([hash_val, game, character])
