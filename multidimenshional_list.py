from tkinter import *

root = Tk()

root.title("Report Card Generator")
root.geometry('500x500')
label = Label(root)


array_1d = ["Sapnap","Dream","Tommy Innit","Technoblade","PraysNL"]
print(array_1d[0])

array_2d = [["Sapnap","C-"],["Dream","A+"],["Tommy Innit","B"],["Technoblade","A+"],["PraysNL","A+"]]
print(array_2d[0][1])

array_3d = [[["Sapnap","C-", "Very Good"],["Dream","A+","Outstanding"],["Tommy Innit","B","Excellent"],["Technoblade","A+","Outstanding"],["PraysNL","A+","Outstanding"]]]
print(array_3d[0][1][2])

def report():
    label["text"] = array_3d[0][1][0] + " got graded in MCC " + array_3d[0][1][1] + "and he is doing " + array_3d[0][1][2] + " in it"
    
btn = Button(root, text= "show report", command = report)
btn.place(relx=0.5,rely =0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)


root.mainloop()

