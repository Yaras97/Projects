def message(times):
    if times > 0:
        message(times - 1)
        print(times)

message(5)