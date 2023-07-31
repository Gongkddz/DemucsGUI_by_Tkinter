# -*- coding: UTF-8 -*-
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox


def ButtonCommand():
    var.set("按钮被按下")


def ButtonCommandReset():
    var.set("完成初始化")


def Entry2Label():
    var.set(e.get())
    t.insert('insert', e.get())
    # label.config(text = "")


def b4function():
    var.set(varrb.get())


def scalePrint(default_input):  # 这里是有一个默认的传入值的
    label2string.set("进度条读取值为{}".format(default_input))


def buttoncheckfun():
    opstring = ""
    if checkbuttonValue1.get() == 1:
        opstring = opstring + "1"
    if checkbuttonValue2.get() == 1:
        opstring = opstring + "2"
    if checkbuttonValue3.get() == 1:
        opstring = opstring + "3"
    label2string.set(opstring)


window = tk.Tk()  # 建立窗口
window.title("MyWindow")  # 窗口的名字
window.geometry("400x700")  # 窗口大小，宽x长，字符串

# 创建Label
# Label在window之上，label的文本，背景颜色灰色，字体宋体12号，宽高分别为15字符、2字符
# text = "Label's text" 是静态的，不能更改
var = tk.StringVar()
var.set("Label's text")
l = tk.Label(window, textvariable = var, bg = 'grey', font = ('宋体', 12), width = 15, height = 2)
l.pack()  # 设置好之后放置label

# 设置按钮
b1 = tk.Button(window, text = '按钮', bg = 'grey', font = ('宋体', 10), width = 4, height = 1, command = ButtonCommand)
b2 = tk.Button(window, text = '初始化', bg = 'grey', font = ('宋体', 10), width = 6, height = 1,
               command = ButtonCommandReset)
b1.pack()
b2.pack()

# 设置一个Entry，输入用的文本框
e = tk.Entry(window, show = None, width = 16)
e.pack()

b3 = tk.Button(window, text = 'Entry->Label', bg = 'grey', font = ('宋体', 10), width = 14, height = 1,
               command = Entry2Label)
b3.pack()

t = tk.Text(window, width = 24, height = 6, bg = 'grey')
t.pack()

# RadioButton
varrb = tk.StringVar()
rb1 = tk.Radiobutton(window, text = "选项A，将变量varrb赋值为‘A’", variable = varrb, value = 'A')
rb2 = tk.Radiobutton(window, text = "选项B，将变量varrb赋值为‘B’", variable = varrb, value = 'B')
rb3 = tk.Radiobutton(window, text = "选项C，将变量varrb赋值为‘C’", variable = varrb, value = 'C')
rb1.pack()
rb2.pack()
rb3.pack()
b4 = tk.Button(window, text = "执行选项", command = b4function, width = 10, height = 1)
b4.pack()

# 测试scale，创建一个label来显示
label2string = tk.StringVar()
label2 = tk.Label(window, textvariable = label2string, width = 25, height = 1, font = ('宋体', 12), bg = 'yellow')
label2.pack()

scale = tk.Scale(window, label = '就是拖动的进度条罢了', from_ = 0, to = 100, orient = tk.HORIZONTAL, length = 200,
                 showvalue = False, tickinterval = 20, resolution = 0.1, command = scalePrint)
# command = 这里是有一个默认的传入值的
scale.pack()

# Checkbutton
checkbuttonValue1 = tk.IntVar()
checkbuttonValue2 = tk.IntVar()
checkbuttonValue3 = tk.IntVar()
check1 = tk.Checkbutton(window, text = 'check1', variable = checkbuttonValue1, onvalue = 1, offvalue = 0)
check2 = tk.Checkbutton(window, text = 'check2', variable = checkbuttonValue2, onvalue = 1, offvalue = 0)
check3 = tk.Checkbutton(window, text = 'check3', variable = checkbuttonValue3, onvalue = 1, offvalue = 0)
check1.pack()
check2.pack()
check3.pack()
buttoncheck = tk.Button(window, text = '执行Checkbutton', width = 20, height = 1, command = buttoncheckfun)
buttoncheck.pack()

# 画布Canvas
canvas = tk.Canvas(window, height = 100, width = 100)
im = Image.open('校徽.png')
im = im.resize((100, 80), Image.Resampling.LANCZOS)
image_file = ImageTk.PhotoImage(im)
image = canvas.create_image(0, 0, anchor = 'nw', image = image_file)
canvas.place(x = -10, y = 0, anchor = 'nw')


# 弹出窗口messagebox
def msgbox():
    # messagebox.showinfo(title = 'showinfo',message = '⚪!展示信息弹窗')
    # messagebox.showwarning(title = 'showwarning', message = '🔺!展示信息弹窗')
    # messagebox.showerror(title = 'showerror', message = '⚪×展示信息弹窗')
    # ret = messagebox.askquestion(title = 'showerror', message = '⚪×展示信息弹窗')   # return 'yes', 'no'
    # ret = messagebox.askyesno(title = 'showerror', message = '⚪×展示信息弹窗')  # return True, False
    label2string.set(ret)

tk.Button(window, height = 1, width = 5, text = "弹窗", command = msgbox).pack()

window.mainloop()  # 设置窗口循环



from tkinter import filedialog
filenames = filedialog.askopenfilenames()   # 询问打开多个文件，返回文件地址列表
filename = filedialog.askopenfilename()   # 询问打开单个文件，返回文件地址字符串
path = filedialog.askdirectory()    # 询问文件夹地址，返回文件夹地址字符串