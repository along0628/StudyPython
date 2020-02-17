# 记录生肖，根据年份判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# year = int(input('请用户输入出生年份'))
#
# if (chinese_zodiac[year%12] == '狗'):
#     print('狗年大吉')
# else:
#     print('你完了')

# for cz in chinese_zodiac:
#     print(cz)
#
# for i in range(1,13):
#     print(i)
# for year in range(1998,2021):
#     print('%s 的生肖是 %s' %(year, chinese_zodiac[year % 12]))

# num  = 5
# while True:
#     print('a')
#     num = num+1
#     if num > 10:
#         break

import time
num = 5
while True:
    num = num+1

    if(num ==10):
        continue

    print(num)
    time.sleep(1)
