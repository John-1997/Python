from prettytable import PrettyTable  #表格
students=[]
#students=[{"name":"zhangs","gender":"男","id":"1"},{"name":"lisi","gender":"男","id":2},
#{"name":"maliu","gender":"男","id":3},{"name":"fengqi","gender":"男","id":4},{"name":"wangyuyan","gender":"女","id":5},{"name":"limochou","gender":"女","id":6}]
import random
global c
def add_student():
    i = 0
    leap=0
    while (1):
        sid=input("请输入学号（输入enter键结束录入）")
        if (not sid):
            #判断是否继续输入
            break
            i=0
            leap=0
        for temp in students:
            if temp['id'] == sid:
                 print("输入学号重复，请重输")
                 break
            else:
                 i=i+1  
            #判断是否为重复学号
        else:
            name=str(input("请输入姓名："))
            gen=str(input("请输入性别（男/女：）"))
            age=int(input("请输入年龄："))
            info={"id":sid,"name":name,"gender":gen,"age":age}
            students.append(info)
            print("录入成功")
        #print(students)
    print("信息录入完毕！")    
#add_student()
#domi=[[{"name":"zhangs"},{"name":"maliu"}],[{"name":"lisi"},{"name":"fengqi"}],[{"name":"wangwu"}],[],[],[]]
domi=[[],[],[],[],[],[]]
def dist_student():
    b=int(input("请选择寝室分配方式1 or 2(1为自动，2为手动)"))
    if b==1:
        #while 1:
        for gen in students:
          #print(gen)
          while 1:
            if gen["gender"]=='男':
                t=random.randint(0,2)
                print("t=%d"%t);
                if len(domi[t])==4:
                    a=t+100
                    print("a=%d"%a);
                    #print('%d寝室人数已满，请重输'%a)
                else:
                    domi[t].append(gen)
                    print(domi[t])
                   #break
                #print('%d男寝室人员信息'%(t+100),boys)
            if gen["gender"]=='女':
                t=random.randint(3,5)
                print("t=%d"%t);
                if len(domi[t])==4:
                    a=t+197
                    #print('%d寝室人数已满，请重输'%a)
                else:
                    domi[t].append(gen)
                    print(domi[t])
                    #break
            break
        #print(domi)
    if b==2:
        for gen in students:
            while 1:
                if gen["gender"]=='男':
                    t=int(input("请输入%s的寝室"%gen['name']))
                    if len(domi[t-100])==4:
                        print('%d寝室人数已满，请重输'%t)
                    else:
                        domi[t-100].append(gen)
                        break
                #print('%d男寝室人员信息'%(t),domi[t-100])
                if gen["gender"]=='女':
                    t=int(input("请输入%s的寝室"%gen['name']))
                    if len(domi[t-197])==4:
                        print('%d寝室人数已满，请重输'%t)
                    else:
                        domi[t-197].append(gen)
                break
                #print('%d女寝室人员信息'%(t),domi[t-197])
#dist_student()
def print_student():
    x = PrettyTable(['学号','姓名','性别','年龄'])        
    for i in range(0,6):
        if domi[i]==[]:
            continue
        if i<3:
            t=i+100
            print("%d寝室人员为："%t)
            for temp in domi[i]:
                a = temp.values()
                x = PrettyTable(['学号','姓名','年龄','性别'])
                x.add_row(a)
                print(x)
        if(i>2):
            t=i+197
            print("%d寝室人员为："%t)
            for temp in domi[i]:
                a = temp.values()
                x = PrettyTable(['学号','姓名','年龄','性别'])
                x.add_row(a)
                print(x)
   # print(x)
#print_student()
def requir_student():
    searchID=input("请输入需要查询的学号：")
    leap=0
    #print(searchID)
    for temp in students:
        #print(temp)
        #print(searchID)
        if temp['id']==searchID:
            leap=1
            x = PrettyTable(['学号','姓名','性别','年龄'])
            x.add_row([temp['id'],temp['name'],temp['age'],temp['gender']])
            print(x)

            #print("找到学生信息如下：")
            #print("学号：%s\n姓名：%s\n年龄：%d\n性别：%s\n"%(temp['id'],temp['name'],temp['age'],temp['gender']))
            break
    if leap==0:
            print("没有该学生信息，请重新输入！")
#requir_student()
def change_domitory():
    t=int(input("请选择单人调换寝室或两人寝室对调1 or 2(1为单人，2为对调)"))
    if t==1:
        changeName=input("请输入需要调换寝室同学姓名")
        for j in range(0,6):
          #print("j=%d"%j)
          k=-1
          #while 1:
          for temp in domi[j]:
              #print("j=%d"%j)
            #print(temp)
            #print(changeName)
            #print(temp['name'])
            #print(type(changeName))
            #print(type(temp['name']))
              if changeName == temp['name']:
                #print ("j=%d"%j)
                if j==0:
                    t=100
                    print("%s当前寝室是%d"%(changeName,t))
                    k=int(input("请输入调换寝室到(101或102)"))
                    mid=temp
                    domi[j].remove(temp) 
                    domi[k-100].append(mid)
                    k=2
                    #print(domi)
                    break
                if j==1:
                    t=101
                    print("%s当前寝室是%d"%(changeName,t))
                    k=int(input("请输入调换寝室到(100或102)"))
                    mid=temp
                    domi[j].remove(temp)
                    domi[k-100].append(mid)
                    k=2
                    #print(domi)
                    break
                if j==2:
                    t=102
                    print("%s当前寝室是%d"%(changeName,t))
                    k=int(input("请输入调换寝室到(101或100)"))
                    mid=temp
                    domi[j].remove(temp)
                    domi[k-100].append(mid)
                    k=2
                    #print(domi)
                    break
                if j==3:
                    t=200
                    print("%s当前寝室是%d"%(changeName,t))
                    k=int(input("请输入调换寝室到(201或202)"))
                    mid=temp
                    domi[j].remove(temp)
                    domi[k-197].append(mid)
                    k=2
                    #print(domi)
                    break
                if j==4:
                    t=201
                    print("%s当前寝室是%d"%(changeName,t))
                    k=int(input("请输入调换寝室到(200或202)"))
                    mid=temp
                    domi[j].remove(temp)
                    domi[k-197].append(mid)
                    k=2
                    #print(domi)
                    break
                if j==5:
                    t=202
                    print("%s当前寝室是%d"%(changeName,t))
                    k=int(input("请输入调换寝室到(200或201)"))
                    mid=temp
                    domi[j].remove(temp)
                    domi[k-197].append(mid)
                    k=2
                    #print(domi)
                    break
              if k==2:
                  #break
                  print("j=%d"%j)
                  print("没有该学生信息，请重新输入！")
                  break
          if k==1:
              break        
    if t==2:
      changeid1 = 0
    while 1:
        mid1=-1
        changename1=input("请输入第一个需要调换寝室同学姓名")
        #c=changeid1
        for j in range(0,6):
            for temp in domi[j]:
              #print("j1=%d"%j)
              if changename1 == temp['name']:
                  print ("j=%d"%j)
                  mid1=j
                  temp1=temp
                  break
        if(mid1!=-1):
            break
        if(mid1==-1):
            print("没有该同学信息请重输")
    while 1:
        mid2=-1
        changename2=input("请输入第二个需要调换寝室同学姓名")  
        for i in range(0,6):
            for temp in domi[i]:
              #print("xunhuan=%d"%j)
              #print("j=%d"%j)
              if changename2 == temp['name']:
                  print ("i=%d"%i)
                  mid2=i
                  print("mid2=%d"%mid2)
                  temp2=temp
                  break
        #if(mid2!=-1):
            #break
        if(mid2==-1):
                print("没有该同学信息请重输")
        if mid1<3 and mid2>2:
                print("请输入相同性别的姓名，重新输入第二名同学")
                #if(mid2 ==-1):
                    #break
                #break
        #if(mid2!=-1):
            #break
        #break
        if mid1>2 and mid2<3:
            print("请输入相同性别的姓名，重新输入第二名同学")
            #break
        if mid1<3 and mid2<3:
            break
        if mid1>2 and mid2>2:
            break
    if mid1<3 and mid2<3:
          print("t=%d"%mid1)
          domi[mid2].append(temp1)
          domi[mid1].append(temp2)
          domi[mid1].remove(temp1)
          domi[mid2].remove(temp2)
    if mid1>2 and mid2>2:
          domi[mid2].append(temp1)
          domi[mid1].append(temp2)
          domi[mid1].remove(temp1)
          domi[mid2].remove(temp2)
print("调用成功")
#change_domitory()
def interface():
    print('-'*30)
    print('学生寝室管理系统 v1.0')
    print('1.添加学生信息')
    print('2.分配寝室')
    print('3.打印寝室人员列表')
    print('4.查找学生')
    print('5.寝室调换')
    print('0.退出')
    print('-'*30)

def file_recover():#从文件中提取信息
  global  students
  f=open('D:/manege system.txt')
  content1=f.read()
  students=eval(content1)     #eval---转换成列表
  f.close ()
 
def file_save():  #保存所有x学生的信息
 f=open('D:/manege system.txt','w')
 f.write(str(students))       #str--转换成字符串
 f.close()


while True:
    file_recover()
    interface()
    data = int(input("请输入选择业务："))   
    if data ==1:
        add_student()
        file_save()
    elif data == 2:                     
        dist_student()
        file_save()     #分配了寝室需要存档
    elif data == 3:
        print_student()
    elif data == 4:
        requir_student()
    elif data == 5:
        change_domitory()
        file_save()     #换了寝室之后必须存入文件，不然寝室信息不会改变
    elif data == 0:
        exit_signal = input("确定要退出吗？(Y/N)：")
        if exit_signal == 'Y':
            break
        else:
            print("输入有误，请重新输入")
    else:                                       
        print("输入错误，请重新输入！")





























        
