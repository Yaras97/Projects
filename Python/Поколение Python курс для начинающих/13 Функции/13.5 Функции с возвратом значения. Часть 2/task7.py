# объявление функции
def is_valid_password(password):
    a=password.split(':')
    if len(a)!=3:
        return False
    if a[0][:]!=a[0][::-1]:
        return False
    if len([i for i in range(1,int(a[1])+1) if int(a[1])%i==0])!=2:
        return False
    if int(a[2])%2!=0:
        return False
    else:
        return True

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))