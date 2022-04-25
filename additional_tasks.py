def goal_parser_interpretation(command):
    out = command.replace("()", 'o').replace("(al)", "al")
    return out


def final_value_after_operations(operations):
    prevX = 0
    for op in operations:
        if op[1] == '+':
            x = prevX + 1
            print(op + f": X is incremented by 1, X = {prevX} + 1 = {x}")
        elif op[1] == '-':
            x = prevX - 1
            print(op + f": X is decremented by 1, X = {prevX} - 1 = {x}")
        else:
            raise Exception("Unrecognised operation")
        prevX = x
    return prevX


def array_strings_are_equal(list1, list2):
    string1 = ''.join(list1)
    string2 = ''.join(list2)
    return string1 == string2


def most_words_found(list):
    most = 0
    max_words = 0

    for i in range(len(list)):
        curr_count = len(list[i].split(' '))
        if curr_count > max_words:
            max_words = curr_count
            most = i
    return most


def to_lower_case(string):
    return string.lower()
