from tkinter import *
from math import *
from tkinter.messagebox import *
root=Tk()
root.title("Scientific calculator")
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("480x568+0+0")
calc=Frame(root)
calc.grid()
class Calc:
    def __init__(self):
        self.total=0
        self.current=""
        self.input=True
        self.check_sum=False
        self.op=""
        self.result=False
    def numberEnter(self,num):
        self.result=False
        firstnum=txtdisplay.get()
        secondnum=str(num)
        if self.input:
            self.current=secondnum
            self.input=False
        else:
            if secondnum=='.':
                return
            self.current=firstnum+secondnum
        self.display(self.current)
    def sum_of_total(self):
        self.result=True
        self.current=float(self.current)
        if self.check_sum==True:
            self.valid_function()
        else:
            self.total=float(txtdisplay.get())
    def display(self,value):
        txtdisplay.delete(0,END)
        txtdisplay.insert(0,value)
    def valid_function(self):
        if self.op=="add":
            self.total+=self.current
        if self.op=="sub":
            self.total-=self.current
        if self.op=="mult":
            self.total*=self.current
        if self.op=="divide":
            self.total/=self.current
        if self.op=="mod":
            self.total%=self.current
        self.input=True
        self.check_sum=False
        self.display(self.total)
    def operation(self,op):
        self.current=float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total=self.current
            self.input=True
        self.check_sum=True
        self.op=op
        self.result=False
    def pi(self):
        self.result=False
        self.current=pi
        self.display(self.current)
    def tau(self):
        self.result=False
        self.current=tau
        self.display(self.current)
    def e(self):
        self.result=False
        self.current=e
        self.display(self.current)
    def log(self):
        self.result=False
        self.current=log(float(txtdisplay.get()))
        self.display(self.current)
    def sin(self):
        self.result=False
        self.current=sin(radians(float(txtdisplay.get())))
        self.display(self.current)
    def sinh(self):
        self.result=False
        self.current=sinh(radians(float(txtdisplay.get())))
        self.display(self.current)
    def asinh(self):
        self.result=False
        self.current=asinh(radians(float(txtdisplay.get())))
        self.display(self.current)
    def cos(self):
        self.result=False
        self.current=cos(radians(float(txtdisplay.get())))
        self.display(self.current)
    def cosh(self):
        self.result=False
        self.current=cosh(radians(float(txtdisplay.get())))
        self.display(self.current)
    def acosh(self):
        self.result=False
        self.current=acosh(radians(float(txtdisplay.get())))
        self.display(self.current)
    def tan(self):
        self.result=False
        self.current=tan(radians(float(txtdisplay.get())))
        self.display(self.current)
    def tanh(self):
        self.result=False
        self.current=tanh(radians(float(txtdisplay.get())))
        self.display(self.current)
    def expo(self):
        self.result=False
        self.current=exp(float(txtdisplay.get()))
        self.display(self.current)
    def mod(self):
        self.result=False
        self.current=modf(float(txtdisplay.get()))
        self.display(self.current)
    def expm(self):
        self.result=False
        self.current=expm1(float(txtdisplay.get()))
        self.display(self.current)
    def gamma(self):
        self.result=False
        self.current=lgamma(float(txtdisplay.get()))
        self.display(self.current)
    def clear(self):
        self.result=False
        self.current="0"
        self.display(0)
        self.input=True
    def clearall(self):
        self.clear()
        self.total=0
    def squareroot(self):
        self.result=False
        self.current=sqrt(float(txtdisplay.get()))
        self.display(self.current)
    def deg(self):
        self.result=False
        self.current=degrees(float(txtdisplay.get()))
        self.display(self.current)
    def percent(self):
        self.result=False
        self.current=(float(txtdisplay.get()))/100
        self.display(self.current)
added_value=Calc()
txtdisplay=Entry(calc,font=('ariel',20,'bold'),bg="powder blue",bd=30,width=29,justify=RIGHT)
txtdisplay.grid(row=0,column=0, columnspan=4,pady=1)
txtdisplay.insert(0,"0")
numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('ariel',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
        i+=1
#____________________________________________________________________________________________________________________________________________________
btnclr=Button(calc,text=chr(67),width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.clear).grid(row=1,column=0,pady=1)
btnclrall=Button(calc,text=chr(67)+chr(69),width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.clearall).grid(row=1,column=1,pady=1)
btnsq=Button(calc,text="sqrt",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.squareroot).grid(row=1,column=2,pady=1)
btnadd=Button(calc,text="+",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.operation("add")).grid(row=1,column=3,pady=1)
btnsub=Button(calc,text="-",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.operation("sub")).grid(row=2,column=3,pady=1)
btnmult=Button(calc,text="x",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.operation("mult")).grid(row=3,column=3,pady=1)
btndiv=Button(calc,text="/",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.operation("divide")).grid(row=4,column=3,pady=1)
btzero=Button(calc,text="0",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter(0)).grid(row=5,column=0,pady=1)
btndot=Button(calc,text=".",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=lambda:added_value.numberEnter(".")).grid(row=5,column=1,pady=1)
btnpercent=Button(calc,text="%",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.percent).grid(row=5,column=2,pady=1)
btnequals=Button(calc,text="=",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.sum_of_total).grid(row=5,column=3,pady=1)
#_____________________________________________________________________________________________________________________________________
btzpi=Button(calc,text="pi",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.pi).grid(row=1,column=4,pady=1)
btncos=Button(calc,text="cos",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.cos).grid(row=1,column=5,pady=1)
btntan=Button(calc,text="tan",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.tan).grid(row=1,column=6,pady=1)
btnsin=Button(calc,text="sin",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.sin).grid(row=1,column=7,pady=1)
btz2pi=Button(calc,text="2pi",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.tau).grid(row=2,column=4,pady=1)
btncosh=Button(calc,text="cosh",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.cosh).grid(row=2,column=5,pady=1)
btntanh=Button(calc,text="tanh",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.tanh).grid(row=2,column=6,pady=1)
btnsinh=Button(calc,text="sinh",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.sinh).grid(row=2,column=7,pady=1)
btzlog=Button(calc,text="log",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.log).grid(row=3,column=4,pady=1)
btnexp=Button(calc,text="Exp",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.expo).grid(row=3,column=5,pady=1)
btnmod=Button(calc,text="Mod",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.mod).grid(row=3,column=6,pady=1)
btnE=Button(calc,text="e",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.e).grid(row=3,column=7,pady=1)
btzlog2=Button(calc,text="log2",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue").grid(row=4,column=4,pady=1)
btndeg=Button(calc,text="deg",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.deg).grid(row=4,column=5,pady=1)
btnacosh=Button(calc,text="acosh",width=6,height=2,font=('ariel',20,'bold'),bd=4,command=added_value.acosh).grid(row=4,column=6,pady=1)
btnasinh=Button(calc,text="asinh",width=6,height=2,font=('ariel',20,'bold'),command=added_value.asinh,bd=4).grid(row=4,column=7,pady=1)
btzlog10=Button(calc,text="log10",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue").grid(row=5,column=4,pady=1)
btnCos=Button(calc,text="log1p",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue").grid(row=5,column=5,pady=1)
btnexpm1=Button(calc,text="expm1",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue",command=added_value.expm).grid(row=5,column=6,pady=1)
btnlgamma=Button(calc,text="gamma",width=6,height=2,font=('ariel',20,'bold'),bd=4,bg="powder blue").grid(row=5,column=7,pady=1)
lbldisplay=Label(calc,text="Scientific Calculator",font=('ariel',30,'bold'),justify=CENTER)
lbldisplay.grid(row=0,column=4,columnspan=4)
#_____________________________________________________________________________________________________________________________________________________
def iExit():
    iexit=askyesno("Scientific Calculator","confirm if you want to Exit")
    if iexit >0:
        root.destroy()
        return
def scientific():
    root.resizable(width=False,height=False)
    root.geometry("950x568+0+0")
def standard():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")
menubar=Menu(calc)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Standard",command=standard)
filemenu.add_command(label="Scientific",command=scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)
editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="cut")
editmenu.add_command(label="copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")
root.config(menu=menubar)
root.mainloop()