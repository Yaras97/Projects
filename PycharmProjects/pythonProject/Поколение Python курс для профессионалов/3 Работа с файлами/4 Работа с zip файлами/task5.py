from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()
    file_dict = {}
    for obj in info:
        if obj.is_dir() is False:
            file_dict[obj.filename.split('/')[-1]] = (obj.compress_size / obj.file_size) * 100
    print(sorted(file_dict.items(), key=lambda x: x[1])[0][0])
