t = "12:30"
def cal_time(time, mins):
    h, m = map(int, time.split(":"))
    temp = int(m) + mins
    while 1:
        if temp < 60:
            m = temp
            break

        if temp >= 60:
            temp -= 60
        h += 1
    return [h, m]
print(cal_time(t, 90))