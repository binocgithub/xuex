from random import random


print("2**4=",2**4)
print("1024*768=",1024*768)
age =  18.5
name="Tom"
weight=75.5
stuId=21
print('今年我的年龄是%d岁'%age)
print('我的名字是%s'%name)
print('我的体重是%.2f公斤'%weight)
print ('我的学号是%03d'%stuId)
print ('我叫%s,今年%d岁了，明年%d，我的体重是%.1f,学号是%03d'%(name,age,age+1,weight,stuId))
print ('我叫%s,今年%s岁了，明年%s，我的体重是%5s,学号是%6s'%(name,age,age+1,weight,stuId))
print (f'我叫{name}，今年{age}岁了，明年{age+1}，我的体重是{weight}，学号是{stuId}')
print ('hello \npty\thon')

print ('hello',end='\t')
print ('word',end='123321')
print ("python")

c=10
c+=1+2
print(c)
d=10
d*=1+2
print(d)

onlineage=int(input("请输入年龄"))
if onlineage>=18:
    print("你的年龄为%s，可以上网。" %onlineage)
else:
    print(f"你的年龄为{onlineage}，不能上网。")
print("系统关闭")
if onlineage<16:
    print(f"你今年{onlineage}岁，属于童工，不合法")
elif (onlineage>=16) and (onlineage<=60):
    print(f"你今年{onlineage}岁，属于合法劳动年龄")
else:
    print(f"你今年{onlineage}岁，退休年龄")

#石头剪刀步游戏
import random
computer=random.randint(0,2)

player=int(input("请出拳，石头是0，剪刀是1，布是2："))
if (player==0 and computer==1) or (player==1 and computer==2) or (player==2 and computer==0):
    print(f"玩家出的是:,{player},电脑出的是:{computer},玩家获胜")
elif player==computer:
    print(f"玩家出的是:,{player},电脑出的是:{computer},平局")
else:
    print(f"玩家出的是:,{player},电脑出的是:{computer},电脑获胜")