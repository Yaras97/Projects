# class Postman:
#     def __init__(self):
#         self.delivery_data = []
#
#     def add_delivery(self,street, house, apart):
#         self.delivery_data.append((street, house, apart))
#
#     def get_houses_for_street(self, street):
#         try:
#             return list(map(lambda x: x[1] ,filter(lambda x: x[0] == street, self.delivery_data)))
#         except:
#             return []
#
#     def get_flats_for_house(self, street, house):
#         try:
#             return list(map(lambda x: x[2] , filter(lambda x:(x[0], x[1]) == (street, house), self.delivery_data)))
#         except:
#             return []

class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        return list({h: None for s, h, _ in self.delivery_data if s == street})

    def get_flats_for_house(self, street, house):
        return list({a: None for s, h, a in self.delivery_data if s == street and h == house})

postman = Postman()
postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)
print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))