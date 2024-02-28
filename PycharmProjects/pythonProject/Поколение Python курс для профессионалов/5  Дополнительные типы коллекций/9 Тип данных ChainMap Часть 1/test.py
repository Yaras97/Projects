from collections import ChainMap
for_adoption = {'dogs': 15, 'cats': 8, 'pythons': 9}
vet_treatment = {'dogs': 7, 'cats': 2, 'tigers': 3}
pets = ChainMap(for_adoption, vet_treatment)
print(pets)
for_adoption['dogs'] = 10000
for_adoption['lions'] = 9
vet_treatment['cats'] = 'fasdf'
print(pets)