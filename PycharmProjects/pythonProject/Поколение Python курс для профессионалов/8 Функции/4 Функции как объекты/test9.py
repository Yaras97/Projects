def countries(country, capital):
    countries.__dict__[country] = capital


countries.__dict__['Germany'] = 'Berlin'
countries.Norway = 'Oslo'
countries('Finland', 'Helsinki')
print(countries.__dict__)
