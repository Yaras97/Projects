import sys

height_list = [int(line) for line in sys.stdin]
print(f'Рост самого низкого ученика: {min(height_list)}\n'
      f'Рост самого высокого ученика: {max(height_list)}\n'
      f'Средний рост: {sum(height_list) / len(height_list)}')