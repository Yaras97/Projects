'''
Создайте приложение FastAPI, которое принимает POST-запрос к конечной станции
(маршруту, адрес странички) `/calculate` с двумя числами (`num1` и `num2`) в качестве входных данных.
Приложение должно ответить суммой двух чисел.

Например, запрос на `/calculate` с `num1=5` и `num2=10` должен вернуть `{"result": 15}` в ответ.
'''

from fastapi import FastAPI

app = FastAPI()


@app.post('/calculate')
async def calculate(num1: float, num2: float):
    return {"result": num1 + num2}


# 1) Создайте html-файл (напр. "index.html"), в тексте которого напишите:
#
# <!DOCTYPE html>
#
# <html lang="ru">
# <head>
#
# <meta charset="UTF-8">
#
# <title> Пример простой страницы html</title>
# </head>
#
# <body>
#
# Я НЕРЕАЛЬНО КРУТ И МОЙ РЕСПЕКТ БЕЗ МЕРЫ :)
# </body>
#
# </html>
# 2) Создайте приложение FastAPI, которое принимает GET-запрос к дефолтной конечной точке
# (маршруту, адресу странички) `/` и возвращает html-страницу.
#
# 3) Сохраните файл и запустите приложение с помощью `uvicorn`:
#
# uvicorn main:app --reload
#
# Откройте 'http://localhost:8000'в вашем веб-браузере.

# from fastapi import FastAPI
# from fastapi.responses import FileResponse
#
# app = FastAPI()
#
#
# @app.get('/')
# async def root():
#     return FileResponse('index.html')


# Алтернативный запуск через файл, а не cmd
# import uvicorn
# if __name__ == '__main__':
#     uvicorn.run(app,
#                 host='127.0.0.1',
#                 port=8000)
