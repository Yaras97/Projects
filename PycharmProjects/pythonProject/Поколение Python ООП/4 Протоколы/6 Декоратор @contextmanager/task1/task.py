from contextlib import contextmanager

@contextmanager
def make_tag(tag):
    print(tag)
    yield
    print(tag)

with make_tag('*' * 20), make_tag(' ' * 5 + '-' * 10), make_tag(' ' * 7 + '=' * 6):
    print(' ' * 7 + 'привет')