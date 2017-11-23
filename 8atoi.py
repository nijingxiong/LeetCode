def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    final = 0
    str = str.lstrip()
    if str == "": return 0
    flag = 1
    if str[0] == '+':
        flag = 1
        str = str[1:]
    elif str[0] == '-':
        flag = -1
        str = str[1:]
    if str == "": return 0
    for i in str:
        if i >= '0' and i <= '9':
            final = final * 10 + int(i)
        else:
            break
    if final > 2147483647:
        final = 2147483647
        if flag == -1:
            final = final + 1
    return flag * final
    return flag * int(str)
print(int("010"))
print(myAtoi(" 010"))