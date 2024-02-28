from collections import defaultdict
house_details = defaultdict(lambda: None, rooms=5, bathrooms=2, garden=True)
print(house_details['garden'])
print(house_details['bedrooms'])