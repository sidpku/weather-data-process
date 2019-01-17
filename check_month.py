File1 = 'error1_data.txt'  # 要进行处理的数据

with open(File1,encoding='utf-8') as f_object:
    pre_data = f_object.readlines()
    data = []
    for i in range(len(pre_data)):
        tmp = pre_data[i].split()   # 将每行数据按照空格分隔
        # 进行数据类型转换，0为站点（字符串）、1为年份（字符串）、2为月份（字符串）、3为月均温（float)、4为月均温（float)
        tmp[3] = float(tmp[3])
        tmp[4] = float(tmp[4])
        data.append(tmp)

i = 0
j = 0
box = ''
error_list = set()
while i < len(data):
    if i == 0:
        if float(data[i][3]) > 10000 or abs(float(data[i][4])) > 100:
           error_list.add((data[i][0], data[i][1]))
        j = 1
        i += 1
        box = data[i][1]

    else:
        if float(data[i][3]) > 10000 or abs(float(data[i][4])) > 100:
            error_list.add((data[i][0], data[i][1]))     # 不完善，会出现1月份异常数据，导致在异常年份的表中输出2次
        if box == data[i][1]:
            i += 1
            j += 1
        elif j == 12:
            j = 0
            box = data[i][1]
        else:
            j = 0
            box = data[i][1]
            print("缺少月份 {} {}".format(data[i-1][0],data[i-1][1]))
            error_list.add((data[i-1][0], data[i-1][1]))
if j != 12:
    error_list.add((data[i-1][0],data[i-1][1]))

error_list = list(error_list)
with open('error_site_year_for2.txt', 'w') as f_object3:
    for i in range(len(error_list)):
        f_object3.write("{} {}\n".format(error_list[i][0], error_list[i][1]))