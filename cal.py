from tkinter import *
w=Tk()
w.title('Simple Calculator') #adding title to window #w.iconbitmap('cal.ico')#adding icon to window 
#global variables 

 
def numclear(): 
    e.delete(0,END)
    
def click(num):
    n1=e.get()
    numclear() 
    n2=n1+num
    e.insert(0,n2)
    
def calculate(op): 
    global operator
    operator=op
    global num1
    num1=e.get()
    numclear()
    
def equals(): 
   # global numl,operator 
    result=0
    num2=e.get()
    numclear() 
    if operator=='+': 
        result=int(num1)+int(num2) 
    elif operator=='-': 
        result=int(num1)-int(num2) 
    elif operator=='*':
        result=int(num1)*int(num2)
    elif operator=='/': 
        result=int(num1)/int(num2) 
    elif operator=='%': 
        result=int(num1)%int(num2) 
    e.insert(0,result) 

#Creating Widgets 
e=Entry(w,width=15,font=('TimesNewRoman',25),justify=RIGHT)#Default justification isLEFT 
b0=Button(w,text='0',padx=30,pady=10, font=('Arial', 15), command=lambda:click('0')) 
bl=Button(w,text='1',padx=30,pady=10, font=('Arial', 15),command=lambda:click('1')) 
b2=Button(w,text='2',padx=30,pady=10, font=('Arial', 15), command=lambda:click('2'))
b3=Button(w,text='3',padx=30,pady=10, font=('Arial', 15), command=lambda:click('3'))
b4=Button(w,text='4',padx=30,pady=10, font=('Arial', 15), command=lambda:click('4')) 
b5=Button(w,text='5',padx=30,pady=10, font=('Arial', 15), command=lambda:click('5'))
b6=Button(w,text='6',padx=30,pady=10, font=('Arial', 15), command=lambda:click('6'))
b7=Button(w,text='7',padx=30,pady=10, font=('Arial',15), command=lambda:click('7'))
b8=Button(w,text='8',padx=30,pady=10, font=('Arial',15), command=lambda:click('8'))
b9=Button(w,text='9',padx=30,pady=10,font=('Arial', 15),command=lambda:click('9'))
add=Button(w,text='+',padx=30,pady=10, font=('Arial"',15), command=lambda:calculate('+'))
sub=Button(w,text='-',padx=32,pady=10,font=('Arial',15),command=lambda:calculate('-'))
mul=Button(w,text='*',padx=32,pady=10, font=('Arial', 15), command=lambda:calculate('*'))
div=Button(w,text='/',padx=32,pady=10, font=('Arial', 15),command=lambda:calculate('/'))
mod=Button(w,text='%',padx=27,pady=10, font=('Arial', 15),command=lambda:calculate('%'))
clear=Button(w,text='C',padx=30,pady=10, font=('Arial', 15),command=numclear)
eq=Button(w,text='=',padx=75,pady=10, font=('Arial', 15),command=equals) 

#adding widgets to the interface.
#Row-0 
e.grid(row=0,column=0,columnspan=3,padx=1,pady=1) 
#Row-1 
b7.grid(row=1,column=0,padx=1,pady=1) 
b8.grid(row=1,column=1,padx=1,pady=1) 
b9.grid(row=1,column=2,padx=1,pady=1) 
#Row-2 
b4.grid(row=2,column=0,padx=1,pady=1) 
b5.grid(row=2,column=1,padx=1,pady=1) 
b6.grid(row=2,column=2,padx=1,pady=1) 
#Row-3 
bl.grid(row=3,column=0,padx=1,pady=1) 
b2.grid(row=3,column=1,padx=1,pady=1) 
b3.grid(row=3,column=2,padx=1,pady=1) 
#Row-4 
add.grid(row=4, column=0,padx=1,pady=1) 
b0.grid(row=4,column=1,padx=1,pady=1)
sub.grid(row=4,column=2,padx=1,pady=1) 
#Row-5 
mul.grid(row=5,column=0,padx=1,pady=1) 
div.grid(row=5,column=1,padx=1,pady=1) 
mod.grid(row=5,column=2,padx=1,pady=1) 
#Row-6 
clear.grid(row=6,column=0,padx=1,pady=1) 
eq.grid(row=6,column=1,columnspan=2,padx=1,pady=1) 

#Executable loop on the application, waits for user input
w.mainloop() 
