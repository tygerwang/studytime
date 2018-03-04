#encoding: utf-8

##study for bool type
#a = True
#b = False
#
#a or b
#a and b

### 输入两个人的年龄，判断第一个人的年龄大于第二个人的年龄，print 前者大
#age1 = int(raw_input('输入二黑的年龄: '))
#age2 = int(raw_input('输入二狗的年龄: '))
#max_age = 0
#
#if age1 > age2:
#    print '二狗年龄 %s > 二黑年龄 %s' % (age1,age2)
#else:
#    if age1 == age2:
#        print '二狗年龄 %s = 二黑年龄 %s' % (age1,age2)
#    else:
#        print '二狗年龄 %s < 二黑年龄 %s' % (age1,age2) 
#
#if age1 > age2:
#    max_age = age1
#    print '二狗年龄 %s > 二黑年龄 %s' % (age1,age2)
#elif age1 == age2:
#    max_age = age1
#    print '二狗年龄 %s = 二黑年龄 %s' % (age1,age2)
#else:
#    max_age = age2
#    print '二狗年龄 %s < 二黑年龄 %s' % (age1,age2)
#
#print '最大年龄为 %s' % max_age


#输入两个年龄
# age1 存储最大的年龄
# age2 存储最小的年龄
#age1 = int(raw_input('输入二黑的年龄age1: '))
#age2 = int(raw_input('输入二狗的年龄age2: '))
#temp = int(0)
#
#if age1 > age2:
#    print 'age1 为 %s，age2 为 %s' % (age1,age2)
#elif age1 == age2:
#    print 'age1 为 %s，age2 为 %s' % (age1,age2)
#else:
#    temp = age1
#    age1 = age2
#    age2 = temp
#    print 'age1 为 %s，age2 为 %s' % (age1,age2)

'''
#请输入一个分数acore
#如果成绩在[0,60) 打印不及格
#[60,70)  一般
#[70,80)  良好
#[80,90)  优良
#[90,100] 优秀

i = 0

while i < 3:
    i += 1
    score = int(raw_input('请输入您的分数: '))
    if 100 < score or score < 0:
        print '您分数为: %s ，超出小学考试分数' % score
    elif score < 60:
        print '您分数为: %s ，不及格成绩需要努力呀' % score
    elif score < 70:
        print '您分数为: %s ，成绩一般' % score
    elif score < 80:
        print '您分数为: %s ，成绩良好' % score
    elif score < 90:
        print '您分数为: %s ，成绩优良' % score
    elif score <= 100:
        print '您分数为: %s ，成绩优秀' % score
'''

'''
#存10000元，利率是 3.3%
#我存几年，银行的账户能翻一翻

#money = 10000
#money = money * (1 + 0.033)

year = 0
money = 10000

while money < 20000:
    money = money * (1 + 0.033)
    year += 1

print year


name = ''
## 不等于空 ---> 跳出   --->为 A
## 等于空 -----> 继续   --->为 非A

#while name == '':
while not name:
    name = raw_input('please input name: ')

print 'hello ' + name
'''


##小练习
# · 让用户一直输入数字
# · 如果输入的是'pc'，终止程序
# · 打印所有数字之和

total = 0
num1 = 0
cnt = 0

while True:
    num1 = raw_input('pleast input a number: ')
    if num1 == 'pc':
        break
    total += int(num1)
    cnt += 1.0

if cnt == 0:
    print 'total:%s,avg:0' % total
else:
    print 'total:%s,avg:%s' % (total,total / cnt)
