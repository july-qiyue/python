# 声明一个类，类名叫做lyl
class s1:
    name = "十一"
    gender = "男"
    hight = "180"
    weight = "150"
    #设置s1这个类的方法self代表了该类本身
    def say(self):
        print("我是" , self.name , "我的性别是" ,self.gender ,
              "我的身高是" , self.gender , "体重是" ,self.weight ,
              "我会做减法jian()")
    def jian(self,x,y): #设置减法运算的方法
        print(x,"-",y,"=",x-y)