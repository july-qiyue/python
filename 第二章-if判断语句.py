# python当中的关键字--keyword
# 很多语言这当中都会有关键字，又叫做保留字段
# 因为我们不同的语言当中都会有一些特殊的英文单词有特殊的作用
# 这些单词不能在我们的变成的时候随意的拿来进行赋值更改他们本身的意思
# 比如我们已经使用的print，input
# 不能拿来做变量名，函数名，类名等等标识符
#
# 有哪些关键字
# 可以用过导入一个包叫座keyword来将python当中的关键字打印出来
# import keyword
# 导入keyword库
# print（keyword.kwlist）#打印所有python的关键字
#
# python当中标识符的命名规则
# 可以使用‘a-z’或‘A-Z’字母和‘0-9’数字以及‘_’下划线来组成标识符名称
# 但是要注意，不能以数字开头
# 如果使用‘_’单下划线或‘__’双下划线作为变量名，那么说明这个变量是一个类当中又特殊用处的变量
#
# 二、python当中的运算符
# 1.算术运算符
# + 加法运算符  用来将加号左右两边的变量或数据进行加法运算
# - 减法运算符  用来将减号左右两边的变量或数据进行减法运算
# * 乘法运算符  用来将乘号左右两边的变量或数据进行乘法运算
# / 除法运算符  用来将除号左右两边的变量或数据进行除法运算
# % 取模运算符  用来将取模符号左右两边的变量或数据进行取模运算  （取余数）
# ** 次幂运算符  用来将次幂符号左右两边的变量或数据进行次幂运算  （次方）
# //向下整除运算符  用来将整除号左右两边的变量或数据进行向下整除运算  （取整数，小数点后不算，例如2.1 取值为2 ，2.9 取值为2）
#
# 例如：
# a=2;b=4;c=0
# c=a+b
# print('a+b',c)
#
# 2.关系运算符
# 判断左右两个数据的关系的运算符，又叫做比较运算符，用来判断两个数据是否相等，或谁大于谁，小于谁...
# == 等于，判断两个数字或者字符串是否相等，如果相等则会返回布尔值（true），如果不相等则会返回布尔值（false）
# != 不等于，判断两个数字或者字符串是否不相等
# > 大于，判断左边的数字是否大于右边的数字
# < 小于，判断左边的数字是否小于右边的数字
# >= 大于等于，判断左边的数字是否大于等于右边的数字
# <= 小于等于，判断左边的数字是否小于等于右边的数字
#
# 例如：
# a=2;b=4
# a == b 这样写判断了吗？ 判断了，但是没有进行结果输出
# print（a==b） #直接打印a和b的判断结果
# c=a!=b #将比较的结果赋值给一个变量
# print(c) #然后直接打印这个变量存储的结果
# z='python';x='python'
# print(z==x) #双等号可以判断两个字符串是否相等，同理，!=也可以判断两个字符串是否不相等
#
# 3.赋值运算符
# 用来给变量进行赋值操作的，但是在赋值的时候我们还可以进行运算
# = 单纯的赋值操作，会将右边的数据赋值给=左边的变量名中
# +=，-=，*=，/=，**=，//=，%=
#
# 这些运算符用起来都差不多，只是运算方式不同
# 他们会将等号左侧的变量的值于等号右边的数据进行算术运算，然后再将运算的结果赋值给左侧的变量
# 例如：
# a=3;b=5
# a+=b   #a=a+b
# print(a)
# a-=b #a=a-b
# print(a)
#
#
# 4.逻辑运算符
# 与and，或or，非not
#
##and 用来判断多个子判断在并列关系下的结果
# 举例：判断吃不吃饭
# 条件：1，饿（true）不饿（flase）  2，有（true）没有（flase）钱
# 饿 and 有钱 == 吃
# 饿 and 没钱 == 不吃
# 不饿 and 有钱 == 不吃
# 不饿 and 没钱 == 不吃
#
##or但凡有一个子条件被满足，最终结果就为真
# 举例：判断吃不吃饭
# 条件：1，饿（true）不饿（flase）  2，有（true）没有（flase）钱
# 饿 or 有钱 == 吃
# 饿 or 没钱 == 不吃
# 不饿 or 有钱 == 吃
# 不饿 or 没钱 == 不吃
# 只有当所有子判断结果都为假的时候，最终结果才是假，只要满足任何一个条件结果就为真
#
# not 取反
# a=10;b=20
# print(not(a>b)) 本来a>b是不成立的，但是我们用not将其结果取反，最后输出的则是true
#
# python当中最字符串的一系列判断
# 这里我们学习一些方法，用来对字符串内容进行判断
#
# 例如
# words = input('请输入一个字符串：')
# # 判断这个字符串当中是否是由数字组成的
# print(words.isdigit())
# # .isdigit()方法，用来判断这个字符串是否是全部数字组成的
# print(words.isalpha())
# # .isalpha()方法，用来判断这个字符串内容是否全部由正经的文字组成（除特殊符号，数字）
# print(words.isalnum())
# # .isalnum()方法，用来判断字符串是否由字母，数字组成，如果字符串里面带有标点符号，或者是空字符串，结果都会是false，
# # 所以我们有时候直接拿他来判断用户是否输入了内容
# print(words.islower()) #判断字符串是否是小写字母组成
# print(words.isupper()) #端盘字符串是否是大写字母组成
# print(words.lower())    #将输出的字符串转换为小写输出
# print(words.upper())    #将输出的字符串转换为大写输出
#
#
# python
# if uname == userinfo[0]:当中的条件判断语句
# if语句
# if 要判断的条件:
#     符合该条件做的事情
#
#例如：
# userinfo = ['liu','123.com']    #这里设定了一个userinfo列表
# uname = input('请输入用户名：')    #程序开始后让用户输入一个用户名赋值给uname
# if uname == userinfo[0]:        #判断uname变量的值是否与userinfo列表中第一个元素值相等
#     upwd = input('请输入密码：')  #如果上面条件达成，则提示输入密码，如果不符合，程序没有给出对应的处理方法，就会结束
#
# if语句是可以嵌套的，我们在没有符合判断条件的情况下的处理，会怎么办？
# 用到了另外一个关键字else
# userinfo = ['liu','123.com']    #这里设定了一个userinfo列表
# uname = input('请输入用户名：')    #程序开始后让用户输入一个用户名赋值给uname
# if uname == userinfo[0]:        #判断uname变量的值是否与userinfo列表中第一个元素值相等
#     upwd = input('请输入密码：')  #如果上面条件达成，则提示输入密码，如果不符合，程序没有给出对应的处理方法，就会结束
# else:   #else否则的意思，用来处理符合条件之外的情况
#     print('您输入的用户名有误！')
#
# 例如：创建一个用户注册and登录程序
# 这个程序在运行的时候，会询问用户，进行注册还是登录
# 如果用户输入的是注册，则让用户输入用户名，密码
# 然后将用户名和密码存入到一个列表或字典当中
#
# 如果用户输入的是登录，则提示用户输入用户名和密码
# 然后使用用户输入的内容和存储用户信息的列表或字典当中的指定内容进行比较
# 如果用户民个密码都与程序中存储的信息匹配，则告知用户登录成功
# 如果不匹配则告知用户登录失败
#
# 注意！让用户进行用户名个密码的输入的时候，首先我们还要判断用户输入的内容是否为空
# 用户名应该有用户名的命名规则，比如是否有数字和字母组成，比如密码不能是纯数字



# 设定全局变量，整个程序当中都可以起作用的变量名
useract = input('登录/注册：')
uname = ""
upwd = ""
upwdretype = ""

#如果用户输入的是登录
if useract == '登录':
    # 指定登录的用户名和密码
    login = {'用户名':'aaa','密码':'bbb'}
    # 定义用户交互的用户名，存储到uname变量中
    uname = input('请输入用户名：')
    # 判断用户输入的用户名是否为login中的'用户名'
    if uname == login['用户名']:
        # 如果是，提示用户输入密码
        upwd = input('请输入密码：')
        # 判断用户输入的密码是否为login中的'密码'
        if upwd == login['密码']:
            # 如果是，则登录成功，开始玩小游戏
            print('登录成功！')
            print('我们来玩个小游戏，石头剪刀布！')
            # 将交互内容存储到play变量中，自己定义石头为1,剪刀为2，布为3
            play = int(input('请出石头（1）,剪刀（2），布（3）'))
            # 导入模块，用来生成随机数，模仿电脑人
            import random
            # 随机生成1-3任意数，来充当石头剪刀布
            ran = random.randint(1, 3)
            # 显示给用户电脑的输出，这里输出的是一个数字
            print('电脑出的是：', ran)
            # 判断，如果你出石头 电脑出剪刀，或，你出剪刀电脑出布，或，你出布电脑出石头
            if ((play == 1 and ran == 2) or
                    (play == 2 and ran == 3) or
                    (play == 3 and ran == 1)):
                # 则代表你胜利
                print('恭喜你，你赢了')
            # 如果你和电脑人出的相同，则平局
            elif play == ran:
                print('平局')
            # 其他情况代表失败
            else:
                print('很遗憾，你输了')
        # 如果不是，提示密码错误
        else:
            print('密码错误！')
    # 如果用户输入的用户不是login中的'用户名'，则提示没有该用户
    else:
        print('没有该用户，您输入的用户名有误！')
#如果用户输入的是注册
elif useract == '注册':   #else if多分支判断的关键字
    #注册要做的事
    uname = input("请输入您的用户名：")
    if uname.isalnum() or uname.isalpha() or uname.isdigit():
        user = []
        user.append(uname)
        #用户符合规则，做什么
        upwd = input("请输入密码：")
        upwdretype = input("请再次输入密码：")
        if upwd == upwdretype:
            pwd = []
            pwd.append(upwd)
            print('注册成功！')
            print('用户名：',user[0],'密码：',pwd[0])
        else:
            print('两次输入的密码不同！')
    else:
    # 用户不符合规则，做什么
        print("您的用户名含有特殊字符！")
    #用户已经输入了用户名和密码，这时，我们该判定用户输入的内容是否符合规则
    #用户输入的内容不能是空值，并且用户名是数字或字母组成
else:
    print('您的输入有误，请输入登录/注册，请重新执行程序！！！')
    #如果不是登录也不是注册，怎么办


# 为了了我们的项目更有趣
# 这里学习一下随机数
# 想要在python当中使用随机数，首先要导入一个库random
# import random
# # 导入随机数库
# ran = random.randrange(54)    #设置随机数范围是0-53
# print(ran)
# ran = random.randrange(1,54)    #设置随机数范围是1-54
# print(ran)
# poker = ['黑桃1','黑桃2','黑桃3','黑桃4','黑桃5','黑桃6','黑桃7','黑桃8','黑桃9','黑桃10','黑桃J','黑桃Q','黑桃K'
#          '红桃1','红桃2','红桃3','红桃4','红桃5','红桃6','红桃7','红桃8','红桃9','红桃10','红桃J','红桃Q','红桃K'
#          '梅花1','梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8','梅花9','梅花10','梅花J','梅花Q','梅花K'
#          '方块1','方块2','方块3','方块4','方块5','方块6','方块7','方块8','方块9','方块10','方块J','方块Q','方块K']
# ran = random.choice(poker)  #从指定范围中进行随机选择
# print(ran)
# random.shuffle(poker) #shuffle()函数用来随机打乱列表顺序
# print(poker)            #这时我们再次打印poker泪飙，会得到一个顺序已经被打乱的列表内容

##作业：
# 完成注册登录程序，当登录后，可以进行游戏
# 游戏内容可以进行是由剪刀布游戏
# 该游戏
# 让玩家输入石头，剪刀或布
# 让电脑随机出（石头，剪刀，布）
# 如果玩家胜利，则告知玩家胜利
# 如果电脑胜利，则告知玩家失败
# play = int(input('请出石头（1）,剪刀（2），布（3）'))
# import random
# ran = random.randint(1,3)
# print('电脑出的是：',ran)
# if ((play == 1 and ran == 2) or
#         (play == 2 and ran == 3) or
#         (play == 3 and ran == 1)):
#     print('恭喜你，你赢了')
# elif play == ran:
#     print('平局')
# else:
#     print('很遗憾，你输了')

