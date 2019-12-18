####################python中的方法和类的定义和使用##########################
# 所谓方法就是我们平常说的函数
# 在之前的学习中，我们以及使用很多python的内置函数
# 比如：print()，input()，isdigit() ...等等
# 方法(函数)我们自己也可以定义，如何定义呢？
# 格式如下：
# def 自定义方法名(定义用来接参数的变量名):
#         方法中要做的事
# 注意：方法定义后要有冒号，方法中记录的处理代码。要与方法名有缩进
#
#
# 实例：定义一个用来进行加法运算的函数

# def jiafa(x,y):         #定义了一个叫做加法的函数，这个函数在调用的时候需要向其中传递两个参数，x，y
#     print('您输入的两个数字之和为',x+y)
# 上面我们定义了函数jiafa，那么如何使用呢？
# 如果要调用他，其实我们已经会调用了，想想print()是怎么用的
# jiafa(1,3)  #调用jiafa()函数，并向其中传递两个数字类型参数，让他们对这两个参数进行加法运算
# jiafa('lyl','hhh') #调用jiafa()函数并向其中传递两个字符串类型的参数求这两个字符串组合的结果
# jiafa('lyl',123)  #调用jiafa()函数，并向其中传递一个字符串类型的参数和一个数字类型的参数，并尝试将其进行加法运算
# 或者字符衔接，他是不行的，为什么呢？
# python当中，字符串和字符串之间使用+来进行字符串的衔接
# 数字和数字之间使用，用+来进行加法运算
# 但是字符串和数字之间不能使用+，因为一个字符串类型的数据不能与数字类型的数据相加，勇士也不能金属字符的衔接，如果想要衔接字符串和数字，
# 应该使用","或者我们可以将数字类型的数据通过str()函数转换为字符串类型，这样沃恩就可以与另外的字符串进行加号衔接了
# 例：
# jiafa('lyl',str(123))

# 使用函数有什么好处呢？
# 能够提高代码的重复利用

# 在函数当中，不光是能够使用print()来打印某写运算的结果
# 如果我们需要在运算过后，将结果反馈出来，要让其他变量能够得到这个反馈出的内容，怎么办？
# 就需要用到一个关键字，叫做return()
# def jisuan(zzz,xxx):
#         if type(zzz)==int and type(xxx)==int:
#             return zzz+xxx
#         else:
#             print('您传递的参数中存在非整型的数字！')

# 尝调用这个变量
# try:
#     jisuan()
# except TypeError:
#     print('没给参数！')


# jisuan('哈哈哈',123)

# aa=jisuan(123,456)  #如果这样调用函数，我们发现并没有报错
# 但是也没有输出结果，为什么呢？应为我们的函数中并没有写输出语句，而是使用return来将计算结果反馈出来
# 这个时候我们就需要用到另外一个变量来承载返回的结果
# res=jisuan(123,456)
# print(res)  #这里使用了变量承载jisuan()的返回值并打印
# 或者我们也可以直接将这个函数调用后返回的结果打印出来

# 设定一个全局变量
# level=1
# def levelUp():
    # level+=1
    # 如上的写法，哦我们尝试这个函数中直接将level变量值加1
    # 错误的！会划红线报错，为什么呢？
    # 因为level是全局变量，在函数当中不能直接调用
    # 在函数当中涉及到对变量赋值操作，首先会认为可能是在函数中
    # 新创建了一个叫做level的局部变量，并对其进行赋值
    # 但是上述的例子中，局部范围内，原本并没有level变量的存在
    # 想要对其进行加法运算，肯定无从假期，所以会报错
    # 那么，如果我想要在函数当中对全局变量level进行加法个赋值运算怎么办呢？
    # 需要先声明一下，我这里使用全局变量level
    # global level
    # 然后在运算赋值
#     level+=1
# print('在函数没有被调用的时候，level的值是:',level)


# 尝试调用一个函数
# levelUp()
# print('调用函数后，level的值是:',level)

####练习#########
# 将原本的石头剪刀布当中判断输赢的部分做成函数来使用
#  定义函数名，并设置连个接参变量userAct--用来截取玩家出拳内容
# a = 0
# while a < 10:
#     play = int(input('请出石头（1）,剪刀（2），布（3）'))
#     import random
#     ran = random.randint(1,3)
#     def winOrLose(userAct,comAct):
#         global ran
#         #判断电脑和玩家输赢
#         if userAct == comAct:
#             print("电脑出的是",ran,"平")
#         elif userAct == 1 and comAct == 2:
#             print("电脑出的是",ran,"胜利")
#         elif userAct == 2 and comAct == 3:
#             print("电脑出的是",ran,"胜利")
#         elif userAct == 3 and comAct == 1:
#             print("电脑出的是",ran,"胜利")
#         else:
#             print("电脑出的是",ran,"失败")
#     winOrLose(play , ran)
###############################################

###########类#############
# 学习编程的时候，经常会听别人问你用的是面向过程的编程方法
# 还是面向对象的编程方法！
#
# 面向过程编程：流程化的，具体化的，面向过程编程当中，如果我们要解决一个问题
# 要分析首先应该做什么，其次做什么，一步一步的实现最终的功能
#
# 面向对象的编程：不需要知道具体的流程内容，只需要拿来别人或自己写好的工具使用即可
#
# 举个例子：
# 如果饿了要吃饭
# 如果用面向过程的方式解决这个问题，需要买菜，择菜，洗菜，切菜，炒菜，吃饭
# 如果用面向对象的方式解决这个问题，只需要点菜，吃饭
#
# class这个关键字用来声明类
# 类：是描述相同属性和方法的对象的集合，在类当总会去定义该集合当中每个对象所共有的属性和方法，对象是类的实例
# 类变量：类变量在整个实例化的对象当中是公用的
# 类变量定义在类当中且在在类当中的函数之外
# 方法的重写，如果我们的类具有继承的属性和方法的话
# 那么他可以通过重新定义继承于父类的方法的内容来对被继承的方法进行内容的重写（重定义）
# 局部变量：定义在方法当中的变量叫做局部变量，他只作用于当前实例化的类当中
# 实例变量：在声明的类当中，类的属性使用变量来表示的，这种变量被称为实例变量，他在类声明的内部，但是在类的其他成员方法之外
# 继承：一个类可以继承另一个类的属性和方法，被继承的类叫做父类（基类），继承别人的类叫做子类（派生类）
# 实例化：实例化用来创建一个类的实例，我们可以理解成刚定义的类，只是一个概念，想要让他实际起作用或着实例存在，需要对其进行实例化
# 在使用一个类的时候，必须要实例化它
#
# 如果定义类呢？？
#
# 语法格式：
# class 类名:
#     定义该类的葛总变量(属性)或函数(方法)

###############尝试在当前项目目录中创建一个新的py文件，叫做classtest文件#########################
# 在这个文件中，我们创建一个叫做s1的类
# 该类中，具有name,gender,height,weight等属性变量
# 同时还具有say()和jian()这两个方法
# #################################################################################################
# 在另外的文件中创建了s1的类，那么当前这个程序文件中中是否可以使用它呢
# 我们首先需要导入叫做classtest的py文件
# 平常我们我们导入某个库，某个包，用的就是这样的实例
#
# # # 导入了我们刚才编写的classtest这个py文件
# import classtest
# # 这里尝试实例化classtest文件中的s1类
# shi = classtest.s1()
# shi.say()   #调用类中的say()方法
# shi.jian(123,12)  #调用类中jian()方法

##################类的继承##########################
# 我们在当前文件中创建一个类
# class human():
#     name = "智人"
#     jie = "动物界"
#     men = "脊椎动物门-脊椎动物亚门"
#     gang = "哺乳纲-真兽亚纲"
#     mu = "灵长目-类人猿亚目"
#     ke = "人科-人亚科"
#     zu = "人猿"
#     shu = "人属"
#     zhong = "智人种-晚期智人亚种"
#     __siyoushuxing = "野蛮" #私有属性
#     # 私有属性只能在类的内部使用，无法在类的外部直接调用
#     # 上面设置了人类的属性，下面我们来为人类设置一个方法
#     def tools(self):
#         print("我们会使用工具，且具有自己的语言")
#
#     def private(self):
#         print("告诉你个秘密，我很"+self.__siyoushuxing)
#
# 尝试实例化一下human类
# renlei = human()
# 实例化后能不能调用其中的属性和方法呢？
# print("我们是",renlei.name+"属于",renlei.jie+renlei.gang,renlei.mu)
# renlei.tools()

# 那么私有属性能直接被调用吗？
# print(renlei.__siyoushuxing)
# 我们法向，不能够直接调用human类的私有属性,__siyoushuxing
# 那么如何调用他呢？
# 先在类中进行一些修改
# 我们刚才试着在垒中添加了方法private(),通过这个方法向外输出私有属性
# 再次尝试调用
# renlei.private()

# 我们刚刚创建了智人
# 下main我们来一个创建智人的子类
# class humanbeing(human): #在括号中协商父类的名字，才能实现继承
#     name = "现代"
#     __siyoushuxing = "相对文明"
#     def tools(self):
#         print("我们不光会使用工具，还会知道极为复杂的工具"
#               "甚至已经开始研究其他物种的语言")
#         print("我们"+self.__siyoushuxing)
# xiandairen = humanbeing()
# print("是否继承了父类的属性")
# print("我们",xiandairen.name,"我属于"+xiandairen.jie+xiandairen.men+xiandairen.gang+xiandairen.mu)
# xiandairen.tools()
#
# 一个子类是否可以拥有两个父类？没有问题的
# class father():
#     name = "爹"
#     gender = "男"
#     def abc(self):
#         print("我是你爸爸")
#     def hehe(self):
#         print("呵呵呵呵")
# class mother():
#     name = "娘"
#     gender = "女"
#     def abc(self):
#         print("我是你妈妈")
#     def heihei(self):
#         print("嘿嘿嘿嘿嘿")
# # 创建一个kid的类，这个类同时继承了father和mother两个类
# class kid(father,mother):
#     name = "崽儿"
# 那么kid的类到底及乘客谁的gender属性呢？继承了谁的笑声和说话方式呢？
# 实例化kid
# haizi = kid()
# print(haizi.gender)
# haizi.heihei()
# haizi.hehe()
# haizi.abc()
# 通过上面的实例，我们发现可以通过继承两个父类
# 但是在继承的时候，如果两个父类当中有同名属性或方法，那么在继承的过程中，那个父类的名字写在前面，则继承谁

######################石头剪刀布新资料篇#########################
# 该资料中，更新了以下内容
# 我们优化了程序代码，将某些功能性代码用函数来做了
# 游戏中加入了三个NPC，这三个NPC名字自定义
# 三个NPC每个人具备属性HP，MP，EXP，GULD，以及技能(def)
# 玩家开始游戏后，随机遇到其中的NPC之一，每次猜拳对决胜利后都能减少对方的HP血量
# NPC如果MP不为空的情况下，可以随机触发技能
# 如果NPC血量清零，玩家获得该NPC的经验和金币
# 当NPC败北后，随机出下一个NPC对手，但是注意，下一个NPC对手肯定不是刚才遇到的


# 定义三个NPC
class npcA():
    name = "迪丽热巴"
    hp = 3
    mp = 1
    exp = 20
    guld = 10
    def jineng(self):
        global hp
        global mp
        print("迪丽热巴发动了技能，HP+1，当前HP剩余"+self.hp)

class npcB():
    name = "古力娜扎"
    hp = 3
    mp = 2
    exp = 30
    guld = 15
    def jineng(self):
        global hp
        global mp
        print("古力娜扎发动了技能，HP+2，当前剩余"+self.hp)

class npcC():
    name = "马尔扎哈"
    hp = 3
    mp = 3
    exp = 50
    guld = 20
    def jineng(self):
        global hp
        global mp
        print("马儿扎哈发动了技能,HP+3，当前剩余"+self.hp)

# 定义玩家遇到的随机对手(实例化)
npclist = [npcA , npcB , npcC]
import random
who = random.choice(npclist)()
import time
print("正在匹配电脑玩家！")
time.sleep(1)
print("玩家 VS",who.name)
time.sleep(1)
print('游戏开始！')

uhp = 5         #玩家血量
useskill = 0    #电脑是否使用技能

while uhp > 0:
    time.sleep(1)
    print('=======================')
    print("您剩余血量为", uhp)
    print("========================")
    time.sleep(1)
    print("您对决的是：", who.name)
    print("血量为：", who.hp)
    print("可以释放", who.mp, "次技能（蓝量）")
    print("经验值为：", who.exp)
    print("赏金为：", who.guld, "金币")
    print("========================")
    # 判断电脑是否使用技能
    import random
    skillran = random.randint(1,10)
    if skillran == 1 or skillran == 3 or skillran == 9 and who.mp > 0:
        useskill = 1
    else:
        useskill = 0
    # 电脑使用技能时候，做什么操作
    if useskill == 1:
        if who.name == "迪丽热巴":
            who.hp += 1
            who.mp -= 1
        elif who.name == "古力娜扎":
            who.hp += 2
            who.mp -= 1
        elif who.name == "马儿扎哈":
            who.hp += 3
            who.mp -= 1
    else:
        play = int(input('请出石头（1）,剪刀（2），布（3）'))
        import random
        ran = random.randint(1,3)
        print('电脑出的是：',ran)
        if ((play == 1 and ran == 2) or
                (play == 2 and ran == 3) or
                (play == 3 and ran == 1)):
            print('恭喜你，你赢了')
            who.hp -= 1
        elif play == ran:
            print('平局')
        else:
            uhp -= 1
            print('很遗憾，你输了')
    print("=============本轮结束===============")





