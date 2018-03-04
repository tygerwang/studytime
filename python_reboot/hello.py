#!/usr/bin/python 
#encoding: utf-8
#-*- conding:utf-8 -*-

# recive a name
#name = raw_input('Please input your name:')
name = raw_input('请输入你的名字:')
print 'Hello ' + ',' + name


# study input
inputname = input('please input your inputname:')
print 'Hello ' + ',' + inputname

print name + '是' + inputname


###study funcation raw_input
print '##' * 20

num1 = raw_input('please input a number: ')
num2 = raw_input('please input a number: ')

sum = float(num1) + float(num2)
avg = sum/2
print 'num1 + num2 = %s' % sum
print '(num1+num2)/2 = %s' % avg
