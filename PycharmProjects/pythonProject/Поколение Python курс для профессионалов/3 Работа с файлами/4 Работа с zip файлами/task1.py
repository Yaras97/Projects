from zipfile import ZipFile

with ZipFile('test/test.zip') as zip_file:
    zip_file.printdir()