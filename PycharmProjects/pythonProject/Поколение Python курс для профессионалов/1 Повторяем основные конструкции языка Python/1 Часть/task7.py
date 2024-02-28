def likes(names):
    if len(names) == 0:
        return 'Никто не оценил данную запись'
    elif len(names) == 1:
        return f'{names[0]} оценил(а) данную запись'
    elif len(names) == 2:
        return f'{names[0]} и {names[1]} оценили данную запись'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} и {names[2]} оценили данную запись'
    else:
        return f'{names[0]}, {names[1]} и {len(names) - 2} других оценили данную запись'


    
# def likes(v):
#     d = {0: "'Никто не оценил'",
#          1: "f'{v[0]} оценил(а)'",
#          2: "f'{v[0]} и {v[1]} оценили'",
#          3: "f'{v[0]}, {v[1]} и {v[2]} оценили'",
#          4: "f'{v[0]}, {v[1]} и {len(v) - 2} других оценили'"}
#     return eval(d.get(len(v), d[4])) + ' данную запись'