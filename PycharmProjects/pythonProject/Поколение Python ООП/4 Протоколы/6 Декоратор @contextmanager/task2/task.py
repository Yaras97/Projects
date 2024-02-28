from contextlib import contextmanager
import sys

@contextmanager
def reversed_print():
    class ReversedStream:
        def __init__(self, target):
            self.target = target

        def write(self, text):
            self.target.write(text[::-1])

    original_stdout = sys.stdout
    try:
        sys.stdout = ReversedStream(sys.stdout)
        yield
    finally:
        sys.stdout = original_stdout


with reversed_print():
    print('python')
    print('beegeek')

print('Вывод вне блока with')