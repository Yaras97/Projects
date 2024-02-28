from collections import ChainMap

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

chain = ChainMap(bread, meat, sauce, vegetables, toppings)
ingredients = input().split(',')
lenght = max(map(len, ingredients)) + 1
counter = 0
for ingredient in sorted(set(ingredients)):
    print(f'{ingredient:<{lenght}} x {ingredients.count(ingredient)}')
    counter += chain[ingredient] * ingredients.count(ingredient)
print(f"{'-'*(lenght + 4)}\n"
      f"ИТОГ: {counter}р")
