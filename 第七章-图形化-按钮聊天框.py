###############使用python创建图形化界面程序########################
#
# # py原生的GUI图形化库-------tiinter
#
# # 调用库，并将其使用as关键字命名别名为tk
# import tkinter as tk
#
# # 如何使用这个库呢？
# # 首先要向将这个库当中的Tk()类实例化
# win = tk.Tk()
#
# # 将窗口显示出来（循环显示，如果不循环显示的话，则只会闪烁以下就不见了）
# win.mainloop()
#
# # 运行，则会出来一个窗口
#
# ========================================================================


# ============================================================================================
# # # 一、调用库，并将其使用as关键字命名别名为tk
# import tkinter as tk
#
#
# # # 二、如何使用这个库呢？
# # # 首先要向将这个库当中的Tk()类实例化
# win = tk.Tk()
#
# # 尝试给这个窗体添加一个名称
# win.title("Zworld")
#
# # 设置窗体的初始化大小,使用函数geometry()，在该函数的圆括号当中写入"窗体X轴宽度x窗体Y轴高度"来定义窗体大小
# win.geometry("800x600")
#
# # 三、设定窗口是否能被鼠标拖放，使用函数resizeable(),该函数中，圆括号内写X轴是否能被缩放，Y轴是否能被缩放
# # 是否可以缩放，用数字0(不可)或非0(可以)来表示
# # win.resizable(1,0) #纵向不能缩放，横向可以缩放
# # win.resizable(0,1) #横向不能缩放，纵向可以缩放
# win.resizable(0,0) #横纵都不能缩放
#
#
# # # 四、界面当中如何丰富呢？我们需要向其中添加各种图形化元素进去
#
# # # Label元素----文字标签
# # 格式：tk.Label(该标签所处的父级元素名称,text="标签中要写的文本内容",bg="标签背景颜色",fg="标签字体颜色")
# lab = tk.Label(win,text="欢迎使用！",bg="darkgray",fg="gold")
#
#
# # # 如果在程序执行后，达成某种条件的时候，我们想要将该标签取消显示怎么办？
# # lab.pack_forget()   # pack_forget()函数用来取消元素的显示
#
#
# # #、可让用户输入的文本框的设置，使用函数Entry()
# # 格式：tk.Entry(父元素名称,文本内容)
# Ent = tk.Entry(win,text="快来填满我!")
#
# # # 按钮的创建
# butt =tk.Button(win,text="点我啊")
#
#
# # 上面的lab内容只是设置了一个标签的内容和样式
# # 但是没有将"欢迎使用"这个标签放置在窗体中，如何放置呢？使用pack()布局函数
# # 放置标签元素，使其显示在窗体中
# lab.pack()
#
# # # 放置文本框Entry()对象
# # Ent.pack()
# # #元素的放置顺序决定了该元素的放置位置，lab元素在Ent上面，所以图形化中lab在上Ent在下
#
#
# # # 五、另外，我们发现在该界面中，每一个元素都自己独占了一行内容（默认）
# # # 如果我们想要让元素与元素放在同一行之内，就需要定的tkinter的布局方法
#
# # 1、绝对布局
# # 放置文本框，使用函数place()
# # 格式：place(x=X轴坐标,y=Y轴坐标)
# Ent.place(x=100,y=100)
#
# # 放置点击按钮
# butt.place(x=100,y=100)
#
#
# # # 将窗口显示出来（循环显示，如果不循环显示的话，则只会闪烁以下就不见了）
# win.mainloop()
#
# ============================================================================================



# ============================================================================================
# # 尝试制作注册界面
#
# # 调用库，并将其使用as关键字命名别名为tk
# import tkinter as tk
#
# # 将这个库当中的Tk()类实例化
# win = tk.Tk()
#
# # 尝试给这个窗体添加一个名称
# win.title("注册中心")
#
# # 设置窗体的初始化大小
# win.geometry("300x200")
#
# # 设定窗口是否能被鼠标拖放，使用函数resizeable(),该函数中，圆括号内写X轴是否能被缩放，Y轴是否能被缩放
# win.resizable(0,0) #横纵都不能缩放
#
# # Label元素----文字标签
# lab = tk.Label(win,text="欢迎登录")
# laba = tk.Label(win,text="用户名:")
# labb = tk.Label(win,text="密码:")
#
# # 可让用户输入的文本框的设置
# Ent = tk.Entry(win,text="用户")
# Entb = tk.Entry(win,text="密码")
#
# # 注册按钮的创建
# butt =tk.Button(win,text="注册")
#
# # 放置标签元素，使其显示在窗体中
# lab.pack()
#
# #用户名和密码布局
# laba.place(x=50,y=60)       #用户名布局
# labb.place(x=50,y=100)      #密码布局
#
# # 文本框布局
# Ent.place(x=100,y=60)       #用户名框
# Entb.place(x=100,y=100)     #密码框
#
# # 放置点击按钮
# butt.place(x=210,y=130)      #放置按钮
#
# # # 将窗口显示出来（循环显示，如果不循环显示的话，则只会闪烁以下就不见了）
# win.mainloop()

# ============================================================================================


# ============================================================================================
# 登录界面输入用户名和密码后，点击按钮获取账户名称和密码
# 连接数据库，查询是否能正常登录，如果可以
# 将界面内的原有内容全部清空，通过用户输入的账户和密码获取
# 对应账户的何种信息（）
# 将上述查出的角色的所有信息，显示在当前界面窗体中

# 调用库，并将其使用as关键字命名别名为tk
import tkinter as tk
import tkinter.messagebox as tkm

# 实例化
win = tk.Tk()

# 尝试给这个窗体添加一个名称
win.title("石头剪刀布")

# 设置窗体的初始化大小
win.geometry("300x200")

# 设定窗口是否能被鼠标拖放
win.resizable(0,0) #横纵都不能缩放

# 设置点击按钮后要做的事情
def getValuse():
    uname = Ent.get()
    upwd = Entb.get()
    # 连接数据库
    import pymysql
    db = pymysql.connect(host='192.168.43.180', port=3306
                         , user='root', passwd='123.com'
                         , charset='utf8', db='testA')
    cursor = db.cursor()
    #查询当前用户信息
    sql = """select * from sjbinfo where name ='""" + uname + """' and pass='""" + upwd + """';"""

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        if uname == results[0][0] and upwd == results[0][1]:
            tkm.showinfo("登录","登录成功！")
            # 登录成功后，将界面的所有内容消除
            lab.pack_forget()
            laba.place_forget()
            labb.place_forget()
            Ent.place_forget()
            Entb.place_forget()
            butt.place_forget()
            # 给当前用户设置变量
            for row in results:
                username = row[0]
                userlv = row[2]
                usergold = row[3]
                userexp = row[4]
                userwinning = row[5]
            # 显示新的用户信息
            out1 = tk.Label(win, text=("用户:",username))
            out2 = tk.Label(win, text=("等级:",userlv))
            out3 = tk.Label(win, text=("金币:",usergold))
            out4 = tk.Label(win, text=("经验:",userexp))
            out5 = tk.Label(win, text=("胜场:",userwinning))
            out1.place(x=100, y=30)  # 用户布局
            out2.place(x=100, y=50)  # 等级布局
            out3.place(x=100, y=70)  # 金币布局
            out4.place(x=100, y=90)  # 经验布局
            out5.place(x=100, y=110)  # 胜场布局
            res = tkm.askokcancel("退出","是否要退出？")
            print(res)
            win.quit()

        elif uname != results[0][0] and upwd != results[0][1]:
            print("登录失败")
    except:
        # 如果报错，执行回滚操作
        db.rollback()
        print('连接数据库错误!')
    db.close()



# Label元素----文字标签
lab = tk.Label(win,text="欢迎使用")
laba = tk.Label(win,text="用户名:")
labb = tk.Label(win,text="密码:")

# 可让用户输入的文本框的设置
Ent = tk.Entry(win,text="用户")
Entb = tk.Entry(win,text="密码")

# 注册按钮的创建#
butt = tk.Button(win,text="登录",command=getValuse)


# 放置标签元素，使其显示在窗体中
lab.pack()

#用户名和密码布局
laba.place(x=50,y=60)       #用户名布局
labb.place(x=50,y=100)      #密码布局

# 文本框布局
Ent.place(x=100,y=60)       #用户名框
Entb.place(x=100,y=100)     #密码框

# 放置点击按钮
butt.place(x=210,y=130)      #放置按钮

# # 将窗口显示出来（循环显示，如果不循环显示的话，则只会闪烁以下就不见了）
win.mainloop()























# ============================================================================================

