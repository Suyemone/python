import tkinter
from logging import root
from tkinter import *
import tkinter.messagebox
win = tkinter.Tk
win = Tk()
win.title("党史知识答题")
num = []

for i in range(1,100):
    num.append(i)

    def close():
        
        print("第%s题%s"%(num[0],textbox))
        print("第%s题%s"%(num[0],textbox))
        print("第%s题%s"%(num[0],textbox))
        if tkinter.messagebox.askokcancel("提示", "你确定要提交吗？"):
            
            win.destroy()


t = tkinter.Button(win, text="提交", command=close,
                   height="2", width=20, bg="#EEEEE0")
t.pack()


sb = Scrollbar(win)
sb.pack(side=RIGHT, fill=Y)





frame1 = Frame(win, relief=SOLID, height=2000)
frame1.pack(fill=X, ipadx=60, ipady=100, expand=0, side=LEFT)

frame2 = Frame(win, relief=SOLID)
frame2.pack(side=RIGHT, fill=X, ipadx=90, ipady=1000, expand=0)
frame3 = Frame(win, relief=RAISED)
frame3.pack(fill=X, ipadx=20, ipady=1, expand=0)



# next 5 lines are modified


v1 = StringVar(value="1")
v2 = StringVar(value="1")
v3 = StringVar(value="1")


v7 = StringVar(value="1")
v8 = StringVar(value="1")
v9 = StringVar(value="1")
v10 = StringVar(value="1")
v11 = StringVar(value="1")
v12 = StringVar(value="1")
v13 = StringVar(value="1")
v14 = StringVar(value="1")
v15 = StringVar(value="1")
v16 = StringVar(value="1")
v17 = StringVar(value="1")
v18 = StringVar(value="1")
v19 = StringVar(value="1")
v20 = StringVar(value="1")
v21 = StringVar(value="1")


def menu():
    global textbox
    if v.get() == "A":
        textbox = '错误'
    if v.get() == "B":
        textbox = '正确'
    if v.get() == "C":
        textbox = '错误'
    if v.get() == "D":
        textbox = '错误'

def menu2():
    global textbox
    if v.get() == "A":
        textbox = '错误'
    if v.get() == "B":
        textbox = '错误'
    if v.get() == "C":
        textbox = '正确'
    if v.get() == "D":
        textbox = '错误'

lab0 = tkinter.Label(frame1, text='党史知识问答',
                     font=("隶书", 30, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')
lab0.pack()
# 第一题
lab1 = tkinter.Label(frame1, anchor='w', height=2, width=45, text="1.揭开人民解放战争战略进攻序幕的是()",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')

lab1.pack()

lab90 = tkinter.Label(frame1)
v= StringVar()
v.set(' ')
r1 = Radiobutton(lab90, text="A.跃进大别山", value="A",
                 font=("楷书", 11, ), variable=v,command=menu)
r2 = Radiobutton(lab90, text="B.济南战役 ", value="B",
                 font=("楷书", 11, ), variable=v,command=menu)


lab91 = tkinter.Label(frame1, bg="#EEEEE0")
r4 = Radiobutton(lab91, text="C.孟良崮战役", value="C",
                 font=("楷书", 11, ), variable=v,command=menu)
r3 = Radiobutton(lab91, text="D.锦州战役 ", value="D",
                 font=("楷书", 11, ), variable=v,command=menu)
r1.pack(side=LEFT)
r2.pack(side=LEFT)

lab90.pack()
r3.pack(side=RIGHT)
r4.pack(side=RIGHT)
lab91.pack()
v.get()

# 第二题**************************************************

lab2 = tkinter.Label(frame1, anchor='w', height=3, width=45, text="2.（）是在中国举起十月革命旗帜的第一任",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')
lab2.pack()
v1= StringVar()
v1.set(' ')

lab100 = tkinter.Label(frame1, bg="#EEEEE0")
#a1 = Radiobutton(frame1, text="改革开放", value="A", variable=v,height=2, width=45,font=("宋体", 12))
#a2 = Radiobutton(frame1, text="人民民主专政", value="B", variable=v, height=2, width=45, font=("宋体", 12))
a1 = Radiobutton(lab100, text="A.李大钊", value="A", font=("楷书", 11), variable=v1,command=menu1)
a2 = Radiobutton(lab100, text="B.陈独秀", value="B", font=("楷书", 11), variable=v1,command=menu1)
lab100.pack()
lab101 = tkinter.Label(frame1)
a3 = Radiobutton(lab101, text="C.蔡元培", value="C", font=("楷书", 11), variable=v1,command=menu1)
a4 = Radiobutton(lab101, text="D.胡适 ", value="D", font=("楷书", 11), variable=v1,command=menu1)
#a3 = Radiobutton(frame1, text="以经济建设为中心", value="C", variable=v, height=2, width=45, font=("宋体", 12))
#a4 = Radiobutton(frame1, text="以人民为中心", value="D", variable=v, height=2, width=45,font=("宋体", 12))
a1.pack(side=LEFT)
a2.pack(side=LEFT)

a4.pack(side=RIGHT)
a3.pack(side=RIGHT)
lab101.pack()
v1.get()

# 第三题*****************************************************

v2= StringVar()
v2.set(' ')
lab3 = tkinter.Label(frame1, text="3.( )提出了改革开放的任务                      ",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')

lab3.pack()
lab200 = tkinter.Label(frame1, bg="#EEEEE0")

b1 = Radiobutton(lab200, text="A.党的八大", value="A",
                 font=("楷书", 11), variable=v2)
b2 = Radiobutton(lab200, text="B.党的九届二中全会", value="B",
                 font=("楷书", 11), variable=v2)
lab200.pack()

lab201 = tkinter.Label(frame1)
b3 = Radiobutton(lab201, text="C.党的十二大", value="C",
                 font=("楷书", 11), variable=v2)
b4 = Radiobutton(lab201, text="D.党的十一届三中全会", value="D",
                 font=("楷书", 11), variable=v2)
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b4.pack(side=RIGHT)
b3.pack(side=RIGHT)

lab201.pack()
v2.get()
# 第四题*********************************************************


lab4 = tkinter.Label(frame1, text="4.党的十五大提出，依法治国是党领导人民治理国家的。",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')

lab4.pack()

lab200 = tkinter.Label(frame1)
c1 = Radiobutton(lab200, text="A.基本方针", value="A",
                 font=("楷书", 11), variable=v3)
c2 = Radiobutton(lab200, text="B.基本政策", value="B",
                 font=("楷书", 11), variable=v3)
lab200.pack()

lab201 = tkinter.Label(frame1)
c3 = Radiobutton(lab201, text="C.基本方略", value="C",
                 font=("楷书", 11), variable=v3)
c4 = Radiobutton(lab201, text="D.指导思想", value="D",
                 font=("楷书", 11), variable=v3)
c1.pack(side=LEFT)
c2.pack(side=LEFT)

c4.pack(side=RIGHT)
c3.pack(side=RIGHT)
lab201.pack()


# 第五题****************************************

lab5 = tkinter.Label(frame1, text="5.全面建设社会主义时期的重要工程和科技成就有（ ）",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')
lab5.pack()

v7= IntVar(value=0)
lab300 = tkinter.Label(frame1)
check1 = Checkbutton(lab300, text="A.原子弹爆炸成功", height=2,
                     width=45, font=("宋体", 12),variable=v7)
v8 = IntVar(value=0)
check2 = Checkbutton(lab300, text="B.人工合成牛胰岛素结晶成功",
                     height=2, width=45, font=("宋体", 12),variable=v8)
v9 = IntVar(value=0)
lab301 = tkinter.Label(frame1)
check3 = Checkbutton(lab301, text="C.大庆油田建成  ",
                     height=2, width=45, font=("宋体", 12),variable=v9)
v10 = IntVar(value=0)
check4 = Checkbutton(lab301, text="D.葛洲坝水利工程建成      ",
                     height=2, width=45, font=("宋体", 12),variable=v10)

check1.pack(side=LEFT)
check2.pack(side=LEFT)
check4.pack(side=RIGHT)
check3.pack(side=RIGHT)
lab300.pack()
lab301.pack()

# 第六题****************************

lab6 = tkinter.Label(frame2, text="6.1926年7月国民党北伐的主要战场在（）",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')
lab6.pack()
v11 = IntVar(value=0)
lab400 = tkinter.Label(frame2)
check5 = Checkbutton(lab400, text="A.湖南", height=2, width=20, font=("宋体", 10),variable=v11)
v12 = IntVar(value=0)
check6 = Checkbutton(lab400, text="B.湖北", height=2, width=20, font=("宋体", 10),variable=v12)
v13 = IntVar(value=0)
lab401 = tkinter.Label(frame2)
check7 = Checkbutton(lab401, text="C.江西", height=2, width=20, font=("宋体", 10),variable=v13)
v14 = IntVar(value=0)
check8 = Checkbutton(lab401, text="D.浙江", height=2, width=20, font=("宋体", 10),variable=v14)
check5.pack(side=LEFT)
check6.pack(side=LEFT)
check8.pack(side=RIGHT)
check7.pack(side=RIGHT)

lab400.pack()
lab401.pack()


# 第七题**************************************


lab7 = tkinter.Label(frame2, text="7.中共七大总结把党在长期奋斗概括为（）",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')
lab7.pack()
v15 = IntVar(value=0)
lab500 = tkinter.Label(frame2)
check1 = Checkbutton(lab500, text="A.主动联系群众的作风   ", font=("宋体", 12),variable=v15)
v16 = IntVar(value=0)

check2 = Checkbutton(lab500, text="B.理论和实践相结合的作风", font=("宋体", 12),variable=v16)
v17 = IntVar(value=0)
lab501 = tkinter.Label(frame2)
check3 = Checkbutton(lab501, text="C.自我批评的作风     ", font=("宋体", 12),variable=v17)
v18 = IntVar(value=0)
check4 = Checkbutton(lab501, text="D.全心全意为人民服务的作风", font=("宋体", 12),variable=v18)
check1.pack(side=LEFT)
check2.pack(side=LEFT)
check4.pack(side=RIGHT)
check3.pack(side=RIGHT)
lab500.pack()
lab501.pack()

lab8 = tkinter.Label(frame2, text="8.1956年我国的社会主义改造对象是（ ）",
                     font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     activebackground='pink',
                     state='disable')
lab8.pack()
v19 = IntVar(value=0)
lab600 = tkinter.Label(frame2)
check1 = Checkbutton(lab600, text="A.官僚资本主义的社会主义改造", font=("宋体", 10),variable=v19)
v20 = IntVar(value=0)
check2 = Checkbutton(lab600, text="B.个体农业的社会主义改造", font=("宋体", 10),variable=v20)
lab601 = tkinter.Label(frame2)
v21 = IntVar(value=0)
check3 = Checkbutton(lab601, text="C.手工业的社会主义改造", font=("宋体", 10),variable=v21)
v22 = IntVar(value=0)
check4 = Checkbutton(lab601, text="D.资本主义工商业的社会主义改造", font=("宋体", 10),variable=22)
check1.pack(side=LEFT)
check2.pack(side=LEFT)
check4.pack(side=RIGHT)
check3.pack(side=RIGHT)
lab600.pack()
lab601.pack()




lab9 = tkinter.Label(frame2, text="9.新文化运动兴起的发端是什么？", anchor='w', height=2, width=45, font=("楷书", 13, "bold"),
                     activeforeground='green',
                     disabledforeground='black',
                     state='disabled',)
lab9.pack()
text1 = Text(frame2, width=40, height=7, fg="black", font=("楷书", 11, "bold"))
text1.pack()

lab10 = tkinter.Label(frame2, text="10.遵义会议的历史功绩是什么？", anchor='w', height=2, width=45, font=("楷书", 13, "bold"),
                      activeforeground='green',
                      disabledforeground='black',
                      state='disabled')
lab10.pack()
text2 = Text(frame2, width=40, height=7, fg="black", font=("楷书", 11, "bold"))
text2.pack()


t.pack(side=BOTTOM)




win.mainloop()


