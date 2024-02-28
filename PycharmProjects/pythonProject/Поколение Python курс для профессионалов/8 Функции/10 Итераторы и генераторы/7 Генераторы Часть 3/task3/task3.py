with open('data.csv', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.strip().split(',') for line in file_lines)
    file_headers = next(line_values)
    line_sum = sum(int(data[1]) for data in line_values if data[2] == 'a')
    print(line_sum)