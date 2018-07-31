# coding:utf-8
file = open("sms_sample.txt")

LAST = True

if not LAST:
    o = open("filtered_taocan_sms_sample.txt", 'w')
else:
    o = open("filtered_last_sms_sample.txt", 'w')

while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        if "10086" in line[:5] and "流量" in line and "套餐" in line and "流量提醒" in line:
            # if "套餐" in line and "流量" not in line:
            if LAST == True:
                continue

            o.write(line[line.index("|") + 1:])
            o.flush()

        if "验证码" in line:
            if LAST == True:
                continue
            o.write(line)
            o.flush()

        if "动态密码" in line:
            if LAST == True:
                continue
            o.write(line)
            o.flush()

        if LAST == True:
            o.write(line)
            o.flush()

o.close()
file.close()
