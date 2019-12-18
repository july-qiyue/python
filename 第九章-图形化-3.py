# ====================================================================================================
##########鼠标进入和离开######################
# import tkinter as tk
# import tkinter.messagebox as tkm
#
# win = tk.Tk()
# win.resizable(0,0)
# win.geometry("400x400")
# win.title("进入和离开事件")
#
# def func(a):
#     print(a.x,a.y)
#
# frm = tk.Frame(win,width=400,height=400)
# labimg = tk.PhotoImage(file=r"aa.png")
# lab = tk.Label(frm,image=labimg)
# lab.bind("<Enter>",func)    #<Enter>鼠标进入被绑定的元素当中触发的方法
# lab.bind("<Leave>",func)    #<Enter>鼠标离开被绑定的元素当中触发的方法
# frm.pack()
# lab.pack()
#
# win.mainloop()
# =====================================================================================================


# =====================================================================================================
##############对键盘任意键的绑定############
# import tkinter as tk
# import tkinter.messagebox as tkm
#
# win = tk.Tk()
# win.resizable(0,0)
# win.geometry("400x400")
# win.title("绑定键盘按键")
#
# def func(a):
#     # print(a.x,a.y)
#     print('a.char=',a.char)         # 按下键的字符
#     print('a.keycode=',a.keycode)   # 按下键的键码值
#
# frm = tk.Frame(win,width=400,height=400)
# labimg = tk.PhotoImage(file=r"aa.png")
# lab = tk.Label(frm,image=labimg)
# lab.focus_set()
# lab.bind("<Key>",func)
# frm.pack()
# lab.pack()
# win.mainloop()
# =====================================================================================================


# =====================================================================================================
# # ###########绑定指定的键########
# import tkinter as tk
# import tkinter.messagebox as tkm
#
# win = tk.Tk()
# win.resizable(0,0)
# win.geometry("400x400")
# win.title("特殊按键的绑定")
#
# def func(a):
#     print('您按下了F1键')
#     print('该键的键码值为:',a.keycode)
#
# frm = tk.Frame(win,width=400,height=400)
# labimg = tk.PhotoImage(file=r"aa.png")
# lab = tk.Label(frm,image=labimg)
# lab.focus_set()
# lab.bind("<F1>",func)
# # 特殊按键一般都是没有对应的字符信息，除F1之外还有：
# # <Return> 回车键
# # <Escape> ESC键
# # <Shift_L> 左Shift
# # <Shift_R> 右Shift
# # <BackSpace> 退格键
# frm.pack()
# lab.pack()
# win.mainloop()
# =====================================================================================================


# =====================================================================================================
# 小练习：
# 写一个图形界面，上面要有一个承载了png图片的label
# 这个label绑定了所有键盘按键
# 当按下d键的时候，该图片会向右移动2像素，按下w向上移动，a向左，s向下
import tkinter as tk

win = tk.Tk()
win.resizable(0,0)
win.geometry("400x400")
win.title("移动图片测试")
x=100
y=100

def func(a):
    global x,y
    if a.char == 'a':
        x -= 10
        lab.place(x=x,y=y)
    elif a.char == 'd':
        x += 10
        lab.place(x=x,y=y)
    elif a.char == 'w':
        y -= 10
        lab.place(x=x,y=y)
    elif a.char == 's':
        y += 10
        lab.place(x=x,y=y)

frm = tk.Frame(win,width=400,height=400)
labimg = tk.PhotoImage(file=r"aa.png")
lab = tk.Label(frm,image=labimg)
lab.focus_set()
lab.bind("<Key>",func)

frm.pack()
lab.place(x=x,y=y)
win.mainloop()


# =====================================================================================================