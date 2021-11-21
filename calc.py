from tkinter import *
from tkinter.messagebox import *
from math import *
class Scien_calc:
    equation=""
    def iexit(self):
        c=askyesno("Calculator","Are you sure you want to exit")
        if c>0:
            self.root.destroy()
    def scientific(self):
        self.root.resizable(width=False, height=False)
        self.root.geometry("950x596")
    def pressnum(self,value):
        self.equation=self.equation+str(value)
        self.textentry.set(self.equation)
    def pressequals(self):
        self.total = str(eval(self.equation))
        self.textentry.set(self.total)
        self.equation=self.total
    def clear(self):
        self.textentry.set("")
        self.equation=""
    def clr(self):
        self.equation=self.equation[:-1]
        self.textentry.set(self.equation)
    def percent(self):
        self.equation=str(int(self.equation)/100)
        self.textentry.set(self.equation)

    def standard(self):
        self.root.resizable(width=False,height=False)
        self.root.geometry("470x596")
    def problem(self,x):
        self.equation=x
        self.textentry.set(self.equation)

    def __init__(self):
        self.root=Tk()
        self.root.resizable(width=False,height=False)
        self.root.geometry("470x596")
        self.root.configure(bg='grey')
        self.p1=PanedWindow(self.root,bg='grey')
        self.p2=PanedWindow(self.root)
        self.textentry=StringVar()
        self.btclear=Button(self.p2,text="C",font=('ariel',20,'bold'),bd=4,bg="orange",fg="white",height=2,width=6,command=self.clr).grid(row=4,column=0)
        self.btallclear=Button(self.p2,text="CE",font=('ariel',20,'bold'),bd=4,bg="orange",fg="white",height=2,width=6,command=self.clear).grid(row=4,column=1)
        self.btpercent=Button(self.p2,text="%",font=('ariel',20,'bold'),bd=4,bg="orange",fg="white",height=2,width=6,command=self.percent).grid(row=4,column=2)
        self.btsquareroot=Button(self.p2,text="sqrt",font=('ariel',20,'bold'),bd=4,bg="orange",fg="white",height=2,width=6,command=lambda:self.problem(str(sqrt(float(self.equation))))).grid(row=4,column=3)
        self.bt1=Button(self.p1,text="Scientific",font=('ariel',20,'bold'),bd=4,bg='orange',fg='white',height=1,width=14,command=self.scientific).grid(row=0,column=0)
        self.bt3=Button(self.p1,text="Standard",font=('ariel',20,'bold'),bd=4,bg='orange',fg='white',height=1,width=14,command=self.standard).grid(row=0,column=2)
        self.bt2=Button(self.p1,text='Exit',font=('ariel',20,'bold'),bg='grey',fg='white',bd=4,height=1,width=12,command=self.iexit).grid(row=0,column=1)
        self.txt1=Entry(self.p1,font=('ariel',20,'bold'),width=45,background="white",bd=20,textvariable=self.textentry)
        self.txt1.grid(row=1,column=0,columnspan=4)

        self.btn1=Button(self.p2,font=('ariel',20,'bold'),text="1",bd=4,width=6,height=2,command=lambda :self.pressnum(1)).grid(row=0,column=0)
        self.btn2=Button(self.p2,font=('ariel',20,'bold'),text="2",bd=4,width=6,height=2,command=lambda : self.pressnum(2)).grid(row=0,column=1)
        self.btn3=Button(self.p2,font=('ariel',20,'bold'),text="3",bd=4,width=6,height=2,command=lambda : self.pressnum(3)).grid(row=0,column=2)
        self.btn4=Button(self.p2,font=('ariel',20,'bold'),text="4",bd=4,width=6,height=2,command=lambda : self.pressnum(4)).grid(row=1,column=0)
        self.btn5=Button(self.p2,font=('ariel',20,'bold'),text="5",bd=4,width=6,height=2,command=lambda : self.pressnum(5)).grid(row=1,column=1)
        self.btn6=Button(self.p2,font=('ariel',20,'bold'),text="6",bd=4,width=6,height=2,command=lambda : self.pressnum(6)).grid(row=1,column=2)
        self.btn7=Button(self.p2,font=('ariel',20,'bold'),text="7",bd=4,width=6,height=2,command=lambda :self.pressnum(7)).grid(row=2,column=0)
        self.btn8=Button(self.p2,font=('ariel',20,'bold'),text="8",bd=4,width=6,height=2,command=lambda : self.pressnum(8)).grid(row=2,column=1)
        self.btn9=Button(self.p2,font=('ariel',20,'bold'),text="9",bd=4,width=6,height=2,command=lambda:self.pressnum(9)).grid(row=2,column=2)
        self.btn0=Button(self.p2,font=('ariel',20,'bold'),text="0",bd=4,width=6,height=2,command=lambda:self.pressnum(0)).grid(row=3,column=1)
        self.btnadd=Button(self.p2,font=('ariel',20,'bold'),text="+",bd=4,bg='orange',width=6,height=2,command=lambda:self.pressnum('+')).grid(row=0,column=3)
        self.btnsub=Button(self.p2,font=('ariel',20,'bold'),text="-",bd=4,width=6,bg='orange',height=2,command=lambda:self.pressnum('-')).grid(row=1,column=3)
        self.btnmult=Button(self.p2,font=('ariel',20,'bold'),text="*",bd=4,width=6,height=2,bg='orange',command=lambda:self.pressnum('*')).grid(row=2,column=3)
        self.btndiv=Button(self.p2,font=('ariel',20,'bold'),text="/",bd=4,width=6,height=2,bg='orange',command=lambda:self.pressnum('/')).grid(row=3,column=3)
        self.btndot=Button(self.p2,font=('ariel',20,'bold'),text=".",bd=4,width=6,height=2,command=lambda:self.pressnum('.')).grid(row=3,column=0)
        self.btnequals=Button(self.p2,font=('ariel',20,'bold'),text="=",bd=4,width=6,height=2,bg='grey',fg='white',command=lambda:self.pressequals()).grid(row=3,column=2)
        self.opbr=Button(self.p2,font=('ariel',20,'bold'),text="(",bd=4,width=6,height=2,bg='grey',fg='white',command=lambda:self.pressnum('(')).grid(row=0,column=4)
        self.clbr=Button(self.p2,font=('ariel',20,'bold'),text=")",bd=4,width=6,height=2,bg='grey',fg='white',command=lambda:self.pressnum(')')).grid(row=0,column=5)
        self.power=Button(self.p2,font=('ariel',20,'bold'),text="^",bd=4,width=6,height=2,bg='orange',fg='white',command=lambda:self.pressnum('**')).grid(row=0,column=7)
        self.btnpi=Button(self.p2,font=('ariel',20,'bold'),text="pi",bd=4,width=6,height=2,command=lambda:self.pressnum(pi)).grid(row=0,column=6)
        self.btn2pi=Button(self.p2,font=('ariel',20,'bold'),text="2pi",bd=4,width=6,height=2,command=lambda:self.pressnum(tau)).grid(row=1,column=6)
        self.btnE=Button(self.p2,font=('ariel',20,'bold'),text="e",bg='orange',fg='white',bd=4,width=6,height=2,command=lambda:self.pressnum(e)).grid(row=4,column=4)
        self.btnfact=Button(self.p2,font=('ariel',20,'bold'),text="x!",bd=4,width=6,height=2,command=lambda:self.problem(str(factorial(float(self.equation))))).grid(row=2,column=6)
        self.btnsin=Button(self.p2,font=('ariel',20,'bold'),text="sin",bd=4,width=6,bg='orange',height=2,command=lambda:self.problem(str(sin(radians(float(self.equation)))))).grid(row=1,column=7)
        self.btncos=Button(self.p2,font=('ariel',20,'bold'),text="cos",bd=4,width=6,height=2,bg='orange',command=lambda:self.problem(str(cos(radians(float(self.equation)))))).grid(row=2,column=7)
        self.btntan=Button(self.p2,font=('ariel',20,'bold'),text="tan",bd=4,width=6,height=2,bg='orange',command=lambda:self.problem(str(tan(radians(float(self.equation)))))).grid(row=3,column=7)
        self.btnasinh=Button(self.p2,font=('ariel',20,'bold'),text="asinh",bd=4,width=6,height=2,bg='orange',fg='white',command=lambda:self.problem(str(asinh(radians(float(self.equation)))))).grid(row=4,column=5)
        self.btnacosh=Button(self.p2,font=('ariel',20,'bold'),text="acosh",bd=4,width=6,height=2,bg='orange',fg='white',command=lambda:self.problem(str(acosh(radians(float(self.equation)))))).grid(row=4,column=6)
        self.btnatanh=Button(self.p2,font=('ariel',20,'bold'),text="atanh",bd=4,width=6,height=2,bg='orange',fg='white',command=lambda:self.problem(str(atanh(radians(float(self.equation)))))).grid(row=4,column=7)
        self.btnsinh=Button(self.p2,font=('ariel',20,'bold'),text="sinh",bd=4,width=6,height=2,command=lambda:self.problem(str(sinh(radians(float(self.equation)))))).grid(row=1,column=5)
        self.btncosh=Button(self.p2,font=('ariel',20,'bold'),text="cosh",bd=4,width=6,height=2,command=lambda:self.problem(str(cosh(radians(float(self.equation)))))).grid(row=2,column=5)
        self.btntanh=Button(self.p2,font=('ariel',20,'bold'),text="tanh",bd=4,width=6,height=2,command=lambda:self.problem(str(tanh(radians(float(self.equation)))))).grid(row=3,column=5)
        self.btnisin=Button(self.p2,font=('ariel',20,'bold'),text="sin inv",bd=4,width=6,height=2,command=lambda:self.problem(str(asin(float(self.equation))))).grid(row=1,column=4)
        self.btnicos=Button(self.p2,font=('ariel',20,'bold'),text="cos inv",bd=4,width=6,height=2,command=lambda:self.problem(str(acos(float(self.equation))))).grid(row=2,column=4)
        self.btnitan=Button(self.p2,font=('ariel',20,'bold'),text="tan inv",bd=4,width=6,height=2,command=lambda:self.problem(str(atan(float(self.equation))))).grid(row=3,column=4)
        self.btnlog=Button(self.p2,font=('ariel',20,'bold'),text="log",bd=4,width=6,height=2,command=lambda:self.problem(str(log(float(self.equation))))).grid(row=3,column=6)
        self.p1.pack()
        self.p2.pack()
        self.root.mainloop()
obj=Scien_calc()