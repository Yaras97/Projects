methods = [str.upper, str.lower, str.title]
text = 'heLLO wORld'
text = methods[0](text)
text = methods[1](text)
text = methods[2](text)
print(text)