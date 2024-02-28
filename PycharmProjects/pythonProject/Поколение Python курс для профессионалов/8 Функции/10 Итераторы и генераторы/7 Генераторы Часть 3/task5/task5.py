def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            cleaned_line = line.strip()
            if cleaned_line:
                yield cleaned_line if len(cleaned_line) <= 25 else '...'


lines = nonempty_lines('tests_2785662/1.clue')
print(next(lines))
print(next(lines))
print(next(lines))