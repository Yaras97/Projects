def log_for(logfile, date_str):
    try:
        with open(logfile, encoding='utf8') as file:
            logs = file.readlines()

        logs = list(map(lambda x: x[len(date_str) + 1:] , filter(lambda x: x[:len(date_str)] == date_str, logs)))
        file_name = 'log_for_' + date_str + '.txt'
        with open(file_name, encoding='utf8', mode='w') as file:
            for log in logs:
                file.write(log)

    except:
        pass


# def log_for(logfile, date_str):
#     with (
#         open(logfile, encoding='utf-8') as file_in,
#         open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as file_out
#     ):
#         for line in file_in:
#             d, *info = line.split()
#             if d == date_str:
#                 print(' '.join(info), file=file_out)