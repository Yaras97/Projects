from collections import namedtuple
Resolution = namedtuple('Resolution', ['horizontal', 'vertical'])
full_hd = Resolution(1920, 1070)
full_hd.vertical = 1080
print(full_hd.vertical)