from zipfile import ZipFile
import json


def is_correct_json(json_file):
    try:
        json.loads(file.read().decode('utf-8'))
        json_file.seek(0)
        return True
    except UnicodeDecodeError:
        return False
    except json.decoder.JSONDecodeError:
        return False


with ZipFile('data.zip') as zip_file:
    foot_dict = {}
    info = zip_file.infolist()
    for obj in info:
        if obj.is_dir() is False:
            if obj.filename.split("/")[-1][-5:] == '.json':
                with zip_file.open(obj.filename) as file:
                    if is_correct_json(file):
                        file_dict = json.loads(file.read().decode('utf-8'))
                        if file_dict['team'] == 'Arsenal':
                            foot_dict[file_dict['first_name']] = file_dict['last_name']

    for name, female in sorted(foot_dict.items(), key=lambda x: (x[0], x[1])):
        print(name, female, sep=' ')


