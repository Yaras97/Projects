data = {'Chrome': 'browser', 'Discord': 'messenger', 'Steam': 'digital distributor'}
try:
    try:
        app_name = 'Firefox'
        app_type = data[app_name]
    except:
        raise KeyError('Not found', app_name)
except KeyError as e:
    print(e.args)