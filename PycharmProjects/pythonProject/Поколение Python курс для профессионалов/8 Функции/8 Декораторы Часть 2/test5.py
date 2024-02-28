def add_smiley_face(face):
    def smiley_face_decorator(func):
        def wrapper():
            return func() + ' ' + face
        return wrapper
    return smiley_face_decorator
@add_smiley_face('^~^')
def beegeek():
    return 'beegeek'
print(beegeek())