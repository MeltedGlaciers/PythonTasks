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


def task_6():
    pass


def task_7(n):
    row = [0, 1, 0]
    print(row[1:-1])
    nextRow = []
    for i in range(n):
        nextRow.append(0)
        for j in range(len(row)-1):
            nextRow.append(row[j]+row[j+1])
        nextRow.append(0)
        row = nextRow
        nextRow = []
        print(row[1:-1])

def task_8(str):
    for i in range(round(len(str)/2)):
        if str[i]!=str[-i-1]:
            return False
    return True