from collections import namedtuple
Country = namedtuple('Country', 'name,capital,president,language,currency')
iceland = Country('Iceland', 'Reykjavik', 'Gwydni Jouhannesson', 'Icelandic', 'Iceland krona')
_, _, *data = iceland
print(data)
print(iceland)