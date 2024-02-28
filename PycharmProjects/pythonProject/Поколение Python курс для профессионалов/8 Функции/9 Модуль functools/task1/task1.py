from functools import partial


def send_email(name, email_address, text):
    message = str(f'В письме для {name} на адрес {email_address} сказано следующее: {text}')
    return message


# Реализация функции to_Timur с использованием partial
to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')

# Реализация функции send_an_invitation с использованием partial
invitation_text = "Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python. тутут...."
send_an_invitation = partial(send_email, text=invitation_text)


print(to_Timur('This is... Requiem. What you are seeing is indeed the truth.'))
