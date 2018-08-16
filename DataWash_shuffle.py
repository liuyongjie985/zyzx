# coding:utf-8
file = open("data/TotalData.txt")

LAST = False

my_dict = {}

class_list = []

count = 100

for x in xrange(10):
    class_list.append(0)


def put(word):
    if not my_dict.has_key(word):
        my_dict[word] = 1


while 1:
    lines = file.readlines(100000)
    if not lines:
        break
    for line in lines:
        if "流量" in line and "套餐" in line and "流量提醒" in line:
            if LAST == True:
                continue
            if class_list[0] >= count:
                continue
            class_list[0] += 1
            put(line)
            continue

        if "验证码" in line or "校验码" in line or "动态密码" in line:
            if LAST == True:
                continue
            if class_list[1] >= count:
                continue
            class_list[1] += 1
            put(line)
            continue

        if "火车" in line or "飞机" in line or "航班" in line:
            if LAST == True:
                continue
            if class_list[2] >= count:
                continue
            class_list[2] += 1
            put(line)
            continue

        if "水力" in line or "电力" in line or "水费" in line or "电费" in line or "用水量" in line or "用电量" in line:
            if LAST == True:
                continue
            if class_list[3] >= count:
                continue
            class_list[3] += 1
            put(line)
            continue

        if "话费余额" in line or "账户余额" in line or "当前余额" in line or "话费" in line:
            if LAST == True:
                continue
            if class_list[4] >= count:
                continue
            class_list[4] += 1
            put(line)
            continue

        if "余额不足" in line or "已欠费" in line or "消费" in line:
            if LAST == True:
                continue
            if class_list[5] >= count:
                continue
            class_list[5] += 1
            put(line)
            continue

        if "缴费" in line or "交费" in line or "充值" in line:
            if LAST == True:
                continue
            if class_list[6] >= count:
                continue
            class_list[6] += 1
            put(line)
            continue

        if "支出" in line or "交易" in line or "退款" in line or "票" in line:
            if LAST == True:
                continue
            if class_list[7] >= count:
                continue
            class_list[7] += 1
            put(line)
            continue

        if "签收" in line or "派送" in line or "代收" in line or "派件" in line:
            if LAST == True:
                continue
            if class_list[8] >= count:
                continue
            class_list[8] += 1
            put(line)
            continue

        if "WLAN" in line or "语音" in line or "短信" in line or "优惠" in line or "套餐" in line or "如下功能" in line or "影票" in line or "影片" in line or "放映时间" in line:
            if LAST == True:
                continue
            if class_list[9] >= count:
                continue
            class_list[9] += 1
            put(line)
            continue

        if LAST == True:
            put(line)

file.close()

if not LAST:
    o = open("output/filtered_shuffle_sample.txt", 'w')
else:
    o = open("filtered_last_sms_sample.txt", 'w')

for x in my_dict.items():
    o.write(x[0].strip())
    o.write('\n')

o.close()
