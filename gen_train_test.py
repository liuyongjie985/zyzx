# coding:utf-8
import os
import re
import random

inpath = 'filtered_taocan_sms_sample.txt'


def split_train_test(path):
    i = 0
    fout1 = open('_train.txt', 'w')
    fout2 = open('_test.txt', 'w')
    fout3 = open('_test2.txt', 'w')

    r = random.randint(0, 10)
    with open(path) as f:
        for line in f.readlines():
            if i % 10 == r:
                fout2.write(line)
                fout3.write(line)
            else:
                fout1.write(line)
                r = random.randint(0, 10)
            i += 1
    fout1.close()
    fout2.close()
    fout3.close()


def dealwithline(line):
    def _line1(matched):
        re_str = ''
        time = matched.group("time")
        word_list = [c for c in time.decode('utf-8')]
        re_str = ''.join(word_list[0:2])
        for i, c in enumerate(word_list[2:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '1' + '\n'
            else:
                re_str += c + ' I-' + '1' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str.encode("utf-8")

    def _line2(matched):
        re_str = ''
        time = matched.group("stream1")
        word_list = [c for c in time.decode('utf-8')]
        re_str = ''.join(word_list[:7])
        for i, c in enumerate(word_list[7:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '2' + '\n'
            else:
                re_str += c + ' I-' + '2' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str.encode("utf-8")

    def _line3(matched):
        re_str = ''
        time = matched.group("stream2")
        word_list = [c for c in time.decode('utf-8')]
        re_str = ''.join(word_list[0:6])
        for i, c in enumerate(word_list[6:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '3' + '\n'
            else:
                re_str += c + ' I-' + '3' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str.encode("utf-8")

    def _line4(matched):
        re_str = ''
        time = matched.group("stream3")
        word_list = [c for c in time.decode('utf-8')]
        re_str = ''.join(word_list[0:6])
        for i, c in enumerate(word_list[6:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '4' + '\n'
            else:
                re_str += c + ' I-' + '4' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str.encode("utf-8")

    def _line5(matched):
        re_str = ''
        time = matched.group("stream4")
        word_list = [c for c in time.decode('utf-8')]
        re_str = ''.join(word_list[0:6])
        for i, c in enumerate(word_list[6:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '5' + '\n'
            else:
                re_str += c + ' I-' + '5' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str.encode("utf-8")

    def _line6(matched):
        re_str = ''
        time = matched.group("stream5")
        word_list = [c for c in time.decode('utf-8')]
        re_str = ''.join(word_list[0:9])
        for i, c in enumerate(word_list[9:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '5' + '\n'
            else:
                re_str += c + ' I-' + '5' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str.encode("utf-8")

    def _line7(matched):
        re_str = ''
        time = matched.group("stream6")
        word_list = [c for c in time.decode('utf-8')]
        re_str = ''.join(word_list[0:7])
        for i, c in enumerate(word_list[7:]):
            if i == 0:
                re_str += '\n' + c + ' B-' + '7' + '\n'
            else:
                re_str += c + ' I-' + '7' + '\n'
        # re_str += ''.join(word_list[-1])
        return re_str.encode("utf-8")

    # 验证码：验证码前后5个单位存在数字的话，把数字提取出来
    def _line8(matched):
        return

    # 提取验证码和动态密码
    start = -1
    end = -1

    line = line.decode("utf-8")
    idx_list = [i.start() for i in re.finditer(u'验证码', line)]
    idx_list += [i.start() for i in re.finditer(u'动态密码', line)]
    for idx in idx_list:
        # 先看后方5个单位内有没有验证码
        end = idx + 3 + 5 + 1
        if end > len(line):
            end = len(line)
        temp = line[idx:end]
        firstrNum = re.compile("\d")
        n_idx = -1

        try:
            n_idx = firstrNum.search(temp).start()
        except:
            pass
        # 有
        if n_idx >= 0:
            start = n_idx + idx
            while n_idx + idx < len(line):
                try:
                    n = int(line[n_idx + idx])
                except:
                    end = n_idx + idx
                    break;
                n_idx += 1
            if start != -1 and end != -1:
                deal = line[start:end]
                re_str = ""
                for l, x in enumerate(deal):
                    if l == 0:
                        re_str += '\n' + x + ' B-' + '8' + '\n'
                    else:
                        re_str += x + ' I-' + '8' + '\n'
                line = line[:start] + re_str + line[end:]
                # 验证码不可能有两个
                break;
        # 前方与后方只需要一个有即可 现在是前方
        else:
            # 看前方8个单位有没有（，如果有看前面2个单位是不是数字
            start = idx
            end = idx
            while start >= 0 and start >= idx - 8:
                if line[start] == u'(' or line[start] == u'（':
                    end = start
                    break;
                start -= 1
            start -= 3
            if end == idx:
                continue
            if start < 0:
                start = 0
            temp = line[start:end]
            firstrNum = re.compile("\d")
            n_idx = -1
            try:
                n_idx = firstrNum.search(temp).start()
            except:
                pass
            # 有
            if n_idx >= 0:
                # 确定end
                end = - 1
                start = n_idx + start
                while n_idx + start < len(line):
                    try:
                        n = int(line[n_idx + start])
                    except:
                        end = n_idx + start
                        break;
                    n_idx += 1
                start = -1
                # 确定start
                start = end - 1
                while start >= 0:
                    try:
                        n = int(line[start])
                    except:
                        start = start + 1
                        break;
                    start -= 1
                if start != end - 1 and end != -1:
                    deal = line[start:end]
                    re_str = ""
                    for l, x in enumerate(deal):
                        if l == 0:
                            re_str += '\n' + x + ' B-' + '8' + '\n'
                        else:
                            re_str += x + ' I-' + '8' + '\n'
                    line = line[:start] + re_str + line[end:]
                    # 验证码不可能有两个
                    break;

    line = line.encode("utf-8")

    line = re.sub(r"(?P<time>截至.*?分)", _line1, line.strip())
    line = re.sub(r"(?P<stream1>国内通用流量共([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line2, line.strip())
    line = re.sub(r"(?P<stream2>省内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line3, line.strip())
    line = re.sub(r"(?P<stream3>套餐外流量为([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line4, line.strip())
    line = re.sub(r"(?P<stream4>国内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line5, line.strip())
    line = re.sub(r"(?P<stream5>已使用移动数据流量([\d\.]+[MG]{0,1}B{0,1}){1,3)", _line6, line.strip())
    replacedStr = re.sub(r"(?P<stream6>套餐内流量剩余([\d\.]+[MG]{0,1}B{0,1}){1,3})", _line7, line.strip())

    return replacedStr


def gen(inpath, name, flag):
    # flag true的话保留大标签
    fout = open('output1.txt', 'w')
    with open(inpath) as f:
        for line in f.readlines():
            re_line = dealwithline(line)
            fout.write(re_line)
            fout.write('\n')
    fout.close()

    fout = open(name, 'w')
    before = ""
    with open('output1.txt') as f:
        for line in f.readlines():
            my_list = line.strip().split()
            if len(my_list) == 2 and (my_list[1].startswith('B') or my_list[1].startswith('I')):
                if not flag:
                    before = line[:-2] + '\n'
                    fout.write(line[:-2] + '\n')

                else:
                    before = line.strip() + '\n'
                    fout.write(line.strip() + '\n')

            else:
                if len(before) == 6 and line[0] != '，' and line[0] != '。' and line[0] != ',':
                    fout.write("\n")

                for w in line.strip().decode('utf-8'):
                    if w in [u'。', u'？', u'?']:
                        fout.write(w.encode('utf-8') + ' O\n\n')
                        before = w.encode('utf-8') + ' O\n\n'
                    else:
                        fout.write(w.encode('utf-8') + ' O\n')
                        before = w.encode('utf-8') + ' O\n'
    os.remove('output1.txt')
    fout.close()


if __name__ == '__main__':
    split_train_test(inpath)
    gen('_train.txt', 'train.txt', True)
    gen('_test.txt', 'test.txt', True)
    # gen('_test2.txt', 'test2.txt', True)

    os.remove('_train.txt')
    os.remove('_test.txt')
    os.remove('_test2.txt')

    f = open("train.txt")

    statistic = {}

    while 1:
        lines = f.readlines(100000)
        if not lines:
            break
        for line in lines:
            line = line.decode('utf-8')
            if statistic.has_key(len(line)):
                statistic[len(line)] += 1
            else:
                statistic[len(line)] = 1
    f.close()
    for x in statistic.items():
        print str(x[0]) + ':' + str(x[1])
