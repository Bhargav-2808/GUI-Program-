
#Import needfull moduls
import tkinter as tk
import os
import shutil
from tkinter import ttk
from csv import DictWriter
from tkinter import messagebox as m_box

win = tk.Tk()

win.title('GUI APP')

r"""
# creating lables using loop
labels=['Enter yur Name :','Enter your age :','Enter your Email :','Enter Your gender :']

for i in range(len(labels)):
    cur_lable = 'lable'+str(i)
    cur_lable=ttk.Label(win ,text=labels[i])
    cur_lable.grid(row=i,column=0,sticky=tk.W)

#creating entry box using loop

user_info={
    'name': tk.StringVar(),
    'age':  tk.StringVar(),
    'email':  tk.StringVar()
}

counter=0
for i in user_info:
    cur_entry='entry'+i
    cur_entry=ttk.Entry(win,width=20 ,textvariable=user_info[i])
    cur_entry.grid(column=1,row=counter)
    counter+=1
"""
lable_frame=ttk.LabelFrame(win, text="Enter Your Details")
lable_frame.grid(row=0,column=0 ,padx=540,pady=50)

label_name = ttk.Label(lable_frame, text='Enter your Name :')
label_name.grid(row=0,column=0,sticky=tk.W, padx=4 ,pady=4)

label_age = ttk.Label(lable_frame, text='Enter your age :')
label_age.grid(row=1,column=0 , sticky=tk.W , padx=4 ,pady=4)

label_email = ttk.Label(lable_frame, text='Enter your email :')
label_email.grid(row=2,column=0 ,sticky=tk.W , padx=4 ,pady=4)

label_gender = ttk.Label(lable_frame, text='Enter your gender :')
label_gender.grid(row=3,column=0,sticky=tk.W , padx=4 ,pady=4)

#creating entry boxes
var_name=tk.StringVar()
entrybox_name=ttk.Entry(lable_frame, width=20 ,textvariable= var_name)
entrybox_name.grid(row=0,column=1, padx=4 ,pady=4)
entrybox_name.focus()

var_age=tk.StringVar()
entrybox_age=ttk.Entry(lable_frame, width=20,textvariable= var_age)
entrybox_age.grid(row=1,column=1 , padx=4 ,pady=4)

var_email=tk.StringVar()
entrybox_email=ttk.Entry(lable_frame, width=20,textvariable= var_email)
entrybox_email.grid(row=2,column=1 , padx=4 ,pady=4)

var_gender=tk.StringVar()
gender_combobox=ttk.Combobox(lable_frame,width=17,textvariable=var_gender,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.grid(row=3,column=1 , padx=4 ,pady=4)
gender_combobox.current(0)

usertype=tk.StringVar()
radiobtn1=ttk.Radiobutton(lable_frame,text='Student',value='student',variable=usertype)
radiobtn1.grid(row=4,column=0 , padx=4 ,pady=4)

radiobtn2=ttk.Radiobutton(lable_frame,text='Teacher',value='teacher',variable=usertype)
radiobtn2.grid(row=4,column=1, padx=4 ,pady=4)

var_checkbtn=tk.IntVar()
checkbtn=ttk.Checkbutton(lable_frame,text='Check(Tick) if you want to set reminder of your  class',variable=var_checkbtn)
checkbtn.grid(row=5,columnspan=3)

#creat function for get data
r"""
def submit():
    user_name=var_name.get()
    user_age=var_age.get()
    user_email=var_email.get()
    print(f"{user_name} is {user_age} old and email id of user is {user_email}")
    user_gender=var_gender.get()
    user_type=usertype.get()
    if var_checkbtn.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'
    print(f"Gender of user is {user_gender}. User-Type is {user_type}. Subscribing status is {subscribed}")
    folderpath=input("Enter the folder pth where you want to store your file :")
    
    with open('Data.txt','a') as f:
        f.write(f"{user_name} {user_age} {user_email} {user_gender} {user_type} {subscribed}")
    shutil.move(r'F:\python\pro2\Data.txt',folderpath)


    entrybox_name.delete(0,tk.END)
    entrybox_age.delete(0,tk.END)
    entrybox_email.delete(0,tk.END)
    label_name.configure(foreground='Blue')
    label_age.configure(foreground='Blue')
    label_email.configure(foreground='Blue')
    submit_button.configure(foregroung='Blue')
    print(f"Gender of user is {user_gender}. User-Type is {user_type}. Subscribing status is {subscribed}")
    folderpath=input("Enter the folder pth where you want to store your file :")
    
"""

def submit():
    user_name=var_name.get()
    user_age=var_age.get()
    user_email=var_email.get()

    user_gender=var_gender.get()
    user_type=usertype.get()
    
    if var_checkbtn.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'
    
    if user_age == '' or user_email =='' or user_gender == '' or user_name =='' or user_type == '':
        m_box.showerror('Error', "Please fill all details !!")
    else:
        try:
            user_age=int(user_age)
        except ValueError:
            m_box.showerror('Type error', "Please enter Your age in Digits !")
        else:
            m_box.showinfo("Message",'Thanks for your information ')
    
    
    
    
    with open('Data.csv','a',newline='') as f:
        dict_w=DictWriter(f,fieldnames=['User name','user email address','user age','user type','Subscription','User gender'])
        if os.stat('Data.csv').st_size==0:
            
            dict_w.writeheader()
        
        dict_w.writerow({
            'User name' : user_name,
            'user email address' : user_email,
            'user age' : user_age,
            'user type' : user_type,
            'Subscription' : subscribed,
            'User gender': user_gender,
        })
    
    
    entrybox_name.delete(0,tk.END)
    entrybox_age.delete(0,tk.END)
    entrybox_email.delete(0,tk.END)
    
    

submit_button=tk.Button(lable_frame, text="submit" ,command= submit)
submit_button.grid(row=6,column=0 , padx=4 ,pady=4)

win.mainloop()