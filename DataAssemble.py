# coding:utf-8
f = open("output/total_train.txt")

my_dict = {"B-1": "截止时间", "B-2": "国内通用流量", "B-3": "省内剩余流量", "B-4": "套餐外流量剩余", "B-5": "国内剩余流量", "B-6": "已使用移动数据流量",
           "B-7": "套餐内流量剩余", "B-8": "验证码", "B-9": "转账金额", "B-10": "尾号", "B-11": "支出", "B-12": "当前余额", "B-13": '存入',
           "B-14": '订单号', "B-15": '出发地', "B-16": '目的地', "B-18": '欠费', "B-19": '电费', "B-20": '用电量', "B-21": '水费',
           "B-22": '用水量', "B-23": '户号', "B-24": '应还款额', "B-25": '最低还款额', "B-26": '最后还款日期', "B-27": '出发日期',
           "B-28": '到达时间', "B-29": '出发时间', "B-30": '航班', "B-31": '乘坐人', "B-32": '状态', "B-33": '出发机场', "B-34": '目的地机场',
           "B-35": '消费时间', "B-36": '账单日期', "B-37": '账单金额', "B-38": '还款日期', "B-39": '付款金额',
           "B-41": '账号后四位', "B-42": '收款人', "B-43": '用途', "B-44": '交易时间', "B-45": "交易类型", "B-46": '交易金额', "B-47": '客服电话',
           "B-48": '客户', "B-49": '业务提醒', "B-50": '状态', "B-51": '提示', 'B-52': "时间", 'B-53': "回复", 'B-54': "申请业务",
           "B-55": "最大可分期金额", 'B-56': "每期本金", 'B-57': "每期手续费", 'B-58': "取款金额", 'B-59': '交易途径', 'B-60': '办理业务',
           'B-61': '缴费时间', 'B-62': '扣费项目', 'B-63': '状态', 'B-64': '转款客户', 'B-65': '转款时间', 'B-66': '收款账户尾号',
           'B-67': '交易类型', 'B-68': '交易金额', 'B-69': '目标账户', 'B-70': '客户', 'B-71': '收款账户尾号', 'B-72': '绑定手机号',
           'B-73': '短信编号', 'B-74': '密码序号', 'B-75': '剩余还款截至时间', 'B-76': '账单时间', 'B-77': '剩余应还款额', 'B-78': '最后还款日',
           'B-79': '剩余最低还款额', 'B-81': '申请业务', 'B-82': '状态', 'B-83': '验证码', 'B-84': '验证码用途', 'B-85': '验证码用途',
           'B-100': '话费余额',
           'B-101': '话费余额不足',
           'B-102': '话费欠费',
           'B-103': '消费金额', 'B-104': '缴费金额', 'B-105': '支付金额', 'B-106': '办理业务', 'B-107': '退款金额', 'B-108': '券号',
           'B-109': '签收快递单号', 'B-110': '派件快递单号', 'B-111': '使用话费',
           'B-200': '剩余流量',
           'B-201': 'WLAN剩余',
           'B-202': '剩余流量',
           'B-203': '剩余语音',
           'B-204': '剩余短信',
           'B-205': '通话时长已使用',
           'B-206': '套餐业务',
           'B-207': '套餐业务语音时长',
           'B-208': '剩余语音时长',
           'B-299': '套餐内流量',
           'B-298': '套餐内剩余流量',

           'B-209': '已开通套餐',
           'B-210': '票面信息',
           'B-212': '放映时间',
           'B-211': '影片',
           'B-213': '取票码',
           'B-214': '申购',

           'B-401': '本月总流量', 'B-402': '已用数据流量', 'B-403': "套餐内使用流量",
           'B-404': "套餐内使用流量", 'B-467': '本月套餐流量', 'B-601': '增加积分', 'B-602': '总积分', 'B-677': '还款金额', 'B-678': '应还款'
    , 'B-999': "编号"}

target_list = []
middle_list = []
explain_list = []
template_list = []

for x in my_dict.items():
    explain_list.append(x[1])
    target_list.append(x[0])
    middle_list.append('I' + x[0][1:])

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
template = ""

count = 0

temp_sign = 0

o = open("output/result_out", "w")
while 1:
    lines = f.readlines(100000)
    if not lines:
        break
    for line in lines:
        temp = line.split(" ")
        if line == "\n":
            for i, x in enumerate(target_list):
                sign[i] = 0
                if value[i] != '':
                    value_list[i].append(value[i])
                value[i] = ""
            o.write(sentence)
            o.write("\n")
            o.write(template)
            o.write("\n")
            o.write("(")
            count += 1
            for j, l in enumerate(explain_list):
                if len(value_list[j]) == 0:
                    continue
                o.write(l)
                o.write(":")
                for p in value_list[j]:
                    o.write(p)
                    o.write("  ")
                o.write("  ")

                value[j] = ""
                value_list[j] = []
                sign[j] = 0

            sentence = ""
            template = ""
            o.write(")")
        else:
            for i, x in enumerate(target_list):
                if temp[1].strip() == x:
                    sign[i] = 1
                    temp_sign = 1
                if sign[i] == 1 and temp[1] != (middle_list[i] + "\n") and temp[1] != (target_list[i] + "\n"):
                    sign[i] = 0
                    temp_sign = 0
                    if value[i] != '':
                        value_list[i].append(value[i])
                        template += "txt_" + my_dict[target_list[i]]
                    value[i] = ""
                if sign[i] == 1:
                    value[i] += temp[0].strip()
            if temp_sign == 0:
                template += temp[0].strip()

        if len(temp) == 2:
            sentence += temp[0]
        else:
            o.write("\n\n")

o.close()

print count
