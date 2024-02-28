from zipfile import ZipFile
zip_file = open('test/test.zip')
print(type(zip_file))


with ZipFile('test/test.zip') as zip_file:
    pass
print(type(zip_file))


zip_file = ZipFile('test/test.zip')
print(type(zip_file))


with open('test/test.zip') as zip_file:
    pass
print(type(zip_file))