#我们可以是用python来打开指定的文件对其内容进行读写操作
#那么我们需要使用到open函数

# 格式：
# open("文件的名称及路径",mode:"何种方式打开")

####有哪些打开方式####
# r:以只读的方式打开文件，这个时候文本当中的光标默认在文件开头位置
# rb:以二进制格式打开一个文件用于只读操作，文本的光标会在文件的开头位置
# r+:打开文件用于读写，光标会在开头
# rb+:二进制格式打开文件用于读写，光标开头位置
# w:打开文件用来写入操作，如果我们的文件已经存在了，那么写入的内容覆盖原有内容，如果不存在则会新建光标位置在文本开头
# wb:二进制格式打开文件用于写入操作
# w+:读写方式打开文件
# wh+:二进制格式读写打开文件
# a:打开文件用于追加内容，光标会在文本的末尾位置，如果文件已经存在，则是进行内容的追加，如果不存在则会进行文件的新建写入
# ab:以二进制方式打开文件用于追加内容，光标会在文本的末尾位置，如果文件不存在则会进行文件的新建写入
# a+:读写方式打开文件进行内容追加
# ab+:二进制格式读写方式打开文件进行内容追加
# x:新建文件，如果创建的文件已经存在则会报错
##########################################################

# 现在我们来尝试使用open（）函数打开一个指定的文件
# 首先，请在我们的项目所在目录中，创建一个文本文件
# aa=open('python.txt',mode='rb')#以只读的方式打开文件python.txt,并将打开后文件交给一个变量aa
# result=aa.read()#对打开的文件aa进行读操作并将其读取的结果交给result变量
# print(result)#打印读取的结果
# #注：无法正确读取txt文件，提示无法按照gdk格式打开读取
# 使用下面的方法尝试

#######尝试，将刚才的内容进行修改，改为嘿嘿！！######
# aa=open("python.txt",mode="w")
# stri="嘿嘿！！"
# aa.write(stri)
# aa.close()#注意打开的文件在使用后要关闭
# print(stri)
#另一种方法修改内容
# open("python.txt",mode="w").write("heihei!!")

#####隐写#####
# img=open("img.jpg",mode="a")
# # stri="www.baidu.com.fxx.shazi"
# # img.write(stri)
# # img.close()
# # print(stri)
# # img=open("img.jpg",mode="rb")
# # print(img.read())

#####将刚才隐写的图片复制一张#####
#副本图片名称叫做newimg.jpg（gif.png）
# img=open("img.jpg",mode="rb")#读取方式打开原始图片
# newpic=img.read()#读取原图片内容并存储到变量
# img.close()#关闭刚才打开的文件
# img=open("newimg.jpg",mode="wb")#写二进制方式打开新的文件，这时文件不会存在就会被创建
# img.write(newpic)#向打开的新文件内写入内容
# img.close()#关闭新文件

#####异常排查语句
# 在编写程序的时候，经常会出现语法错误，格式错误等等，能够在编写代码的过程中排除的错误，我们不用去考虑它
# 但是难免会在程序写完后发现某个地方报错，影响我们的运行
# 那么我们可以通过使用异常排查语句，在拟定的代码段位置
# 实现写好对可能出现的情况的排查和处理
# 那么就需要用到异常排查语句---try...exception
# open("new.txt",mode="x")
#在第一次执行上面的代码的时候，我们发现是可以正常运行的
# 但是在第二次使用的时候报错了
# 原因是已经创建过了
# 用户子输入的文件名已经存在了，那么我们可以添加提示语
# try:
#     open("new.txt",mode="x")
# except FileExistsError:
#     print("您指定要创建的新文件已经存在")
# 上面的代码，我们使用try语句，在这里try:后面内容写的是尝试去执行的事情
# except后面写的FileExistsError是事先预判可能出现的具体的错误情况
# 在except的冒号下面所写的，是对指定的错误情况
# 出现后程序应该做出的反应和处理方法

#####根据上面的语法格式和内容
# 尝试让用户输入一个字符串，使用这个字符串作为文件名称，进行新文件的创建
# 其中应该有异常排查语句。针对文件已经存在的错误做出相应的处理
# 如果用户指定的文件本身不存在，那么直接创建它即可
# 如果用户指定要创建的文件已经存在，那么告知用户文件名已经存在
# 并让用户重新输入用户名进行文件的创建
# suc="no"
# while suc=="no":
#     aa = input('请输入文件名(带后缀)：')  #让用户输入要创建的文件名
#     try:    #尝试执行
#         open(aa, mode="x")  #尝试创建
#         suc = "yes" #创建成功后suc的变量值改为yes
#     except FileExistsError: #排查异常
#         print('文件名已存在，请重新输入文件名进行创建！') #如果失败告诉用户文件名已经存在
#     else:
#         print('创建成功')
#     finally:    #这个是最终结果，不管成功与不成功都会出项这句话
#         print('创建成功与创建不成功你都会看到这句话！！！')
##split()函数用来按照条件分割字符串
#split()圆括号中的第一个位置写的是分割字符串的条件，上述例子中以","逗号来分割
#第二个位置2这个数字代表了切割两次

########石头剪刀布游戏的再次更新########
# 1、玩家注册后，需要登陆验证才能进入游戏；
# 2、玩家的注册信息被记录到本地的某个文档中；
# 3、记录玩家账号的文件以每个玩家的用户名命名
# 4、玩家第一次进入游戏中，会将该玩家的初始化属性值全部记录到某个存档文件中；
# 5、在每一局游戏过后，应该询问玩家是否存档，如果玩家选择存档，则将当下玩家的各项属性值更新到指定存档中;
# 6、玩家登陆游戏时，应该询问是进行新游戏/读取存档；
# 7、如果读取存档，则读取玩家指定的存档=内容，并将存档中存储的属性加载到游戏中











