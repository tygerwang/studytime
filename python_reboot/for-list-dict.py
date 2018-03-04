#encoding: utf-8

# 小练习5
# 遍历一个序列 ['C','js','python','js','css','js','html','node','css']
# 统计这个序列中，js出现的次数
'''
cnt = 0

list = ['C','js','python','js','css','js','html','node','css']
for i in list:
    if i == 'js':
        cnt += 1
print '\'js\' 出现次数:%s' % cnt
'''

# 小练习6
# 一个序列 [1,2,3,2,12,3,1,21,2,2,3,4111,2,3333,444,111,4,5,777,65555,45,33,45]
# 求这个list的最大值
'''
num_list = [1,2,3,2,12,3,1,21,2,2,3,4111,2,3333,444,111,4,5,777,65555,45,33,45]
maxnum = num_list[0]

for i in num_list:
    if i > maxnum:
        maxnum = i
print '最大值为: %s' % maxnum
'''

# 小练习7
# 用户输入一个数字，判断是不是闰年
# · 如果是100的倍数，要被400整除
# · 被4整除
# · 比如 1900不是闰年，2000,2004 就是闰年
# · 如果输入不是闰年，提示信息，并且继续输入

'''
while True:
    year = raw_input('请输入一个年份判断是否为闰年: ')
    if year == 'quit':
        break
    chu1 = int(year) % 100
    chu2 = int(year) % 400
    chu3 = int(year) % 4
    if chu1 == 0 and chu2 == 0:
        print '%s 是闰年' % year
    elif chu1 != 0 and chu3 ==0:
        print '%s 是闰年' % year
    else:
        print '%s 不是闰年，请继续输入...' % year
'''


# 小练习8
# ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
# 求出这个 list中，每个字符出现的次数

dict_cnt = {}
cnt = 0
listcnt = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']


for listterm in listcnt:
    if listterm in dict_cnt:
        dict_cnt[listterm] += 1
    else:
        dict_cnt[listterm] = 1

print dict_cnt


# 作业1
# 一个序列 [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
# 求这个 list 的最大的两个值






# 作业2
# 打印99乘法表







