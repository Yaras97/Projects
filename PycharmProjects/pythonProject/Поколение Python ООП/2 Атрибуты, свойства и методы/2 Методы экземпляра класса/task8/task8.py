class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

array = [(76, 164), (132, 195), (181, 97), (61, 124), (19, 158), (130, 116), (101, 191), (84, 35), (190, 21), (106, 49), (91, 192), (133, 155), (170, 24), (137, 107), (114, 142), (145, 170), (167, 148), (91, 43), (25, 15), (12, 20)]

for x, y in array:
    vector = Vector(x, y)
    print(vector.abs())