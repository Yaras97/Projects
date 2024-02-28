def sourcetemplate(url):
    def re_args(**kwargs):
        return url + '?' + '&'.join([str(i[0]) + "=" + str(i[1]) for i in sorted(kwargs.items())])

    return re_args


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))