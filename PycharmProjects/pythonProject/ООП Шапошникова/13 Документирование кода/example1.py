import example


print(example.Rectangle.__doc__)

print(example.__doc__)

print(help(example.Circle.length))

print(str.__doc__)

import math

print(math.trunc.__doc__)

print(example.Rectangle.__dir__)
print('*******'
      '*******'
      '*******')
a = example.Rectangle(1, 2)
print(dir(a))

print(help('random'))