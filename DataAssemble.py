# coding:utf-8
f = open("result.txt")

target_list = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8"]
middle_list = ["I-1", "I-2", "I-3", "I-4", "I-5", "I-6", "B-7", "B-8"]
explain_list = ["截止时间", "国内通用流量", "省内剩余流量", "套餐外流量剩余", "国内剩余流量", "已使用移动数据流量", "套餐内流量剩余", "验证码"]
sign = []
for x in target_list:
    sign.append(0)
value = []
for x in target_list:
    value.append("")
value_list = []
for x in target_list:
    value_list.append([])
sentence = ""

o = open("result_out", "w")
while 1:
    lines = f.readlines(100000)
    if not lines:
        break
    for line in lines:
        temp = line.split(" ")
        if line == "\n":
            for i, x in enumerate(target_list):
                    sign[i] = 0
                    value_list[i].append(value[i])
                    value[i] = ""
            o.write(sentence)
            o.write("\n")
            o.write("(")
            for j, l in enumerate(explain_list):
                o.write(l)
                o.write(":")
                for p in value_list[j]:
                    o.write(p)
                    o.write("\t")
                o.write("\t")

                value[j] = ""
                value_list[j] = []
                sign[j] = 0

            sentence = ""
            o.write(")")
        else:
            for i, x in enumerate(target_list):
                if temp[1].strip() == x:
                    sign[i] = 1
                if sign[i] == 1 and temp[1] == "O\n":
                    sign[i] = 0
                    value_list[i].append(value[i])
                    value[i] = ""
                if sign[i] == 1:
                    value[i] += temp[0].strip()

        if len(temp) == 2:
            sentence += temp[0]
        else:
            o.write("\n\n")

o.close()
