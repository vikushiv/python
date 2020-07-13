import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("First Windows")

#name lebel
name_label=ttk.Label(win,text="Enter your name")
name_label.grid(row=0,column=0,sticky=tk.W)

name_var=tk.StringVar()
entry_label=ttk.Entry(win,width=16,textvariable=name_var)
entry_label.grid(row=0,column=1)
entry_label.focus()



#age lebel
age_label=ttk.Label(win,text="Enter your age")
age_label.grid(row=1,column=0,sticky=tk.W)

age_var=tk.StringVar()
age_entry=ttk.Entry(win,width=16,textvariable=age_var)
age_entry.grid(row=1,column=1)


#mail label
mail_label=ttk.Label(win,text="Enter your mail")
mail_label.grid(row=2,column=0,sticky=tk.W)

mail_var=tk.StringVar()
mail_entry=ttk.Entry(win,width=16,textvariable=mail_var)
mail_entry.grid(row=2,column=1)

#gender label
sex_lebel=ttk.Label(win,text="sex")
sex_lebel.grid(row=3,column=0,sticky=tk.W)

sex_var=tk.StringVar()
sex_entry=ttk.Combobox(win,width=13,textvariable=sex_var,state='readonly')
sex_entry['values']=('male','female','other')
sex_entry.current(0)
sex_entry.grid(row=3,column=1)


#type lebel
type_var=tk.StringVar()
type_radio1=ttk.Radiobutton(win,text='Student',value='Student',variable=type_var)
type_radio1.grid(row=4,column=0)

type_radio2=ttk.Radiobutton(win,text='teacher',value='Teacher',variable=type_var)
type_radio2.grid(row=4,column=1)


#newsleter
news_var=tk.IntVar()
news_lebel=ttk.Checkbutton(win,text='Ckeck to get news update',variable=news_var)
news_lebel.grid(row=5,columnspan=3)



#button lebel
def action():
    username=name_var.get()
    userage=age_var.get()
    usermail=mail_var.get()
    usersex=sex_var.get()
    usertype=type_var.get()
    if news_var.get()==0:
        subscribe='No'
    else:
       subscribe='Yes'
    with open('File.txt','a') as f:
       f.write(f'{username},{userage},{usermail},{usersex},{usertype},{subscribe}\n')
    

   #to emply form at last
    entry_label.delete(0,tk.END)
    age_entry.delete(0,tk.END)
    mail_entry.delete(0,tk.END)
    name_label.configure(foreground='blue')


    print(f"Use name is {username} .and age is {userage} .and mail is {usermail}.and sex is {usersex},and type is {usertype},and subscription is {subscribe}")


#name_submit=ttk.Button(win,text="submit",command=action)
#name_submit.grid(row=6,columnspan=2)



win.mainloop()

