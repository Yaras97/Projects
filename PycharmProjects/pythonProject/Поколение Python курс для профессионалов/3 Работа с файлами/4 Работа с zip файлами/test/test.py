from zipfile import ZipFile

with ZipFile('test.zip') as zip_file:
    info = zip_file.infolist()
    for file in info:
        name = file.filename.split('/')[-1]
        dr = file.filename.split('/')[0]
        count_space = 0
        if file.is_dir():
            # print(' ', dr)
            print(' ', file.filename)
        elif file.is_dir() is False:
            print(file.filename, file.file_size)
            # print(name, file.file_size)
