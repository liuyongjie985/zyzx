# coding:utf-8
file = open("data/TotalData.txt")

LAST = False

if not LAST:
    o = open("output/filtered_sms_sample.txt", 'w')
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

            try:
                o.write(line[line.index("|") + 1:])
            except:
                o.write(line)
            o.flush()

        if "验证码" in line or "校验码" in line or "动态密码" in line:
            if LAST == True:
                continue
            o.write(line)
            o.flush()

        if "火车" in line or "飞机" in line or "航班" in line:
            if LAST == True:
                continue
            o.write(line)
            o.flush()

        if "水力" in line or "电力" in line or "水费" in line or "电费" in line or "用水量" in line or "用电量" in line:
            if LAST == True:
                continue
            o.write(line)
            o.flush()

        if LAST == True:
            o.write(line)
            o.flush()

o.close()
file.close()
