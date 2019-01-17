File1 = 'weather_data_from_ssh.txt'  # 要进行处理的数据
File2 = 'data_for_test.txt'  # 用来测试的数据
File3 = 'weather_data_from_ssh2.txt'

with open(File3) as f_object:
    pre_data = f_object.readlines()
    data = []
    for i in range(len(pre_data)):
        tmp = pre_data[i].split()   # 将每行数据按照空格分隔
        # 进行数据类型转换，0为站点（字符串）、1为年份（字符串）、2为月份（字符串）、3为月均温（float)、4为月均温（float)
        tmp[3] = float(tmp[3])
        tmp[4] = float(tmp[4])
        data.append(tmp)

# 异常数据年份列表
with open('error_site_year_for2.txt') as f_object2:
    pre_data = f_object2.readlines()
    error_data = []
    for i in range(len(pre_data)):
        error_data.append(tuple(pre_data[i].split()))
    error_data = tuple(error_data)


# 进行数据的处理
output = {}
i = 0
while i < len(data):
    # 判断是否是异常站点的异常年份
    if (data[i][0], data[i][1]) in error_data:
        box = data[i][1]
        # output[data[i][0]] = {data[i][1]: [0, 0, 0, 0, 0]}
        while i < len(data) and box == data[i][1]:
            i += 1
    else:
        # 判断站点、年份是否被记录
        site = data[i][0]
        year = data[i][1]
        if site in output.keys():
            output[site][year] = [0, 0, 0, 0, 0]

            sum_rain = sum_temp = 0
            output[site][year][1] = data[i][4]

            # print(output[site][year])
            # print(data[i+6][4])
            output[site][year][2] = data[i + 6][4]
            output[site][year][3] = output[site][year][2] - output[site][year][1]
            for j in range(12):
                print(data[i])
                sum_rain = sum_rain + data[i][3]
                sum_temp = sum_temp + data[i][4]
                i += 1
            output[site][year][0] = sum_rain
            output[site][year][4] = sum_temp / 12

        else:
            output[site] = {}
            output[site][year] = [0, 0, 0, 0, 0]

            sum_rain = sum_temp = 0
            output[site][year][1] = data[i][4]

            output[site][year][2] = data[i+6][4]
            output[site][year][3] = output[site][year][2]-output[site][year][1]
            for j in range(12):
                sum_rain = sum_rain + data[i][3]
                sum_temp = sum_temp + data[i][4]
                i += 1
            output[site][year][0] = sum_rain
            output[site][year][4] = sum_temp / 12

# 进行数据的格式化输出
with open('output.txt', 'w') as f_object3:
    for key1 in output.keys():
        for key2 in output[key1].keys():
            f_object3.write("{} {} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}\n".format(key1, key2, output[key1][key2][0], output[key1][key2][1], output[key1][key2][2], output[key1][key2][3], output[key1][key2][4]))
