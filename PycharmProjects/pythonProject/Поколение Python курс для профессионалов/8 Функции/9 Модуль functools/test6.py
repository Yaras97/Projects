from functools import partial
beegeek = partial(print, 'beegeek', sep=', ')
beegeek('stepik', 'python')