def merge(values):      # values - это список словарей
    res = {}
    for i in values:
        for k in i:
            res.setdefault(k, set()).add(i[k])
    return res




