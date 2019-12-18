# 使用python连接数据库
# 1.安装mysql（虚拟机或真机都可以）
# 2.确保虚拟机中的数据库能够让真机访问到(授权)
# 3.防火墙放行端口设置
# 4.python安装一个库(Terminal---执行：pip install PyMySQL)


# ========================================================================================================================================================
# # 导入PyMySQL
# import pymysql
#
# # 创建数据库的连接
# #格式：
# # 变量名 = pymysql.connect(host = '数据库服务器地址' , port = 3306
# #                       , user = '数据库访问用户名'
# #                       , passwd = '数据库用户密码'
# #                       , charset = '编码格式')
# db = pymysql.connect(host = '192.168.43.180' , port = 3306
#                       , user = 'root' , passwd = '123.com'
#                       , charset = 'utf8')
#
# # 创建指针，指针用来对数据库进行详细操作
# # 使用cursor()方法！
# cursor = db.cursor()
#
# # 对指针设定具体的操作，使用了方法execute()
# # 圆括号里写的是具体的sql语句，这里写的select version()是查看数据库版本
# cursor.execute('select version()')
#
# # fetchone()这个方法用来获取指针操作后返回的单条数据
# data = cursor.fetchone()
#
# # 打印结果
# print('database version: %s' % data)
#
# # 关闭与数据库的连接
# db.close()
# # 到此为止，我们运行就可以获得是否则正确连接到数据库的结果了
# ========================================================================================================================================================


# ========================================================================================================================================================
# 数据库的增删改查
# insert插入（对数据库内容的增加）
# delete删除（对数据库内容的删除）
# update更新（对数据库以有内容的改变）
# select选择（对数据库内容的查询）
# ========================================================================================================================================================


# ========================================================================================================================================================
# # 增操作--insert
# import pymysql
#
# # 在数据库中创建zzz库，在zzz库中创建zuser表
# # MariaDB [(none)]> create database zzz;
# #
# # MariaDB [(none)]> use zzz;
# #
# # MariaDB [zzz]> create table zuser(zid int(4) auto_increment primary key,zname varchar(20) not null unique,zpwd varchar(20) not null);
#
# # 创建连接的时候要知道库名
# db = pymysql.connect(host = '192.168.43.180' , port = 3306
#                       , user = 'root' , passwd = '123.com'
#                       , charset = 'utf8' , db = 'zzz' )
#
# # 创建指针
# cursor =db.cursor()
#
# # 切换数据库
# cd = 'use zzz'
# cursor.execute(cd)
#
# na = input('请输入用户名：')
# pw = input('请输入密码：')
#
# # 创建插入语句
# # sql = """insert into zzz.zuser(zname,zpwd) values('用户名','密码')"""
# sql = """insert into zzz.zuser(zname,zpwd) values('"""+na+"""','"""+pw+"""')"""
#
# # 尝试执行sql语句
# try:
#     cursor.execute(sql)
# # 提交数据到数据库
#     db.commit()
# except:
#     #如果报错，执行回滚操作
#     db.rollback()
#     print('连接数据库错误!')
#
# # 操作完成后，关闭数据库
# db.close()
#
# # 执行，并在数据库中验证
# ========================================================================================================================================================


# ========================================================================================================================================================
# # 数据库查询操作--select
# # 创建连接的时候要知道库名
# import pymysql
#
# db = pymysql.connect(host = '192.168.43.180' , port = 3306
#                       , user = 'root' , passwd = '123.com'
#                       , charset = 'utf8' , db = 'zzz' )
#
# # 创建指针
# cursor =db.cursor()
#
# # 创建查询语句
# sql = 'select * from zuser;'
#
# # # # 执行sql语句
# # # cursor.execute(sql)
# # # # 这里使用了fetchall()
# # # results = cursor.fetchall()
# # # # 输出
# # # print(results)
#
# # 异常排查尝试执行
# try:
#     cursor.execute(sql)    #执行sql语句
#     results = cursor.fetchall()     #这里使用了fetchall()
#     # 因为查询的结果未必是一个，所以用到了fetchall()方法，获得所有查询结果
#     # 使用for循环语句遍历得到的所有查询结果
#     # 每次遍历的时候，row遍历都会被赋值为一整条数据内容
#     # 这一整条内容，在我们yonghu表中包含了三个字段，分别是id，username，userpass
#     for row in results:
#         # 所以每一次循环，我们都定义了一个变量来承载每个字段的数据内容
#         userid = row[0]     # 获取id字段的内容
#         username = row[1]   # 获取第二个字段username的内容
#         userpass = row[2]   # 获取第三个字段userpass的内容
#         # 每次循环都打印输出得到的结果
#         print('用户ID：',userid,'用户名：',username,'密码：',userpass)
# except:
#     print('连接错误')
# db.close()
# ========================================================================================================================================================


# ========================================================================================================================================================
# # 删除数据--delete
# # 导入模块
# import pymysql
#
# # 连接数据库
# db = pymysql.connect(host = '192.168.43.180' , port = 3306
#                       , user = 'root' , passwd = '123.com'
#                       , charset = 'utf8' , db = 'zzz' )
#
# # 创建指针
# cursor =db.cursor()
#
# # 创建删除sql语句
# sql = "delete from zuser where zname='ajjaj'"
#
# try:
#     cursor.execute(sql)
#     db.commit()
#     print('成功删除！')
# except:
#     db.rollback()
#     print("数据库错误！")
#
# db.close()
#
# # 去数据库验证是否删除
# ========================================================================================================================================================


# ========================================================================================================================================================
# # 改操作--update
# # 导入模块
# import pymysql
#
# # 连接数据库
# db = pymysql.connect(host = '192.168.43.180' , port = 3306
#                       , user = 'root' , passwd = '123.com'
#                       , charset = 'utf8' , db = 'zzz' )
#
# # 创建指针
# cursor =db.cursor()
#
# # 创建修改数据库内容
# sql = "update zuser set zname='hahaha' where zname='lyl'"
#
# try:
#     cursor.execute(sql)
#     db.commit()
#     print('成功修改！')
# except:
#     db.rollback()
#     print("数据库错误！")
#
# db.close()
#
# # 去数据库验证结果
# ========================================================================================================================================================


# ========================================================================================================================================================
# # 练习1：
# # 1.在数据库中创建一个sjbinfo表
# # 2.改表字段如下：用户名，密码，等级，金币，经验，连胜次数
# # 3.尝试让用户注册账户，当用户注册后，使用用户注册的名称和密码以及默认0等级0金币0经验0连胜向表内插入一条数据
# # 4.插入成功的话，通过查询将插入后的所有内容显示出来
# # 5.显示过程中，应该将每个字段拆分开显示，用户名：xxx 密码：xxx....
#
# # 先在数据库中创建一个test的库，再创建一个sjbinfo的表，并添加字段
# # MariaDB [(none)]> create database testA;
# # MariaDB [(none)]> use testA;
# # MariaDB [testA]> create table sjbinfo (name char(20), pass char(20), lv int, gold int,exp int, winning int);
#
#
# def zhuce():
#     # 导入模块
#     import pymysql
#
#     # 连接数据库
#     db = pymysql.connect(host='192.168.43.180', port=3306
#                          , user='root', passwd='123.com'
#                          , charset='utf8', db='testA')
#
#     # 创建指针
#     cursor = db.cursor()
#
#     uname = input('请输入要注册的用户名：')
#     upass = input('请输入密码：')
#
#     # 创建插入数据
#     sql = """insert into testA.sjbinfo(name,pass,lv,gold,exp,winning) values('"""+uname+"""','"""+upass+"""','0','0','0','0')"""
#
#     # 尝试执行sql语句
#     try:
#         cursor.execute(sql)
#     # 提交数据到数据库
#         db.commit()
#     except:
#         #如果报错，执行回滚操作
#         db.rollback()
#         print('数据无法写入，连接数据库错误!')
#     db.close()
#
#
# # 查询内容
# def chaxun():
#     # 导入模块
#     import pymysql
#
#     # 连接数据库
#     db = pymysql.connect(host='192.168.43.180', port=3306
#                          , user='root', passwd='123.com'
#                          , charset='utf8', db='testA')
#
#     # 创建指针
#     cursor = db.cursor()
#
#     cat = 'select * from sjbinfo;'
#     try:
#         cursor.execute(cat)
#         results = cursor.fetchall()
#         for row in results:
#             username = row[0]
#             userpass = row[1]
#             userlv = row[2]
#             usergold = row[3]
#             userexp = row[4]
#             userwinning = row[5]
#             print('用户名',username,'密码：',userpass,'等级：',userlv,'金币：',usergold,'经验：',userexp,'连胜次数：',userwinning)
#     except:
#         print('查询失败！连接数据库错误！')
#     db.close()
#
# play = input('注册/查询：')
# if play == '注册':
#     zhuce()
# elif play == '查询':
#     chaxun()
# else:
#     print('您的输入有误！暂时不支持此功能！')
# ========================================================================================================================================================


# ========================================================================================================================================================
# 练习2：
# 在程序运行的时候可以选择进行网络游戏或本地单机游戏
# 如果选择了网络游戏，则需要通过用户名和密码进行登录验证
# 如果没有注册过，则需要先进行注册。向数据库写入新用户的用户名以及密码等内容
# 验证成功后，从数据库中获取当前指定用户对应的属性内容
# 每次哦安定胜利失败后，同时向数据库中修改玩家的指定属性值，如当前等级或经验并能够在游戏中提现用户连胜记录排名
# 游戏中各种玩家信息均为数据库中查询得出
#
a = 5    # 生命值
ls = 0  # 连胜
s = 0   # 金币数量
ex = 0  # 经验数量
lv = 0  # 等级
uname = ""
upwd = ""


def danji():
    global a
    global ls
    global s
    global ex
    global lv
    while a < 6 and a > 0:
        print('==============单机模式==============')
        print('=============石头剪刀布=============')
        print("您的等级为", lv, "级")
        print("您的经验值为", ex)
        print("您剩余", a , "生命值")
        print("您持有金币数量为", s)
        # 设置要求，连胜次数5次以上，添加
        if ls >= 5:
            ls -= 5
            a += 1
            print("达成5连胜", "生命值+1")
        import random
        ran = random.randint(1, 3)
        print('电脑出的是：', ran)
        play = int(input('请出石头（1）,剪刀（2），布（3）'))
        if ((play == 1 and ran == 2) or
                (play == 2 and ran == 3) or
                (play == 3 and ran == 1)):
            ls += 1
            s += 1
            ex += random.randrange(10,20)
            if ex >= 50:
                lv += 1
                ex = 0
                print('恭喜你，升到' ,lv ,'级了')
            print('恭喜你，你赢了')
            print('剩余生命值：', a)
        elif play == ran:
            print('平局')
            a = a - 1
            ls = 0
            print('剩余生命值：', a)
        elif ((play == 2 and ran == 1) or
              (play == 3 and ran == 2) or
              (play == 1 and ran == 3)):
            print('很遗憾，你输了')
            a = a - 1
            print('剩余生命值：', a)
        else:
            print('您的输入有误！')
            a = a - 1
            print('剩余机会：', a)

def wangluo():
    useract = input('您是要登录/注册/查询（按Q退出）：')
    while useract != 'Q':
        if useract == '登录':
            pan = denglu()
            if pan == '登录失败':
                print('用户不存在！')
            elif pan == '登录成功':
                import time
                global a
                global ls
                global s
                global ex
                global lv

                # 导入模块
                import pymysql

                # 连接数据库
                db = pymysql.connect(host='192.168.43.180', port=3306
                                     , user='root', passwd='123.com'
                                     , charset='utf8', db='testA')

                # 创建指针
                cursor = db.cursor()

                lvs = """select * from sjbinfo where name ='""" + uname + """' and pass='""" + upwd + """';"""
                try:
                    cursor.execute(lvs)
                    results = cursor.fetchall()
                    lv = results[0][2]
                    ex = results[0][4]
                    s = results[0][3]
                    ls = results[0][5]
                except:
                    print('查询失败！连接数据库错误！')
                db.close()

                while a < 6 and a > 0:
                    print('========网络模式==========')
                    print('=======石头剪刀布==========')
                    print("您的等级为", lv, "级")
                    print("您的经验值为", ex)
                    print("您剩余", a, "生命值")
                    print("您持有金币数量为", s)
                    if ((ls != 0) or (s != 0) or (ex != 0) or (lv != 0)):
                        xiugai()
                    # 设置要求，连胜次数5次以上，添加
                    if ls >= 5:
                        ls -= 5
                        a += 1
                        print("达成5连胜", "生命值+1")
                    import random
                    ran = random.randint(1, 3)
                    print('电脑出的是：', ran)
                    play = int(input('请出石头（1）,剪刀（2），布（3）'))
                    if ((play == 1 and ran == 2) or
                            (play == 2 and ran == 3) or
                            (play == 3 and ran == 1)):
                        ls += 1
                        s += 1
                        ex += random.randrange(10,20)
                        if ex >= 50:
                            lv += 1
                            ex = 0
                            print('恭喜你，升到', lv, '级了')
                        print('恭喜你，你赢了')
                        print('剩余生命值：', a)
                        time.sleep(1)
                    elif play == ran:
                        print('平局')
                        a = a - 1
                        ls = 0
                        print('剩余生命值：', a)
                    elif ((play == 2 and ran == 1) or
                          (play == 3 and ran == 2) or
                          (play == 1 and ran == 3)):
                        print('很遗憾，你输了')
                        a = a - 1
                        print('剩余生命值：', a)
                        time.sleep(1)
                    else:
                        print('您的输入有误！')
                        a = a - 1
                        print('剩余生命值：', a)
                        time.sleep(1)
                print('次数耗尽')
                time.sleep(2)

        elif useract == '注册':
            zhuce()
        elif useract == '查询':
            chaxun()
        else:
            print('您的输入有误！')
            break
        useract = input('您是要登录/注册/查询（按Q退出）：')
    else:
        print('程序已退出')


def denglu():
    global uname
    global upwd
    # 导入模块
    import pymysql

    # 连接数据库
    db = pymysql.connect(host='192.168.43.180', port=3306
                         , user='root', passwd='123.com'
                         , charset='utf8', db='testA')

    # 创建指针
    cursor = db.cursor()

    uname = input("请输入用户名：")
    upwd = input("请输入密码：")

    #创建sql语句
    sql = """select * from sjbinfo where name ='""" + uname + """' and pass='""" + upwd + """';"""

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if uname == results[0][0] and upwd == results[0][1]:
            return '登录成功'
        elif uname != results[0][0] and upwd != results[0][1]:
            return '登录失败'
    except:
        #如果报错，执行回滚操作
        db.rollback()
        print('连接数据库错误!')
    db.close()



def zhuce():
    # 导入模块
    import pymysql

    # 连接数据库
    db = pymysql.connect(host='192.168.43.180', port=3306
                         , user='root', passwd='123.com'
                         , charset='utf8', db='testA')

    # 创建指针
    cursor = db.cursor()
    uname = input('请输入要注册的用户名：')
    upass = input('请输入密码：')
    upass2 = input('请再次输入密码：')
    if upass != upass2:
        print('俩次密码不一致，请重写输入！')

    # 创建插入数据
    sql = """insert into testA.sjbinfo(name,pass,lv,gold,exp,winning) values('"""+uname+"""','"""+upass+"""','0','0','0','0')"""

    # 尝试执行sql语句
    try:
        cursor.execute(sql)
    # 提交数据到数据库
        db.commit()
        print('注册成功！')
    except:
        #如果报错，执行回滚操作
        db.rollback()
        print('数据无法写入，连接数据库错误!')
    db.close()


# 修改内容
def xiugai():
    global a
    global ls
    global s
    global ex
    global lv
    global uname
    global upwd

    # 导入模块
    import pymysql

    # 连接数据库
    db = pymysql.connect(host='192.168.43.180', port=3306
                         , user='root', passwd='123.com'
                         , charset='utf8', db='testA')

    # 创建指针
    cursor = db.cursor()

    sql = """update sjbinfo  set lv='""" + str(lv) + """',gold='""" + str(s) + """',exp='""" + str(
        ex) + """',winning='""" + str(ls) + """' where name='""" + str(uname) + """' and pass='""" + str(
        upwd) + """';"""


    try:
        cursor.execute(sql)
        db.commit()
        # print("数据已成功写入数据库！")
    except:
        db.rollback()
        print("数据库错误，数据没有写入到数据库！")
    db.close()




# 查询内容
def chaxun():
    # 导入模块
    import pymysql

    # 连接数据库
    db = pymysql.connect(host='192.168.43.180', port=3306
                         , user='root', passwd='123.com'
                         , charset='utf8', db='testA')

    # 创建指针
    cursor = db.cursor()

    cat = 'select * from sjbinfo;'
    try:
        cursor.execute(cat)
        results = cursor.fetchall()
        for row in results:
            username = row[0]
            userpass = row[1]
            userlv = row[2]
            usergold = row[3]
            userexp = row[4]
            userwinning = row[5]
            print('用户名:',username,'密码:',userpass,' ','等级:',userlv,' ','金币:',usergold,' ','经验:',userexp,' ','连胜次数:',userwinning)
    except:
        print('查询失败！连接数据库错误！')
    db.close()


game = input('您要进行单机游戏还是网络游戏？单机/网络：')
if game == '单机':
    danji()
if game == '网络':
    wangluo()
else:
    print('您的输入有误！暂时不支持此功能！')

# ========================================================================================================================================================