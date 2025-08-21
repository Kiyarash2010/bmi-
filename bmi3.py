from tkinter import*
from tkinter import messagebox
tk=Tk()
tk.title('bmi')
a=Label(tk,text='height(m)',font=('Arial Black',10))
a.pack()
d=Entry(tk,font=('Arial Black',10))
d.pack()
s=Label(tk,text='weight(kg)',font=('Arial Black',10))
s.pack()
f=Entry(tk,font=('Arial Black',10))
f.pack()
def bmi():
    g=(d.get())
    e=(f.get())
    if not g or not e:
        messagebox.showerror('هشدار','عددي وارد نشده')
        return
    try:
        g=float(g)
        e=float(e)
    except:
        messagebox.showerror('هشدار','لطفا عدد وارد کنيد ')
        return
    if g<=0 or e<=0:
        messagebox.showerror('هشدار','قد و وزن بايد بزرگتر از صفر باشد')
        return
        
        
    BMI=e/g**2
    m.config(text=BMI)
    if BMI<18.5:
        t.config(text='کمبودوزن',fg='red')
    elif 25>BMI>=18.5:
        t.config(text='طبيعي',fg='green')
    elif 30>BMI>=25:
        t.config(text='وزن زياد',fg='orange')
    elif BMI>30:
        t.config(text='چاقي مفرط',fg='crimson')
    d.delete(0,END)
    f.delete(0,END)
def clear():
    d.delete(0,END)
    f.delete(0,END)
    m.config(text='')
    t.config(text='')
y=Button(tk,text="clear",command=clear,bg='blue')
y.pack()
b=Button(tk,text='ok',command=bmi)
b.pack()
m=Label(tk,text='',font=('Arial Black',10))
m.pack()
t=Label(tk,text='',font=('Arial Black',10))
t.pack()
