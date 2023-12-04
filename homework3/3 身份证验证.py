import re
mtp = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
res = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
day_Num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
flag = True
id = input("请输入需要验证的身份证号:")
if len(id) != 18:
    #print(len(id))
    flag = False
else:
    check = 0
    for i in range(0,17):
        check += mtp[i] * int(id[i])
    if str(res[check % 11]) != id[17]:
        #print(str(res[check % 11]) , id[17])
        flag = False
    regex = re.compile(r'(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})(\d|\w)')
    info = regex.search(id)
    year = int(info.group(2))
    month = int(info.group(3))
    day = int(info.group(4))
    #print(year,month,day)
    if month > 12 or month == 0:
        flag = False
    elif day == 0 or day > day_Num[month - 1] + (month == 2 and year % 4 == 0) :
        flag = False
    #print(info.groups())
if flag :
    print("合法")
else:
    print("不合法")
