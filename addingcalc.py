



from tkinter import *
root = Tk()

def call_result(label_result, n1, n2):
     result = float(n1) + float(n2)
     print(result)
     label_result.configure(text= result)
root.title("calculator")

number1 = StringVar()
number2 = StringVar()

LabelNum1 = Label(root, text="First number").grid(column=0, row=1)
LabelNum2 = Label(root, text="Second number").grid(column=0, row=2)

labelResult = Label(root,bg="gold")
labelResult.grid(column=2, row=7)

ent1=Entry(root,textvariable=number1)
ent1.grid(column=2, row=1)
ent2=Entry(root,textvariable=number2)
ent2.grid(column=2, row=2)
buttoncall = Button(root, text="calculate", \
  command=lambda: call_result(labelResult, number1.get(), number2.get())).grid(column=0, row=3)
buttoncall2 = Button(root, text="Quit", command=quit).grid(column=0, row=4)
  

root.mainloop()
