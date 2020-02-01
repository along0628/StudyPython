# 记录生肖，根据年份判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# 切片操作
print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])

year = 2018
print(chinese_zodiac[year%12])
# 判断是否存在操作
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)

# 连接操作
m = 'abcd救护车'
n = 'efgh看见我'
M = m + n
print(M)

# 重复操作
q = '123啊'
w = 5
print(q * w)
