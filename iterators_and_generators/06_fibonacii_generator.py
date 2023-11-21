def fibonacci():
    current_num, nex_num = 0, 1
    while True:
        yield current_num
        current_num, nex_num = nex_num, current_num + nex_num