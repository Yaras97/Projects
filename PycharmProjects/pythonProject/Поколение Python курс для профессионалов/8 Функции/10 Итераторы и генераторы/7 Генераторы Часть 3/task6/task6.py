def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        planet_info = {}
        for line in file:
            line = line.strip()
            if line:
                key, value = line.split(' = ')
                planet_info[key] = value
            else:
                yield planet_info
                planet_info = {}

planets = txt_to_dict()

print(*planets)