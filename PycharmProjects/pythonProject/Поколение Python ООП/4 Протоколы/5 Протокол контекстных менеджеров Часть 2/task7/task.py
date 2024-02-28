class WriteSpy:
    def __init__(self, file_1, file_2, to_close=False):
        self.file_1 = file_1
        self.file_2 = file_2
        self.to_close = to_close

    def write(self, text):
        if self.writable():
            self.file_1.write(text)
            self.file_2.write(text)
        else:
            raise ValueError('Файл закрыт или недоступен для записи')

    def close(self):
        self.file_1.close()
        self.file_2.close()

    def writable(self):
        if self.file_1.closed or self.file_2.closed:
            return False
        else:
            if self.file_1.__dict__['mode'] == 'w' and self.file_2.__dict__['mode'] == 'w':
                return True
            return False

    def closed(self):
        if self.file_1.closed and self.file_2.closed:
            return True
        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close:
            self.close()


f1 = open('file1.txt', mode='w')
f2 = open('file2.txt', mode='w')

with WriteSpy(f1, f2, to_close=True) as combined:
    combined.write('You shall seal the blinding light that plagues their dreams\n')
    combined.write('You are the Vessel\n')
    combined.write('You are the Hollow Knight')

print(f1.closed, f2.closed)

with open('file1.txt') as file1, open('file2.txt') as file2:
    print(file1.read())
    print(file2.read())