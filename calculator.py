from tkinter import*
import pyttsx3 as pt
def btnclick(numbers):
    global operator
    operator=operator+ str(numbers)
    input_text.set(operator)

def btncleardisplay():
    global operator
    operator=""
    input_text.set("")
def btnequaldisplay():
    global operator
    sumup=str(eval(operator))
    input_text.set(sumup)
    pt.speak("The result is"+sumup)
    operator=""

cal=Tk()
cal.title("Basic calculator-----Developed By Mir_Monajir")
operator=""
input_text=StringVar()
txtDisplay=Entry(cal, font=('verdana', 20, 'bold'), textvariable=input_text, bd=30, insertwidth=5, bg="powder blue", justify='right').grid(columnspan=4)
btn1=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="1", command=lambda:btnclick(1)).grid(row=1,column=0)
btn2=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="2", command=lambda:btnclick(2)).grid(row=1,column=1)
btn3=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="3", command=lambda:btnclick(3)).grid(row=1,column=2)
btn4=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="4", command=lambda:btnclick(4)).grid(row=2,column=0)
btn5=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="5", command=lambda:btnclick(5)).grid(row=2,column=1)
btn6=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="6", command=lambda:btnclick(6)).grid(row=2,column=2)
btn7=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="7", command=lambda:btnclick(7)).grid(row=3,column=0)
btn8=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="8", command=lambda:btnclick(8)).grid(row=3,column=1)
btn9=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="9", command=lambda:btnclick(9)).grid(row=3,column=2)
btn0=Button(cal, padx=15,pady=16, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="0", command=lambda:btnclick(0)).grid(row=4,column=0)
btn_add=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="+", command=lambda:btnclick("+")).grid(row=1,column=3)
btn_sub=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="-", command=lambda:btnclick("-")).grid(row=2,column=3)
btn_mul=Button(cal, padx=15, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="*", command=lambda:btnclick("*")).grid(row=3,column=3)
btn_div=Button(cal, padx=15,pady=16, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="/", command=lambda:btnclick("/")).grid(row=4,column=3)
btn_clr=Button(cal, padx=15,pady=16, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="Clr", command=btncleardisplay).grid(row=4,column=1)
btn_equal=Button(cal, padx=15,pady=16, font=('verdana', 20, 'bold'), fg='black', bd=7, bg="powder blue", text="=", command=btnequaldisplay).grid(row=4,column=2)
cal.mainloop()