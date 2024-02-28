import datetime
t = datetime.datetime.now()
print(t)

print('Сегодня {}. Время: {}.'.format(t.date(), t.time()))

print("Год {}, месяц {}, день {}, {} ч. {} мин. {} сек.".format(t.year,
                                                          t.month,
                                                          t.day,
                                                          t.hour,
                                                          t.minute,
                                                          t.second))