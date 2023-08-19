def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']

    for word in ignore:
        if word in command:
            return True
    return False



