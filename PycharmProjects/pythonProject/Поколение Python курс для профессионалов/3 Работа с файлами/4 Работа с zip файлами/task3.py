from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    for obj in info:
        if obj.is_dir():
            info.remove(obj)
    print(len(info))