#
#Class namer 1.0 Github-IcyBlue17
lang =0
import random
import time
#def chouhao(lang2):
    #if lang2 == 1:
      #  print('现在是中文模式！')
        #hs=random.randint(1,46)
      #  print(hs)
   # if lang2 == 2:
      #  print('English model!')
        #hs=random.randint(1,46)
      #  print(hs)
while True:
    try:
     print('''
     Select your language
     1.简体中文
      2.English
      3.Exit
      3.退出''')
     lang=int(input('Enter 1 or 2 to select!输入1或者2选择语言!'))
     if lang == 1:     
        print('现在是中文模式')
        rs=int(input('输入班级人数！'))
        while True:
            hs=random.randint(1,rs)
            print('请',hs,'号同学回答！')
            jixu=int(input('输入任意数字抽取下一个！,输入80停止抽取！'))
            if jixu == 80:
                break
            else:
                continue   
     if lang == 2:
        print('Language:English')
        rs=int(input('How many people in your class?'))
        while True:
            hs=random.randint(1,rs)
            print('The number of student is',hs)
            jixu=int(input('Enter any number to continue,enter 80 to stop'))
            if jixu == 80:
                break
            else:
                continue
     if lang == 3:
         break
    except ValueError:
        print('您输入了字符代替了数字，请重试！')
        print('You inputed the word to instead number,please try again!')
        continue
#https://heipg.cn/tag/OpenCore-Configurator
#This is something you shoudn't care about!XD
