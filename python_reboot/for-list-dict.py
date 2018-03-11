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
'''
dict_cnt = {}
cnt = 0
listcnt = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']


for listterm in listcnt:
    if listterm in dict_cnt:
        dict_cnt[listterm] += 1
    else:
        dict_cnt[listterm] = 1

print dict_cnt
'''

# 作业1
# 一个序列 [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
# 求这个 list 的最大的两个值
'''
list_num = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
        
left_num = None
right_num = None
for num in list_num:
    if right_num is None:
        right_num = num
    elif right_num < num:
        left_num = right_num
        right_num = num
    elif left_num is None:
        left_num = num
    elif left_num < num:
        left_num = num

print right_num,left_num
'''

# 作业2
# 打印99乘法表
'''
print '\n9x9 Table\n'
for i in range(1,10):
    for j in range(1,i+1):
        #print j,'x',i,'=',j*i,'\t'
        print '%d x %d = %2d ' % (j,i,j*i),
    print '\n'
print '\nDone!'
'''

# 判断某一字符串是否在list中
'''
list_name = ['wang', 'hui', 'tyger']

isname = raw_input('please input name: ')
exists = False

for _name in list_name:
    if _name == isname:
        exists = True
        break

if exists:
    print 'your name %s is in list' % isname
else:
    print 'your name %s is not in list' % isname
'''

# 判断某一字符串出现的次数
'''
list_name = ['wang', 'hui', 'tyger', 'wang']

isname = raw_input('please input name: ')
cnt = 0

for _name in list_name:
    if _name == isname:
        cnt += 1

print 'your name %s 出现了 %d 次' % (isname,cnt)
'''

# 练习7 待办事项，让用户持续输入，采用队列
'''
如果用户输入的是add,让用户再输入字符，加到代办事项列表，打印列表，让用户继续输入，
如果用户输入的是do, 从待办事项取出一个打印出来,如果没有事情要做，终止程序，让用户
继续输入
'''
'''
works_list = []


while True:
    _terms = raw_input('input a term add=>new work/do=>do first work/exit=>exit system: ')
    if _terms == 'add':
        _work_term = raw_input('please input a work term: ')
        works_list.append(_work_term)
        print works_list
    elif _terms == 'do':
        if len(works_list) != 0:
            print 'will do a work: %s' % works_list[0]
            works_list.pop(0)
        else:
            print 'all works have been done! good!'
    elif _terms == 'exit':
        break
'''

# 通过代码实现reverse反转
'''
list_num=range(10)
new_list = []
cnt = 0
for i in list_num:                                  
    new_list.append(list_num[len(list_num)-cnt])
    cnt += 1     
    if len(new_list) == len(list_num):             
        print new_list
# 法二
for i in range(0, len(num_list)/2):
    num_list[i],num_list[-1 - i] = nunm_list[-1 -i],num_list[i]
'''

# 冒泡排序，排列身高列表 
heigh = [176, 178, 165, 169, 179, 172]

for j in range(0, len(heigh) -1):
    print '======第%s次排序=====================' % j
    for i in range(0, len(heigh) - 1):
        if heigh[i] > heigh[i + 1]:
            print '交换%s[%s], %s[%s]' % (i, heigh[i], i + 1, heigh[i + 1])
            heigh[i],heigh[i + 1] = heigh[i + 1], heigh[i]
            print '结果:%s' % heigh 
























