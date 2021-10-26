from tkinter import *
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import ttk
import time
from tkinter import messagebox
import backendh
import os
from tkinter import filedialog
import random
from tkinter import PhotoImage
global data_list
global x
x = datetime.today()
x = str(x).split()[0]

#developed by rakibul hasan asif
#------------------about function-------------------
def about():
    messagebox.showinfo("About", "This application is developed by Rakibul Hasan Asif  (rakibul4210@gmail.com)")

#------------------------quote function--------------------------------
def quote_func():
    quote = random.choice(list_quote)
    quote_label.config(text=quote)
#--------------------------------receipt--------------------------------
def saved():
    info = text_area.get("1.0", "end-1c")
    resip = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    resip.write(info)
    resip.close()
    messagebox.showinfo("saved", "Your receipt has been saved")
    text_area.delete("1.0", "end")


#---------------------------------------database--------------------------
def submits():
    reply = messagebox.askyesno("confirmation!", "Do you really want to submit?")
    if reply == True:
        backendh.insert(date.get(),name.get(), email.get(),c_pack_cmb.get(),room_num_cmb.get(),room_rb.get(),food_rb.get(),room_no.get(), addr.get(), national.get(),total_cost.get())
        data_list.delete(0, END)
        data_list.insert(END,(date.get(),name.get(), email.get(),c_pack_cmb.get(),room_num_cmb.get(),room_rb.get(),food_rb.get(),room_no.get(), addr.get(), national.get(),total_cost.get()))

        #------------------text area--------------------
        text_area.insert(END, f"Date: {date.get()} | ")
        text_area.insert(END, f"Name: {name.get()} | ")
        text_area.insert(END, f"email or phone: {email.get()} | ")
        text_area.insert(END, f"room no: {room_no.get()} | ")
        text_area.insert(END, f"package: {c_pack_cmb.get()} | ")
        text_area.insert(END, f"number of rooms: {room_num_cmb.get()} | ")
        text_area.insert(END, f"Food type: {food_rb.get()} | ")
        text_area.insert(END, f"Total Payment: {total_cost.get()} | ")
        messagebox.showinfo("Saved", "Your data has been saved successfully!")
    else:
        messagebox.showwarning("Warning", "Your data couldn't be saved!")
def search_func():
    data_list.delete(0,END)
    for row in backendh.search(date.get(),email.get()):
        data_list.insert(END, row)
def view_all():
    data_list.delete(0, END)
    for row in backendh.view():
        data_list.insert(END, row)
def delete_func():
    global data_list
    global name
    index = data_list.curselection()[0]
    name = data_list.get(index)
    backendh.delete(name[0])
    view_all()
#------------------------------calculator funtions------------------------
global operators
operators = ''

def calculate(numbers):
    global calc_main
    global operators
    operators = operators + str(numbers)
    calc_main.set(operators)
    pass
def clear():
    global operators
    operators = ''
    calc_main.set(operators)
    calc_entry.delete(0, END)
    calc_main.set(operators)
    pass
def equal():
    global operators
    global calc_main
    result = float(eval(operators))
    calc_main.set(result)
    operators = ''
#---------------------------calculation button-------------
def show_total():
    global price
    global priced
    #room_cost
    global room_num_cmb
    f = int(room_num_cmb.get())
    if c_pack_cmb.get() == "1 day" and room_rb.get() == '1' :
        #one day  vip room cost 100   
        price = (1 * 100) * f
        room_cost.set(price)
    elif c_pack_cmb.get() == "3 days" and room_rb.get() == '1' :
        #one day  vip room cost 100
        price = (3*95)* f
        room_cost.set(price)
    elif c_pack_cmb.get() == "5 days" and room_rb.get() == '1' :
        #one day  vip room cost 100
        price = (5 * 90)* f
        room_cost.set(price)
    elif c_pack_cmb.get() == "7 days" and room_rb.get() == '1' :
        #one day  vip room cost 100
        price = (7 * 85)* f
        room_cost.set(price)
    elif c_pack_cmb.get() == "1 month" and room_rb.get() == '1' :
        #one day  vip room cost 100
        price = (30 * 70)* f
        room_cost.set(price)
    else:
        pass

    if c_pack_cmb.get() == "1 day" and room_rb.get() == '2' :
        #one day  vip room cost 100
        price = (1 * 50)* f
        room_cost.set(price)
    elif c_pack_cmb.get() == "3 days" and room_rb.get() == '2' :
        #one day  vip room cost 100
        price = (3*48)* f
        room_cost.set(price)
    elif c_pack_cmb.get() == "5 days" and room_rb.get() == '2' :
        #one day  vip room cost 100
        price = (5 * 45)* f
        room_cost.set(price)
    elif c_pack_cmb.get() == "7 days" and room_rb.get() == '2' :
        #one day  vip room cost 100
        price = (7 * 40)* f
        room_cost.set(price)
    elif c_pack_cmb.get() == "1 month" and room_rb.get() == '2' :
        #one day  vip room cost 100
        price = (30 * 35)* f
        room_cost.set(price)
    else:
        pass


    #food cost
    if c_pack_cmb.get() == "1 day" and food_rb.get() == '1' :
        #one day  vip room cost 100
        priced = (1 * 30)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "3 days" and food_rb.get() == '1' :
        #one day  vip room cost 100
        priced = (3 * 27)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "5 days" and food_rb.get() == '1' :
        #one day  vip room cost 100
        priced = (5 * 25)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "7 days" and food_rb.get() == '1' :
        #one day  vip room cost 100
        priced = (7 * 23)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "1 month" and food_rb.get() == '1' :
        #one day  vip room cost 100
        priced = (30 * 20)* f
        food_cost.set(priced)
    else:
        pass

    if c_pack_cmb.get() == "1 day" and food_rb.get() == '2' :
        #one day  vip room cost 100
        priced = (1 * 20)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "3 days" and food_rb.get() == '2' :
        #one day  vip room cost 100
        priced = (3 * 18)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "5 days" and food_rb.get() == '2' :
        #one day  vip room cost 100
        priced = (5 * 16)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "7 days" and food_rb.get() == '2' :
        #one day  vip room cost 100
        priced = (7 * 15)* f
        food_cost.set(priced)
    elif c_pack_cmb.get() == "1 month" and food_rb.get() == '2' :
        #one day  vip room cost 100
        priced = (30 * 13)* f
        food_cost.set(priced)
    else:
        pass
    #delivery cost
    days = c_pack_cmb.get().split()[0]
    day = int(days)
    delivery = 1 * day * f
    del_cost.set(delivery)

    #total cost
    total = price + priced + delivery
    total_cost.set(total)


#-----------------------------clean function------------------
def clean():
    global room_num_cmb
    room_rb.set(2)
    food_rb.set(2)
    c_pack_cmb.current(0)
    room_num_cmb.current(0)
    room_cost.set("")
    food_cost.set("")
    del_cost.set("")
    total_cost.set("")
    text_area.delete("1.0", "end")
#-----------------------------reset button -----------------------
def reset():
    global room_num_cmb
    room_rb.set(2)
    food_rb.set(2)
    c_pack_cmb.current(0)
    room_num_cmb.current(0)
    room_cost.set("")
    food_cost.set("")
    del_cost.set("")
    total_cost.set("")
    name.set("")
    addr.set("")
    email.set("")
    national.set("")
    gender.set("")
    room_no.set("")
    cur_amnt.set("")
    rate_amnt.set("")
    amount_amnt.set("")
    text_area.delete("1.0", "end")
    time.sleep(1)
    messagebox.showinfo("Application resetted", "Input New Entries!")

#--------------------------back-----------------
def back():
    global book_frame
    book_frame.pack_forget()
    bar_frame.pack_forget()
    details_frame.place_forget()
    main_frame.pack(fill="both", expand=1)
def Back():
    global data_frame
    global bar_data_frame
    data_frame.pack_forget()
    bar_data_frame.pack_forget()
    btn_frames.place_forget()
    main_frame.pack(fill="both", expand=1)


#------------------------convert---------------------
def convert():
    main_bal = float(cur_amnt.get())
    cur_bal = float(rate_amnt.get())
    converted = main_bal * cur_bal
    amount_amnt.set(converted)
def booking():
    global book_frame
    book_frame.pack_forget()
    main_frame.pack_forget()
    book_frame.pack(fill="both", expand=1)
    #bar frame
    global bar_frame
    bar_frame = Frame(book_frame, bg="lightgray", relief=RIDGE)
    bar_frame.pack()
    bar = Label(bar_frame, text="Input The Informations Of New Customers", font=("roboto", 32, "bold"), bg="Darkred", fg="white", relief=RIDGE, bd=10, width=1600)
    bar.pack( ipady=8, ipadx=15)
    #details frame
    global details_frame
    details_frame = LabelFrame(book_frame, text="Customer Details: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    details_frame.place(x=10, y=110)

    c_name_label = Label(details_frame, text="Full name: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_name_label.grid(row=0, column=0, padx=10, pady=5)
    global name
    name = StringVar()
    c_name_entry = Entry(details_frame,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=name)
    c_name_entry.grid(row=0, column=1, padx=10, pady=5)

    c_add_label = Label(details_frame, text="Address: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_add_label.grid(row=1, column=0, padx=10, pady=5)
    global addr
    addr = StringVar()
    c_add_entry = Entry(details_frame,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable= addr)
    c_add_entry.grid(row=1, column=1, padx=10, pady=5)

    c_email_label = Label(details_frame, text="Email or Phone: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_email_label.grid(row=2, column=0, padx=10, pady=5)
    global email
    email = StringVar()
    c_email_entry = Entry(details_frame,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=email)
    c_email_entry.grid(row=2, column=1, padx=10, pady=5)

    c_country_label = Label(details_frame, text="Nationality: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_country_label.grid(row=3, column=0, padx=10, pady=5)
    global national
    national = StringVar()
    c_country_entry = Entry(details_frame,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=national)
    c_country_entry.grid(row=3, column=1, padx=10, pady=5)

    c_gender_label = Label(details_frame, text="Gender: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_gender_label.grid(row=4, column=0, padx=10, pady=5)
    global gender
    gender = StringVar()
    c_gender_entry = Entry(details_frame,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=gender)
    c_gender_entry.grid(row=4, column=1, padx=10, pady=5)

    #currency converter
    pack_frame = LabelFrame(book_frame,  text="Package Details: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    pack_frame.place(x=10, y=380)

    c_date_label = Label(pack_frame, text="Date: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_date_label.grid(row=0, column=0, padx=10, pady=5)
    global date
    global x
    date = StringVar()
    date.set(x)
    c_date_entry = Entry(pack_frame,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=date)
    c_date_entry.grid(row=0, column=1, padx=10, pady=5)

    c_pack_label = Label(pack_frame, text="Available packages: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_pack_label.grid(row=1, column=0, padx=10, pady=5)
    global c_pack_cmb
    pack_list = ["1 day", "3 days", "5 days", "7 days", "1 month"]
    c_pack_cmb = ttk.Combobox(pack_frame,font=("roboto", 16, "bold"),width=15, value=pack_list)
    c_pack_cmb.current(0)
    c_pack_cmb.grid(row=1, column=1, padx=10, pady=5)

    c_room_label = Label(pack_frame, text="Room type: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_room_label.grid(row=2, column=0, padx=10, pady=5)
    global room_rb
    room_rb = StringVar()
    room_rb1 = Radiobutton(pack_frame, text="VIP",font=("roboto", 15, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=4, variable=room_rb, value=1) 
    room_rb1.grid(row=2, column=1, padx=10, pady=5, sticky=W)
    room_rb2 = Radiobutton(pack_frame, text="Normal",font=("roboto", 15, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=6, variable=room_rb, value=2) 
    room_rb2.grid(row=2, column=1, padx=2, sticky=E)
    room_rb.set(2)
    c_food_label = Label(pack_frame, text="Food type: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_food_label.grid(row=3, column=0, padx=10, pady=5)

    global food_rb
    food_rb = StringVar()
    food_rb1 = Radiobutton(pack_frame, text="VIP",font=("roboto", 15, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=4, variable=food_rb, value=1) 
    food_rb1.grid(row=3, column=1, padx=10, pady=5, sticky=W)
    food_rb2 = Radiobutton(pack_frame, text="Normal",font=("roboto", 15, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=6, variable=food_rb, value=2) 
    food_rb2.grid(row=3, column=1, padx=2, sticky=E)
    food_rb.set(2)

    room_num_list = ["1", "2", "3", "4", "5", "6", "7","8","9","10"]
    number_of_rooms =  Label(pack_frame, text="Num of rooms: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    number_of_rooms.grid(row=4, column=0, padx=10, pady=5)
    global room_num_cmb
    room_num_cmb = ttk.Combobox(pack_frame,font=("roboto", 16, "bold"),width=15, value=room_num_list)
    room_num_cmb.grid(row=4, column=1, padx=10, pady=5)
    room_num_cmb.current(0)

    c_roomno_label = Label(pack_frame, text="Booked room no: ",font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=16, justify=RIGHT )
    c_roomno_label.grid(row=5, column=0, padx=10, pady=5)
    global room_no 
    room_no = StringVar()
    c_roomno_entry = Entry(pack_frame,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=room_no)
    c_roomno_entry.grid(row=5, column=1, padx=10, pady=5)

    #total cost frame
    cost_frame =  LabelFrame(book_frame, text="Total cost: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    cost_frame.place(x=555, y=110)

    room_cost_label = Label(cost_frame, text="Room cost($): ",font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=14, justify=RIGHT )
    room_cost_label.grid(row=0, column=0, padx=10, pady=3)
    global room_cost
    room_cost = StringVar()
    room_cost_entry = Entry(cost_frame,font=("roboto", 14, "bold"), bg="lightgray", relief="sunken", bd=3, width=14, justify=RIGHT, textvariable=room_cost, fg="black")
    room_cost_entry.grid(row=0, column=1, padx=10, pady=3)

    food_cost_label = Label(cost_frame, text="Food cost($): ",font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=14, justify=RIGHT )
    food_cost_label.grid(row=1, column=0, padx=10, pady=3)
    global food_cost
    food_cost = StringVar()
    food_cost_entry = Entry(cost_frame,font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=14, justify=RIGHT, textvariable=food_cost)
    food_cost_entry.grid(row=1, column=1, padx=10, pady=3)

    del_cost_label = Label(cost_frame, text="Delivery cost($): ",font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=14, justify=RIGHT )
    del_cost_label.grid(row=2, column=0, padx=10, pady=3)
    global del_cost
    del_cost = StringVar()
    del_cost_entry = Entry(cost_frame,font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=14, justify=RIGHT, textvariable=del_cost)
    del_cost_entry.grid(row=2, column=1, padx=10, pady=3)

    total_cost_label = Label(cost_frame, text="Total cost($): ",font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=14, justify=RIGHT )
    total_cost_label.grid(row=3, column=0, padx=10, pady=3)
    global total_cost
    total_cost = StringVar()
    total_cost_entry = Entry(cost_frame,font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=14, justify=RIGHT, textvariable=total_cost)
    total_cost_entry.grid(row=3, column=1, padx=10, pady=3)


     #CURRENCY CONVERTER
    currency_frame = LabelFrame(book_frame, text="Currency Converter: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    currency_frame.place(x=555, y=305)

    cur_label = Label(currency_frame, text="Amount($): ",font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=14, justify=RIGHT )
    cur_label.grid(row=0, column=0, padx=10, pady=2)
    global cur_amnt
    cur_amnt = StringVar()
    cur_entry = Entry(currency_frame,font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=14, justify=RIGHT, textvariable=cur_amnt)
    cur_entry.grid(row=0, column=1, padx=10, pady=2)

    rate_label = Label(currency_frame, text="conversion rate: ",font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=14, justify=RIGHT )
    rate_label.grid(row=1, column=0, padx=10, pady=2)
    global rate_amnt
    rate_amnt = StringVar()
    rate_entry = Entry(currency_frame,font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=14, justify=RIGHT, textvariable=rate_amnt)
    rate_entry.grid(row=1, column=1, padx=10, pady=2)

    amount_label = Label(currency_frame, text="Native amount: ",font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=14, justify=RIGHT )
    amount_label.grid(row=2, column=0,padx=10, pady=2)
    global amount_amnt
    amount_amnt = StringVar()
    amount_entry = Entry(currency_frame,font=("roboto", 14, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=14, justify=RIGHT, textvariable=amount_amnt)
    amount_entry.grid(row=2, column=1, padx=10, pady=2)

    convert_btn = Button(currency_frame, text="Convert", font=("roboto", 13, "bold"), bg="red", fg="white", relief="raised", bd=2, width=13, command=convert, activebackground="brown", activeforeground="white")
    convert_btn.grid(row=3, column = 1, padx=7, pady=2)

    #sumup buttons
    sumup_frame = LabelFrame(book_frame, text="Menu: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    sumup_frame.place(x=555, y=495)
    global total_btn
    total_btn = Button(sumup_frame, text="Show total", font=("roboto", 13, "bold"), bg="green", fg="white", relief="raised", bd=2, width=14, command=show_total, activebackground="brown", activeforeground="white")
    total_btn.grid(row=0, column = 0, padx=7, pady=5)

    sub_btn = Button(sumup_frame, text="Submit", font=("roboto", 13, "bold"), bg="green", fg="white", relief="raised", bd=2, width=14, command=submits, activebackground="brown", activeforeground="white")
    sub_btn.grid(row=0, column = 1, padx=7, pady=5)

    clear_btn = Button(sumup_frame, text="Clear", font=("roboto", 13, "bold"), bg="green", fg="white", relief="raised", bd=2, width=14, command=clean, activebackground="brown", activeforeground="white")
    clear_btn.grid(row=1, column = 0, padx=7, pady=5)

    reset_btn = Button(sumup_frame, text="Reset", font=("roboto", 13, "bold"), bg="red", fg="white", relief="raised", bd=2, width=14, command=reset, activebackground="brown", activeforeground="white")
    reset_btn.grid(row=1, column = 1, padx=7, pady=5)

    back_btn = Button(sumup_frame, text="Back", font=("roboto", 13, "bold"), bg="red", fg="white", relief="raised", bd=2, width=14, command=back, activebackground="brown", activeforeground="white")
    back_btn.grid(row=2, column = 0, padx=7, pady=5)

    exit_btn = Button(sumup_frame, text="Exit", font=("roboto", 13, "bold"), bg="red", fg="white", relief="raised", bd=2, width=14, command=root.quit, activebackground="brown", activeforeground="white")
    exit_btn.grid(row=2, column = 1, padx=7, pady=5)

    #calculator
    calc_frame = LabelFrame(book_frame, text="Calculator: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    calc_frame.place(x=986, y=110)
    global calc_main, calc_entry
    calc_main = StringVar()
    calc_entry = Entry(calc_frame,font=("roboto", 23, "bold"), bg="lightgray", fg="black", relief="sunken", bd=5, width=16, justify=RIGHT, textvariable=calc_main)
    calc_entry.grid(row=0, column=0, columnspan=4, padx=6, pady=2)

    #buttons
    global btn_0, btn_1, btn_2,  btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9
    global btn_p, btn_m, btn_C,  btn_dot, btn_mul, btn_div, btn_first_bra, btn_scnd_bra, btn_ans
    #row 1
    btn_7 = Button(calc_frame, text="7", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(7), activebackground="brown", activeforeground="white")
    btn_7.grid(row=1, column = 0, pady=2, ipadx=19, ipady=8)
    btn_8 = Button(calc_frame, text="8", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(8), activebackground="brown", activeforeground="white")
    btn_8.grid(row=1, column = 1, pady=2, ipadx=20, ipady=8)
    btn_9 = Button(calc_frame, text="9", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(9), activebackground="brown", activeforeground="white")
    btn_9.grid(row=1, column = 2, pady=2, ipadx=20, ipady=8)
    btn_C = Button(calc_frame, text="C", font=("roboto", 13, "bold"), bg="green", fg="black", relief="raised", bd=2, command=clear, activebackground="brown", activeforeground="white")
    btn_C.grid(row=1, column = 3, pady=2, ipadx=19, ipady=8)

    #row2
    btn_4 = Button(calc_frame, text="4", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(4), activebackground="brown", activeforeground="white")
    btn_4.grid(row=2, column = 0, pady=2, ipadx=19, ipady=8)
    btn_5 = Button(calc_frame, text="5", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(5), activebackground="brown", activeforeground="white")
    btn_5.grid(row=2, column = 1, pady=2, ipadx=20, ipady=8)
    btn_6 = Button(calc_frame, text="6", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(6), activebackground="brown", activeforeground="white")
    btn_6.grid(row=2, column = 2, pady=2, ipadx=20, ipady=8)
    btn_p = Button(calc_frame, text="+", font=("roboto", 13, "bold"), bg="tomato", fg="black", relief="raised", bd=2, command=lambda : calculate('+'), activebackground="brown", activeforeground="white")
    btn_p.grid(row=2, column = 3, pady=2, ipadx=19, ipady=8)

    #row3
    btn_1 = Button(calc_frame, text="1", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(1), activebackground="brown", activeforeground="white")
    btn_1.grid(row=3, column = 0, pady=2, ipadx=19, ipady=8)
    btn_2 = Button(calc_frame, text="2", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(2), activebackground="brown", activeforeground="white")
    btn_2.grid(row=3, column = 1, pady=2, ipadx=20, ipady=8)
    btn_3 = Button(calc_frame, text="3", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(3), activebackground="brown", activeforeground="white")
    btn_3.grid(row=3, column = 2, pady=2, ipadx=20, ipady=8)
    btn_m = Button(calc_frame, text="-", font=("roboto", 13, "bold"), bg="tomato", fg="black", relief="raised", bd=2, command=lambda : calculate('-'), activebackground="brown", activeforeground="white")
    btn_m.grid(row=3, column = 3, pady=2, ipadx=22, ipady=8)

    #row4
    btn_0 = Button(calc_frame, text="0", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(0), activebackground="brown", activeforeground="white")
    btn_0.grid(row=4, column = 0, pady=2, ipadx=19, ipady=8)
    btn_dot = Button(calc_frame, text=".", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate('.'), activebackground="brown", activeforeground="white")
    btn_dot.grid(row=4, column = 1, pady=2, ipadx=21, ipady=8)
    btn_mul = Button(calc_frame, text="x", font=("roboto", 13, "bold"), bg="tomato", fg="black", relief="raised", bd=2, command=lambda : calculate('*'), activebackground="brown", activeforeground="white")
    btn_mul.grid(row=4, column = 2, pady=2, ipadx=21, ipady=8)
    btn_div = Button(calc_frame, text="/", font=("roboto", 13, "bold"), bg="tomato", fg="black", relief="raised", bd=2, command=lambda : calculate('/'), activebackground="brown", activeforeground="white")
    btn_div.grid(row=4, column = 3, pady=2, ipadx=22, ipady=8)

    #row5
    btn_first_bra = Button(calc_frame, text="(", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate('('), activebackground="brown", activeforeground="white")
    btn_first_bra.grid(row=5, column = 0, pady=2, ipadx=22, ipady=8)
    btn_scnd_bra = Button(calc_frame, text=")", font=("roboto", 13, "bold"), bg="white", fg="black", relief="raised", bd=2, command=lambda : calculate(')'), activebackground="brown", activeforeground="white")
    btn_scnd_bra.grid(row=5, column = 1, pady=2, ipadx=22, ipady=8)
    btn_ans = Button(calc_frame, text="=", font=("roboto", 13, "bold"), bg="Green", fg="black", relief="raised", bd=2, command= equal, activebackground="brown", activeforeground="white")
    btn_ans.grid(row=5, column = 2,columnspan=2, pady=2, ipadx=65, ipady=8)

    #receipt frame
    receipt_frame = LabelFrame(book_frame,  text="Receipt: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    receipt_frame.place(x=986, y=490)
    
    global text_area
    text_area = Text(receipt_frame, height=5, width=40, font=("arial", 12, "bold"), bg="white", fg="black")
    text_area.grid(row=0, column=0, columnspan=3)

    btn_r_save = Button(receipt_frame, text="Save", font=("roboto", 12, "bold"), bg="green", fg="black", relief="raised", bd=2, command=saved, activebackground="brown", activeforeground="white")
    btn_r_save.grid(row=1, column = 0, pady=2, ipadx=20, ipady=4)
    btn_r_send = Button(receipt_frame, text="Send", font=("roboto", 12, "bold"), bg="green", fg="black", relief="raised", bd=2, activebackground="brown", activeforeground="white")
    btn_r_send.grid(row=1, column = 1, pady=2, ipadx=20, ipady=4)
    btn_r_print = Button(receipt_frame, text="Print", font=("roboto", 12, "bold"), bg="green", fg="black", relief="raised", bd=2, activebackground="brown", activeforeground="white")
    btn_r_print.grid(row=1, column = 2, pady=2, ipadx=20, ipady=4)

#----------------------------------dataset----------------------------
def database():
    global date
    main_frame.pack_forget()
    global data_frame
    data_frame.pack(fill="both", expand=1)

    global bar_data_frame
    bar_data_frame = Frame(data_frame, bg="lightgray", relief=RIDGE)
    bar_data_frame.pack(side=TOP)
    bar_data = Label(bar_data_frame, text="Hotel Database", font=("roboto", 32, "bold"), bg="Darkred", fg="white", relief=RIDGE, bd=10, width=1600)
    bar_data.pack( ipady=8, ipadx=15)
    

    #btn_frames
    global btn_frames
    btn_frames = LabelFrame(data_frame, text="Menu: ", bg="Darkred", fg="white", relief=RIDGE, font=("roboto", 14,"bold"))
    btn_frames.place(x=15, y=110)

    #BUTTONS
    btn_search = Button(btn_frames, text="Search By", font=("roboto", 14, "bold"), bg="Green", fg="black", relief="raised", bd=2, command=search_func, activebackground="brown", activeforeground="white")
    btn_search.grid(row=0, column = 0, pady=15, ipadx=8, ipady=14, padx=10)
    date_label = Label(btn_frames, text="Date: ",font=("roboto", 18, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=15, justify=RIGHT )
    date_label.grid(row=0, column=1, padx=10, pady=2, ipady=14)
    email_label = Label(btn_frames, text="Email: ",font=("roboto", 18, "bold"), bg="lightgray", fg="black", relief="raised", bd=2, width=15, justify=RIGHT )
    email_label.grid(row=0, column=3, padx=10, pady=2, ipady=14)

    global date
    date = StringVar()
    date_entry = Entry(btn_frames,font=("roboto", 18, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=date)
    date_entry.grid(row=0, column=2, padx=10, pady=2, ipady=13)
    global email
    email = StringVar()
    email_entry = Entry(btn_frames,font=("roboto", 18, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=16, justify=RIGHT, textvariable=email)
    email_entry.grid(row=0, column=4, padx=10, pady=2, ipady=13)

    btn_show = Button(btn_frames, text="SHOW", font=("roboto", 14, "bold"), bg="Green", fg="black", relief="raised", bd=2, command=view_all, activebackground="brown", activeforeground="white")
    btn_show.grid(row=1, column = 0, pady=15, ipadx=25, ipady=14, padx=10)
    btn_remove = Button(btn_frames, text="REMOVE", font=("roboto", 14, "bold"), bg="Green", fg="black", relief="raised", bd=2, command=delete_func, activebackground="brown", activeforeground="white")
    btn_remove.grid(row=2, column = 0, pady=15, ipadx=10, ipady=14, padx=10)
    btn_back = Button(btn_frames, text="BACK", font=("roboto", 14, "bold"), bg="Green", fg="black", relief="raised", bd=2, command=Back, activebackground="brown", activeforeground="white")
    btn_back.grid(row=4, column = 0, pady=15, ipadx=25, ipady=14, padx=10)
    btn_exit = Button(btn_frames, text="EXIT", font=("roboto", 14, "bold"), bg="Green", fg="black", relief=GROOVE, bd=2, command=root.quit, activebackground="brown", activeforeground="white")
    btn_exit.grid(row=5, column = 0, pady=15, ipadx=30, ipady=14, padx=10)
    

    ##listbox
    global data_list
    data_list = Listbox(btn_frames,font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="sunken", bd=3, width=75, height=13)
    data_list.grid(row=1, column=1, columnspan=4, rowspan=6)
    l1 = Label(btn_frames, text="Hey, Good to see you here!", font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief=RIDGE, bd=10)
    l1.grid(row=7, column = 1, columnspan=4, pady=2, ipadx=15, ipady=5)


root = Tk()
root.title("Hotel management programme")
root.geometry("1600x800")
global data_list

##main frame
global main_frame
main_frame = Frame(root, bg="darkred")
main_frame.pack(fill="both", expand=1)

name_label = Label(main_frame, text="Welcome To The Hotel Paradise", font=("roboto", 32, "bold"), bg="lightgray", fg="black", relief=RIDGE, bd=10)
name_label.pack(pady=15, ipady=15, ipadx=16)

'''
time_date_label = Label(main_frame, text=Time, font=("roboto", 32, "bold"), bg="lightgray", fg="black", relief="raised", bd=5)
time_date_label.pack(pady=10, ipady=5, ipadx=5)
'''
book_btn = Button(main_frame, text="New Booking", font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=5, width=16, command=booking, activebackground="brown", activeforeground="white")
book_btn.pack(pady=5, ipady=7, ipadx=16)

data_btn = Button(main_frame, text="Check Database", font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=5, width=16, command=database, activebackground="brown", activeforeground="white")
data_btn.pack(pady=5,ipady=7, ipadx=16)

quote_btn = Button(main_frame, text="Change Quote", font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=5, width=16, activebackground="brown", activeforeground="white", command=quote_func)
quote_btn.pack(pady=5,ipady=7, ipadx=16)

about_btn = Button(main_frame, text="About", font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=5, width=16, activebackground="brown", activeforeground="white", command=about)
about_btn.pack(pady=5,ipady=7, ipadx=16)

exit_btn = Button(main_frame, text="Exit", font=("roboto", 16, "bold"), bg="lightgray", fg="black", relief="raised", bd=5, width=16, command=root.quit,activebackground="brown", activeforeground="white")
exit_btn.pack(pady=5,ipady=7, ipadx=16)
global list_quote
list_quote = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The way to get started is to quit talking and begin doing.",
    "If life were predictable it would cease to be life, and be without flavor.",
    "Life is what happens when you're busy making other plans.",
    "Always remember that you are absolutely unique. Just like everyone else.",
    "Spread love everywhere you go. Let no one ever come to you without leaving happier.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
    "It is during our darkest moments that we must focus to see the light.",
    "You will face many defeats in life, but never let yourself be defeated."
    ]
global quote
quote = random.choice(list_quote)

global quote_label
quote_label = Label(main_frame, text=quote, font=("roboto", 18, "bold"), bg="lightgray", fg="black", relief=RIDGE, bd=10)
quote_label.pack(pady=30, ipady=10, ipadx=16)


####
global book_frame
book_frame  = Frame(root, bg="lightgray")

global data_frame
data_frame = Frame(root, bg="lightgray")

#-----------------------------logo-----------------
my_image = PhotoImage(file="/home/asif/Documents/python3/GUI/hotelmanage/logo.png")
image_label = Label(main_frame,image=my_image)
image_label.place(x=10, y=600)

database()
Back()



root.mainloop()