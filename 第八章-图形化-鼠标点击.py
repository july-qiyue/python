# #########鼠标点击事件###############
# import tkinter as tk
# win = tk.Tk()
# win.resizable(0,0)
# win.geometry("400x400")
# win.title("鼠标点击事件")
#
# # 设置一个函数
# # 当该函数被调用的时候，将鼠标指针处于被绑定的元素当中的坐标为位置作为参数传递进函数中
# # 并在函数内，将该参数中包含的x轴坐标和y轴坐标打印输出
# def func(a):
#     print(a.x,a.y)
#
# # 设置了标签lab
# lab = tk.Label(win,text="点我啊",bg="Red")
# # 将标签lab通过bind()函数绑定了一个方法func
# # 同时我们使用了<Button-1>来绑定了除法func这个方法动作为单击鼠标左键
# lab.bind("<Button-1>",func)
# # <Button-1>  鼠标左键单击
# # <Button-2>  鼠标滚轮单击
# # <Button-3>  鼠标右键单击
# # <Double-Button-1>   双击鼠标左键
# # <Triple-Button-1>   三击鼠标左键
#
# lab.pack()
# win.mainloop()
# ===============================================================================================


# ===============================================================================================
##########鼠标移动事件#############
# import tkinter as tk
# win = tk.Tk()
# win.resizable(0,0)
# win.geometry("400x400")
# win.title("鼠标移动事件")
#
# def func(a):
#     print("当前鼠标的坐标为:",a.x,a.y)
#
# lab = tk.Label(win,text="按住鼠标在我身上游走",bg="black")
# lab.bind("<B1-Motion>",func)
# # <B1-Motion> 绑定鼠标左键被按下后地洞鼠标的动作
# # <B2-Motion> 绑定鼠标滚轮被按下后地洞鼠标的动作
# # <B3-Motion> 绑定鼠标右键被按下后地洞鼠标的动作
#
# lab.pack()
# win.mainloop()
# ===============================================================================================


# ===============================================================================================
# 小实验:
# 创建一个400x400的窗体
# 在这个窗体上,随机坐标产生一个label
# 当点击这个label的时候,该lable会消失,并重新在另一个坐标显现出来
# 点中了label则全局变量score加1
# 每次点击,全局变量shotTime-1,该变量的最大值为10
# 当shotTime的值为0时,不再产生新的label
score = 0
shottime = 10

import random
ran = random.randint(0,350)
ran1 = random.randint(0,350)

import tkinter as tk
import tkinter.messagebox as tkm
win = tk.Tk()
win.resizable(0, 0)
win.geometry("400x400")
win.title("测测你的反应")

def on(a):
    global score,shottime
    lab.place_forget()
    score += 1
    shottime -= 1
    labscore.config(text="Score:"+str(score))
    labtime.config(text="ShotTime:"+str(shottime))

def off(a):
    global shottime
    ran = random.randint(0, 350)
    ran1 = random.randint(0, 350)
    lab.unbind("ButtonRelease-1")
    lab.place(x=ran, y=ran1)
    if shottime < 1:
        lab.place_forget()
        labgame.pack()


# lab = tk.Label(win, text="点我", bg="green")
labscore = tk.Label(win,text="Score:"+str(score))
labtime = tk.Label(win,text="ShotTIme:"+str(shottime))
labgame = tk.Label(win,text="Game Over!",bg="red")
# frm = tk.Frame(win,width=400,height=400)    #框架
labimage = tk.PhotoImage(file=r"aa.png")  #打开指定文件
lab = tk.Label(win,image=labimage)  #在label当中,通过image=属性来定义使用图片

lab.bind("<Button-1>",on)
lab.bind("<ButtonRelease-1>",off)
labscore.place(x=10,y=370)
labtime.place(x=100,y=370)
lab.place(x=ran, y=ran1)

win.mainloop()


