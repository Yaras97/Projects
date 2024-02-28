from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    zip_size = 0
    true_size = 0
    for obj in info:
        zip_size += obj.compress_size
        true_size += obj.file_size
    print(f'Объем исходных файлов: {true_size} байт(а)')
    print(f'Объем сжатых файлов: {zip_size} байт(а)')