import tkinter as tk
import random

#Логика калькулятора.
def FuncFact(fact):
    fact = int(fact)
    if (fact < 2):
        return 1
    return fact*FuncFact(fact-1)
def OperationCalculate():
    value = Row.get() #eval(). Мат операция в виде строки.
    for i in range(len(value)):
        if value[i].isalpha():
            Row.delete(0, tk.END)
            Row.insert(0, "ERR")
            return
    if value[-1] in "+-/":
        Row.delete(0,tk.END)
        Row.insert(0,"0")
        return
    if value[-1] == "*":
        Row.delete(0,tk.END)
        Row.insert(0,str(int(value[:-1])*int(value[:-1])))
        return
    if value[-1] != "!":
        Row.delete(0, tk.END)
        Row.insert(0, eval(value))
    else:
        value = value[:-1]
        Row.delete(0,tk.END)
        Row.insert(0,str(FuncFact(value)))

#Обработка кнопок
def AddNumber(number):
    value = Row.get()
    if value[0] == "0":
        value = value[1:]
    Row.delete(0, tk.END)
    Row.insert(0, value + number)

def AddOperation(Operation):
    value = Row.get()
    if value[-1] in "+-/*":
        value = value[:-1]
    Row.delete(0, tk.END)
    Row.insert(0, value+Operation)

def Result(ravno):
    return tk.Button(text=ravno,bd=2, fg="Black",bg="White",activebackground="Gray",font=("Times New Roman",15),command= lambda: OperationCalculate())
def Operation(Operation):
    return tk.Button(text=Operation,bd=2,fg="Black",bg="White",activebackground="Gray",font=("Times New Roman",15),command=lambda: AddOperation(Operation))
def DelAll():
    Row.delete(0, "end")
    Row.insert(0,"0")
def ButtonDelAll(OperationC):
    return tk.Button(text=OperationC,fg="Red", bg="White",bd=2, activebackground="Gray", font=("Times New Roman", 15), command=lambda: DelAll())
def DeleteLast():
    line = Row.get()
    if len(line) == 1:
        Row.delete(0,tk.END)
        Row.insert(0,"0")
    else:
        Row.delete(Row.index(len(Row.get()))-1)
def ButtonDelLast(DelLast):
    return tk.Button(text=DelLast, bd=2, fg="Black", bg="White", activebackground="Gray", font=("Times New Roman", 15), command=lambda: DeleteLast())

#Создание окна, размеры, иконка
window = tk.Tk()
window.title("Калькулятор")
window.geometry("310x400+600+200")
window.resizable(False, False)
#window.iconphoto(False, tk.PhotoImage(file=r"C:\Users\Александр\Desktop\ПРОЕКТ калькулятор\2819726.png")) #Изменено 02.03.2023.
window.config(bg="White")

#Создание панели ввода
Row = tk.Entry(window,bd=2,bg="White",fg="Black",justify=tk.RIGHT,font=("Times New Roman", 14))
Row.insert(0,"0")
Row.grid(row=0, column=0,columnspan=6, stick="snwe")

#Кнопки, расположение
tk.Button(text="1",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("1")).grid(row=1, column=0, stick="nswe", padx=5, pady=5)
tk.Button(text="2",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("2")).grid(row=1, column=1, stick="nswe", padx=5, pady=5)
tk.Button(text="3",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("3")).grid(row=1, column=2, stick="nswe", padx=5, pady=5)
tk.Button(text="4",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("4")).grid(row=2, column=0, stick="nswe", padx=5, pady=5)
tk.Button(text="5",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("5")).grid(row=2, column=1, stick="nswe", padx=5, pady=5)
tk.Button(text="6",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("6")).grid(row=2, column=2, stick="nswe", padx=5, pady=5)
tk.Button(text="7",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("7")).grid(row=3, column=0, stick="nswe", padx=5, pady=5)
tk.Button(text="8",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("8")).grid(row=3, column=1, stick="nswe", padx=5, pady=5)
tk.Button(text="9",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("9")).grid(row=3, column=2, stick="nswe", padx=5, pady=5)
tk.Button(text="0",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber("0")).grid(row=4, column=1, stick="nswe", padx=5, pady=5)
tk.Button(text=".",bg="White",fg="Black",activebackground="Gray", font=("Times New Roman",15), command = lambda: AddNumber(".")).grid(row=4,column=0,stick="nswe",padx=5,pady=5)
#Размер клеток)

for i in range(1,5):
    window.grid_rowconfigure(i, minsize=60)
    window.grid_columnconfigure(i, minsize=60)

window.grid_rowconfigure(0, minsize=40)
window.grid_columnconfigure(0, minsize=60)
window.grid_rowconfigure(5 ,minsize=60)

#Операции
Operation("+").grid(row=1, column=3, stick="nswe", padx=5, pady=5)
Operation("-").grid(row=2, column=3, stick="nswe", padx=5, pady=5)
Operation("*").grid(row=3, column=3, stick="nswe", padx=5, pady=5)
Operation("/").grid(row=4, column=3, stick="nswe", padx=5, pady=5)
Operation("!").grid(row=4,column=2,stick="nswe",padx=5,pady=5)
ButtonDelAll("C").grid(row=1, column=4, stick="nwse",padx=5, pady=5)
ButtonDelLast("<=").grid(row=2, column=4, stick="nswe",padx=5, pady=5)
Result("=").grid(row=3, column=4, stick="nwse", rowspan=2, columnspan=3, padx=5, pady=5)

#Random число
def AddOne():
    row = StrA.get()
    for i in range(len(row)):
        if row[i].isalpha():
            StrA.delete(0,tk.END)
            StrA.insert(0,"ERROR")
            return
    value = int(row)
    value = value+1
    StrA.delete(0,tk.END)
    StrA.insert(0,str(value))
def MinusOne():
    row = StrA.get()
    for i in range(len(row)):
        if row[i].isalpha():
            StrA.delete(0, tk.END)
            StrA.insert(0, "ERR")
            return
    value = int(row)
    if value <=1:
        StrA.delete(0,tk.END)
        StrA.insert(0,"1")
    else:
        value = value - 1
        StrA.delete(0, tk.END)
        StrA.insert(0, str(value))
def Clean():
    StrA.delete(0,tk.END)
    StrA.insert(0,"1")

def Random():
    row = StrA.get()
    for i in range(len(row)):
        if row[i].isalpha():
            StrA.delete(0, tk.END)
            StrA.insert(0, "ERR")
            return
    if int(StrA.get()) < 1:
        StrA.delete(0, tk.END)
        StrA.insert(0, "1")
        return
    Begin = Row.get()
    if Begin[0] == "0":
        Begin=Begin[1:]
    Row.delete(0, tk.END)
    REZ = ""
    count = int(StrA.get())
    for i in range(count):
        REZ += str(random.randint(0,9))
    if REZ[0] == "0":
        REZ.replace("0","1",1)
    Row.insert(0, Begin+str(REZ))

tk.Label(window,text="Случайное\nчисло",font=("Times New Roman",8),bg="White").grid(row=5,column=0)
tk.Label(window,bg="White",text="Нажмите +1 или -1 для изменения количества\nразрядов. Clear,чтобы очистить поле разрядов\n, нажмите Gen!,чтобы вывести полученное число\n(Только целые числа)",font=("Times New Roman",8)).grid(row=5,column=1,columnspan=4,stick="nwse")
StrA = tk.Entry(bd=1,bg="White",fg="Black",justify=tk.RIGHT,width=5,font=("Times New Roman",14))
StrA.insert(0, "1")
StrA.grid(row=7,column=0)
window.grid_rowconfigure(5,minsize=30)
window.grid_rowconfigure(6,minsize=10)
tk.Button(text="+1",activebackground="Gray",bg="White", font=("Times New Roman",15),command=lambda: AddOne()).grid(row=7,column=1,stick="we",padx=5,pady=5)
tk.Button(text="-1",activebackground="Gray",bg="White", font=("Times New Roman",15),command=lambda: MinusOne()).grid(row=7,column=2,stick="we",padx=5,pady=5)
tk.Button(text="Clear",activebackground="Gray",bg="White", font=("Times New Roman",12),command=lambda: Clean()).grid(row=7,column=3,stick="we",padx=5,pady=5)
tk.Button(text="Gen!",activebackground="Gray",bg="White", font=("Times New Roman",12),command=lambda: Random()).grid(row=7,column=4,stick="we",padx=5,pady=5)


window.mainloop() #Вывод окна
exit()
