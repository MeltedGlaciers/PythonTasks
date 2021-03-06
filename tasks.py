import os
import time


def task_1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    return [el for el in a if el < 5]


def task_2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    return [el for el in a if el in b]


def task_3():
    dic = {"e": 5, "b": 2, "d": 4, "c": 3, "a": 1}
    listASC = sorted(dic.items(), key=lambda dic: dic[1])
    listDESC = sorted(dic.items(), key=lambda dic: dic[1], reverse=True)
    return (dict(listDESC), dict(listASC))


def task_4():
    dic1 = {"e": 5, "b": 2, "d": 4, "c": 3, "a": 1}
    dic2 = {"f": 6, "g": 7, "k": 8, "n": 9, "o": 10}
    dic1.update(dic2)
    return dic1


def task_5():
    my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    list = sorted(my_dict.items(), key=lambda my_dict: my_dict[1])
    return list[-3:]


def task_6(num):
    return str(num)


def task_7(n):
    row = [0, 1, 0]
    print(row[1:-1])
    nextRow = []
    for i in range(n):
        nextRow.append(0)
        for j in range(len(row) - 1):
            nextRow.append(row[j] + row[j + 1])
        nextRow.append(0)
        row = nextRow
        nextRow = []
        print(row[1:-1])


def task_8(str):
    for i in range(round(len(str) / 2)):
        if str[i] != str[-i - 1]:
            return False
    return True


def task_9():
    dels = [60 * 60 * 24, 60 * 60, 60]
    timeList = []
    currT = round(time.time())
    for d in dels:
        timeList.append(currT // d)
        currT = currT % d
    timeList.append(currT)
    st = ""
    for el in timeList:
        st += str(el)
        st += ":"
    return st[:-1]


def task_10():
    line = input()
    nums = [int(el) for el in line.split(',')]
    numsTup = tuple(nums)
    return (nums, numsTup)


def task_11():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return (list[0], list[-1])


def task_12(string):
    list = string.split(".")
    if len(list) < 2 or list[-1] == '':
        raise Exception("Cannot define extension")
    return list[-1]


def task_13(num):
    razr = len(str(num))
    return num + \
           num * (10 ** razr) + num + \
           num * (10 ** (razr * 2)) + num * (10 ** razr) + num  # n+nn+nnn


def task_14(list):
    for el in list:
        if el == 237:
            break
        if el % 2 == 0:
            print(el)


def task_15(list1, list2):
    return list(set(list1) - set(list2))


def task_16():
    for file in os.listdir("./"):
        print(file)


def task_17(num):
    str_num = str(num)
    res = [int(ch) for ch in str_num]
    return sum(res)


def task_18(string, req_char):
    count = 0
    for ch in string:
        if ch == req_char:
            count += 1
    return count


def task_19(a, b):
    a, b = b, a
    return a, b


def task_20(nums):
    return list(filter(lambda el: el%15==0,nums))


def task_21(nums):
    return len(nums) == len(set(nums))


def task_22(text):
    text = text.replace('.',' ').replace(',',' ') # and other punctuation marks
    word_dict = {}
    longest = ''
    for word in text.split():
        if word=='':
            continue
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
        if len(word)>len(longest):
            longest=word
    res = sorted(word_dict.items(), key=lambda my_dict: my_dict[1])[-1][0]
    print(sorted(word_dict.items(), key=lambda my_dict: my_dict[1]))
    return res, longest