from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for obj in sorted(info, key=lambda x: x.filename.split("/")[-1]):
        if obj.is_dir() is False:
            t = obj.date_time
            print(f'{obj.filename.split("/")[-1]}\n'
                  f'  Дата модификации файла: {datetime(t[0], t[1], t[2], t[3], t[4], t[5]).strftime("%Y-%m-%d %H:%M:%S")}\n'
                  f'  Объем исходного файла: {obj.file_size} байт(а)\n'
                  f'  Объем сжатого файла: {obj.compress_size} байт(а)')
            print()