"""
  python哲学：优雅 清晰 简单
  python是一种解释型的、面向对象的语言
  python对语言风格与语法有着比较严格的要求。写程序时应注意代码的整洁、完整与优美
"""

'''
python的输入与输出
注意：编程语言中，引号、括号均用英文输入法输入，否则不会被识别
      python大小写敏感：word，Word，WORD是不同的
'''

'''
注释：在写在代码中，用于对程序的标记与说明，但不会被运行。对后期修改、维护以及团队合作有很大帮助
      好的程序员会在程序中添加适当、清晰的注释
      python的注释方法：
      单行注释：#
      本行#后的代码会被省略
      多行注释：
      '''  '''
      或者
      """
      """
      里面的内容均会被省略
'''

'''
 python中的输入与输出
输出函数：print()   输入函数：input()  函数的特点：function_name(parameters)
 参数可以没有，也可以有多个，与函数有关

 函数与对象的区别
'''
# 输出函数 print()

# print('helloworld')
'''
在编程中，存在不同的数据类型
基本类型：整形short int long char    浮点型 float double
引用类型：
'''

'''
ascii字符表（见supplement）
'''
'''
在python中引号的使用
单引号或者双引号均可  单引号内双引号，双引号内单引号（在其他语言中不常用，建议用转义序列）
'''

# 转义序列（escape sequence）
# print('What do u say?')
# print('What\n do\n u\n say?')

# print('what's that')

# print('what\'s that')
# print("what's that")
# print("""what's that""")

'''
转义序列
\a 响铃(BEL)
\b 退格(BS) ，将当前位置移到前一列
\n 换行(LF) ，将当前位置移到下一行开头
\r 回车(CR) ，将当前位置移到本行开头
\t 水平制表(HT) （跳到下一个TAB位置）
\v 垂直制表(VT)
\\ 代表一个反斜线字符''\'
\' 代表一个单引号（撇号）字符
\" 代表一个双引号字符
'''

# python其他输出技巧

# print('helloworld\n'*10)

# shibo=100  txt='aaaaa'
# print('helloworld'+shibo+'you'+txt)

# lishi=666
# print('lishi:',lishi)

# 格式化输出
'''
%d  整数
%f  浮点数
%e  科学记数法
%c  ascii字符
%s  string
%r  任意类型
当可以确定类型时，最好确定类型。这样可以及时发现编程中的错误
'''
# cats=4
# cat_name='Kathy'
# print('There are %d cats.'%cats)
# print('There are %d cats. And one is lost. Her name is:%s'%(cats,cat_name))

# python的输入  input函数

# name=input()
# print(name)

# 强制类型转换
# 将一个类型的数据强行转化为另一个类型

# income='1000'

# print(income+1)

# income=int(income)
# print(income+2000)

# 整数与小数的转换

# pay=50
# pay=float(pay)
# print(pay)


# cats=int(input())
# print('There are %d cats.'%(cats+1))

# 提示用户输入内容
# name=input('Enter ur name: ')
# print('ur name is : ',name)

# python的数值计算

# + - * / %  **(指数运算)  //（地板除，除后去掉小数点后的值）  +=  -= *= /=

'''
a=2
b=3
c=2.0
d=3.0
print(d%c)
print(a**b)
print(c**d)
print(b//a)
print(c//d)
'''

# from xxx import xxx  python的模块化
# import math
# print(math.sin(math.radians(45)))
# print(math.log10(100))
# print(math.exp(3))
# print(sqrt(9))

# from math import exp
# print(exp(3))

# from math import *
# print(exp(3))
# print(log10(100))
'''
python中会有多种第三方模块，甚至即使内部的模块，也可能出现重名的函数。因此建议使用第一种，肯定不会错
在确定使用的模块中没有重名函数时，可以使用第二种或者第三种。但第三种不是很推荐
'''

# python的变量 variable
# 使用前初始化（initialize）
# 随时使用，随时创建
# 命名规则：首字母不是数字或特殊字符，首字母一般不大写，清晰地表达出变量的用途，单词间一般用_连接。
# 常量全部大写(python中没有定义常量const，可以自行定义。此处不深入。C语言中再说)
# 注意避免保留字符，如and or not from while for import... （编程中遇到过的自带的单词）


# python的逻辑运算
# and  or  not
# == >= <= !=
# ==与= 的区别：==是比较，相同或相等返回True，不同或不等返回False  =是赋值符，将右边的数符给左边
# bool型数  homework—finished = False

# 重要：运算的顺序：先算术运算符，再逻辑运算符，最后是赋值符  多重函数，先里后外  可以用小括号来调整运算顺序
# 尽量避免复杂的运算顺序。这样能保证代码的可读性，并且避免错误

# print(1+1==2 and 2+2==3)
# print( 2+1==3 or 3-1==2)

# 列表、字典和元组

# 列表
# 列表是有一定顺序的对象的集合（数字、字符串等）
# cats_names = ['Case', 'John', 'Peter', 'Hans', 'Linda', 'Mary']
# cats_owner = 'They all gonna die!'  # He must be a devil or mad!

# 得到列表的一个值或几个值
# print(cats_names[2])
# print(cats_names[-1])
# print(cats_names[1:5:2])
# 第一条语句显示的是什么？  生活中，我们用的是序数，是从1开始的 编程中使用基数，从0开始
# 第二条语句显示的是什么？  倒数是从-1开始，-1 -2 -3
# 第三条语句显示的是什么？显示了几个名字？  列表中xx[起点：终点：步长] 正数不算最后一个
# 问题：想要倒数怎么办？

# 添加一个数据
# cats_names.append('Lucy')
# print(cats_names)

# 插入一个数据
# cats_names[2:3] = ['Miao']
# print(cats_names)

# 去掉一个数据
# del cats_names[2:4]
# print(cats_names)

# 将字符串分割成列表
# cats_owner_saying = cats_owner.split(' ')
# print(cats_owner_saying)
# case = list(cats_names[0])
# print(case)

# 将元素相连
# cats_owner_saying[1:2] = ['not']
# print(' '.join(cats_owner_saying))

# 更多函数看附加网页

# 字典！口耐的字典！
# 字典就是索引。这也是我觉得python异常强大的原因！Life is short! I use python!
# 列表是用中括号[]，而字典是用大括号{}
elvis = {'name': 'elvis', 'height': 170, 'weight': 70, 'hair_color': 'black', 'school': 'WHU'}

# 利用索引显示内容
# print(elvis['name'])
# print(elvis['school'])
# print(elvis[2])
# 注意大中小括号的使用，注意引号的使用

# 修改字典里的内容
# elvis['height'] = 171
# print(elvis['height'])

# 删除字典里的内容
# del elvis['name']
# print(elvis)

# 元组
# （似乎不太重要，这里先不介绍了。需要的时候再补充）

# python的程序结构
# if分支结构   for循环结构  while结构

# if
'''
day=int(input('Today is the ?th day of a week\n> '))
if day>=1 and day<=5:
    print('Sorry! Today is a work day. Go back to work!')
    if day==3:
        print('But u can enjoy some snacks first.')
    else:
        pass
elif day==6:
    print('It\'s Saturday. Have fun~')
elif day==7:
    print('U are supposed to go to the church!')
else:
    print('Man! Are u on Mars?')
'''

# 不要丢掉冒号
# 有没有注意到elif与else的区别？
# 注意python里的缩进:请指出这个程序的层次
# 有if，下面一定要有else对应。可用pass占位

# for循环

# for numbers in range(0,4):
#     print(numbers)
# for numbers in range(1,7,2):
#     print(numbers)
'''
1.注意range（0，4）的范围
2.range（1，7，2）是什么意思？
3.为什么同时出现了两个numbers，不矛盾吗？   变量的生命周期：global（全局变量） 和局部变量
'''

'''
names = ['kathy', 'elvis', 'linda', 'John']
for name in names:
    print('1', name)

for name in names[2]:
    print('2', name)
# 思考，为什么names[2]却打出的是l,i,n,d,a而不是linda
for name in names[:2]:
    print('3', name)
for name in names[-1:-3:-1]:
    print('4', name)
'''

# while
# while与for功能有些类似。但也有独特之处
'''
date = 1
while date <= 5:
    print('Today is No.%d day of a week. U have to work.'%date)
    date+=1
print('Well.U have worked 5 days. Have a rest.')
'''

# 与break连用
'''
speed = 80
while True:
    print('PC:U are driving at a speed of %d miles/h.'%speed)
    print('ELVIS:I want to be faster.')
    speed += 10
    print('PC:Accelerating to %d miles/h'%speed)
    if speed >= 100:
        break
print('U are way too fast and knocked on a pig and died.')
'''

# 定义新函数与返回数值(解包省略，好像没什么用，不想讲了)
# 为了节约时间，python已经自带了一些函数供我们使用。
# 同时，我们可以将我们经常用到的代码写成函数，或者做成模块，重复使用
# python中函数的形式：def function_name(parameters):  请注意形式
# 同样的，函数可以没有参数传入。但圆括号不可以省略

# 一个关于爱的程序：
'''
def love(loverone, lovertwo):
    print(loverone,'loves',lovertwo)

def inputs():
    lovera = input('Enter the name of the first one:')
    loverb = input('Enter the name of the second one:')
    return lovera, loverb

print('Here is a game:')
name1, name2 = inputs()
love(name1, name2)
'''

# 引入自己编写或者他人编写的模块,减少工作量
# from Lishi import buzuosijiubuhuisi
# buzuosijiubuhuisi('anbeijinsan')

# 编写一个小游戏（exit（））

# from sys import exit
# exit(0)是一个正常退出的信号
# exit（1）是非正常退出信号
# 可以加入更多的参数代表更多的异常类型

# 处理文本
# 打开与读取
# txt1 = open('pythonstudy')
# data = txt1.read()
# print(data)

# 创建与写入
# txt2 = open('pythonpractise', 'w')
# txt2.write('Learning python need practice!')
# txt2.close()


# 类与实例（面向对象）
# 面向对象的语言，就是有相同特点的一类事物。他们有相同的属性和可以完成的事情，
# 比如习近平和奥巴马都是国家首领，都有身高、体重等基本属性，同时有管理国家等功能
# 那么我们就将他们归为一类。我们只需要写国家首领这个类，然后告诉系统，习与奥都是首领
# 我们就可以实现代码的重复利用。而习与奥二人就叫做实例

'''
class Birds(object):                         #object不可以省略
    def __init__(self, legnumbers, wings):   #self的使用是约定俗成。
        self.legnumbers = legnumbers
        self.wings = wings

    def flying(self):
        print('It can fly by %d wings'%self.wings)

    def running(self):
        print('It can run by %d legs'%self.legnumbers)

eagle = Birds(2,2)                           #创建一个eagle实例
eagle.flying()
eagle.running()

dapeng = Birds(2,0)                          #创建一个dapeng实例
dapeng.flying()
dapeng.running()
'''
# getattr(object,string)函数

# 程序猿之装逼手册
# class里的函数叫method
# 尽量让程序简单，不要滥用class
# 让class名称保持驼峰式大小写：如NoZuoNoDie
# 函数和方法用下划线隔词
# 加好的注释
# 发展出自己的代码风格，但要注意清晰美观

# python中的继承
# class Person(object):
# class Employee(Person):

#python的多继承与super:还在研究，先不讲了。自己先倒腾清楚
