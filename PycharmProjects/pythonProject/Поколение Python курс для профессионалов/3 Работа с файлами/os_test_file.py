import os

print(os.name)

# print(*os.environ.items(), sep='\n')
print(os.getenv("TMP"))
print(os.getcwd())
print(os.path.exists(
    "/Поколение Python курс для профессионалов/3 Работа с файлами/os_test_file.py"))
print(os.path.isfile(
    "/Поколение Python курс для профессионалов/3 Работа с файлами/os_test_file.py"))
print(os.path.isdir(
    "/Поколение Python курс для профессионалов/3 Работа с файлами/os_test_file.py"))

# os.makedirs(r"D:/folder/first/second/third")

# os.startfile(r"C:/Program Files/Google/Chrome/Application/chrome.exe")

print(os.path.basename("C:/Program Files/Google/Chrome/Application/chrome.exe"))
print(os.path.dirname("C:/Program Files/Google/Chrome/Application/chrome.exe"))
print(os.path.getsize('C:/Users/Yaras/PycharmProjects/pythonProject'))

print(os.path.split("C:/Program Files/Google/Chrome/Application/chrome.exe"))