"""
It's a tamil keyboard. Reference for look like a android keyboard.
"""
from tkinter import *
root_window=Tk()
root_window.geometry('1500x700')

#Display the text
typing_frame = Frame(root_window,width=1000,height=100, highlightbackground='red', highlightthicknes=2)
typing_frame.pack()
tamil_display = Text(typing_frame, width=75, height=10, font=('calibre',20,'bold'))
tamil_display.pack()

#TAMIL CHARACTOR PRINT FUNCTION.
def tamil_print(ch):
    chh = chr(ch)
    tamil_display.insert(END,chh)   

def clear_all():
    tamil_display.delete("1.0",END)

def text_copy():
    wordes = str(tamil_display.get('1.0',END))
    print("______TAMIL LETTERS BOARD______")
    print( wordes)
    

#Button frame
button_frame = Frame(root_window, width=200, highlightbackground='red', highlightthickness=2)
button_frame.pack()
clear_button = Button(button_frame, text="CLEAR", command=clear_all)
clear_button.pack(side=LEFT)
copy_button = Button(button_frame, text="COPY TO TERMINAL",command=text_copy)
copy_button.pack(side=LEFT)


#Keyboard Frame 1
k_f_1 = Frame(root_window, highlightbackground='red', highlightthickness=2,padx=10,pady=10)
k_f_1.pack(pady=20)

#aa_na, va_na tamil key's created.
t_b_1 = Button(k_f_1,text=chr(2949),command=lambda:tamil_print(2949),width=2,height=2,font=('bold'))
t_b_1.pack(side=LEFT)

t_b_2 = Button(k_f_1,text=chr(2950),command=lambda:tamil_print(2950),width=2,height=2,font=('bold'))
t_b_2.pack(side=LEFT)

t_b_3 = Button(k_f_1,text=chr(2951),command=lambda:tamil_print(2951),width=2,height=2,font=('bold'))
t_b_3.pack(side=LEFT)

t_b_4 = Button(k_f_1,text=chr(2952),command=lambda:tamil_print(2952),width=2,height=2,font=('bold'))
t_b_4.pack(side=LEFT)
t_b_5 = Button(k_f_1,text=chr(2953),command=lambda:tamil_print(2953),width=2,height=2,font=('bold'))
t_b_5.pack(side=LEFT)

t_b_6 = Button(k_f_1,text=chr(2954),command=lambda:tamil_print(2954),width=2,height=2,font=('bold'))
t_b_6.pack(side=LEFT)

t_b_7= Button(k_f_1,text=chr(2958),command=lambda:tamil_print(2958),width=2,height=2,font=('bold'))
t_b_7.pack(side=LEFT)

t_b_8 = Button(k_f_1,text=chr(2959),command=lambda:tamil_print(2959),width=2,height=2,font=('bold'))
t_b_8.pack(side=LEFT)

t_b_9 = Button(k_f_1,text=chr(2960),command=lambda:tamil_print(2960),width=2,height=2,font=('bold'))
t_b_9.pack(side=LEFT)

t_b_10 = Button(k_f_1,text=chr(2962),command=lambda:tamil_print(2962),width=2,height=2,font=('bold'))
t_b_10.pack(side=LEFT)

t_b_11 = Button(k_f_1,text=chr(2963),command=lambda:tamil_print(2963),width=2,height=2,font=('bold'))
t_b_11.pack(side=LEFT)

t_b_12 = Button(k_f_1,text=chr(2964),command=lambda:tamil_print(2964),width=2,height=2,font=('bold'))
t_b_12.pack(side=LEFT)

t_b_13 = Button(k_f_1,text=chr(2947),command=lambda:tamil_print(2947),width=2,height=2,font=('bold'))
t_b_13.pack(side=LEFT)
#aa_na. va_na end

#root window is changed k_f_1 frame
k_f_3 = Frame(root_window, highlightbackground='red', highlightthickness=2, padx=10,pady=10)
k_f_3.pack(pady=10) 

#charactor is upload to the text view
def charactor_upload(chrr,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel):
    tamil_display.insert(END,chrr)
    zero.pack_forget();one.pack_forget();two.pack_forget();three.pack_forget();four.pack_forget();five.pack_forget();six.pack_forget();seven.pack_forget();eight.pack_forget();nine.pack_forget();ten.pack_forget();leven.pack_forget();twel.pack_forget()

#charactor change loop function
def charactor_change_loop(chrr):
    charactor_0 = chrr
    charactor_1 = chrr;charactor_2 = chrr;charactor_3 = chrr;charactor_4 = chrr;charactor_5 = chrr;charactor_6 = chrr;charactor_7 = chrr;charactor_8 = chrr;charactor_9 = chrr;charactor_10 = chrr;charactor_11 = chrr;charactor_12 = chrr

#ik_ka_na created
    #this chrr_one,chrr_zero......chrr_twel send to the text area.
    chrr_zero = chr(charactor_0)
    zero = Button(k_f_3,text=chrr_zero,command = lambda:charactor_upload(chrr_zero,zero,one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    zero.pack(side=LEFT)

    chrr_one = chr(charactor_1)+chr(3021)
    one = Button(k_f_3,text = chrr_one,command = lambda:charactor_upload(chrr_one,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))  
    one.pack(side=LEFT)

    chrr_two = chr(charactor_2)+chr(3006)
    two = Button(k_f_3,text = chrr_two,command = lambda:charactor_upload(chrr_two,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    two.pack(side=LEFT)

    chrr_three = chr(charactor_3)+chr(3007)
    three = Button(k_f_3,text = chrr_three,command = lambda:charactor_upload(chrr_three,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    three.pack(side=LEFT)

    chrr_four = chr(charactor_4)+chr(3008)
    four = Button(k_f_3,text = chrr_four,command = lambda:charactor_upload(chrr_four,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    four.pack(side=LEFT)

    chrr_five = chr(charactor_5)+chr(3009)
    five = Button(k_f_3,text = chrr_five,command = lambda:charactor_upload(chrr_five,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    five.pack(side=LEFT)

    chrr_six = chr(charactor_6)+chr(3010)
    six = Button(k_f_3,text = chrr_six,command = lambda:charactor_upload(chrr_six,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    six.pack(side=LEFT)

    chrr_seven = chr(3014)+chr(charactor_7)
    seven = Button(k_f_3,text = chrr_seven,command = lambda:charactor_upload(chrr_seven,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    seven.pack(side=LEFT)

    chrr_eight = chr(3015)+chr(charactor_8)
    eight = Button(k_f_3,text = chrr_eight,command = lambda:charactor_upload(chrr_eight,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    eight.pack(side=LEFT)

    chrr_nine = chr(3016)+chr(charactor_9)
    nine = Button(k_f_3,text = chrr_nine,command = lambda:charactor_upload(chrr_nine,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    nine.pack(side=LEFT)

    chrr_ten = chr(charactor_10)+chr(3018)
    ten = Button(k_f_3,text = chrr_ten,command = lambda:charactor_upload(chrr_ten,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    ten.pack(side=LEFT)

    chrr_leven = chr(charactor_11)+chr(3019)
    leven = Button(k_f_3,text = chrr_leven,command = lambda:charactor_upload(chrr_leven,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    leven.pack(side=LEFT)

    chrr_twel = chr(charactor_12)+chr(3020)
    twel = Button(k_f_3,text=chrr_twel,command = lambda:charactor_upload(chrr_twel,zero, one,two,three,four,five,six,seven,eight,nine,ten,leven,twel),width=5,height=2,font=('bold'))
    twel.pack(side=LEFT)

   
    

#keyboard frame 2
k_f_2 = Frame(root_window, highlightbackground='red', highlightthickness=2,pady=10,padx=10)
k_f_2.pack()
  
#ka na start the hear
t_1 = 2965
t_m_1 = Button(k_f_2,text=chr(2965)+" : line",command= lambda:charactor_change_loop(t_1),width=5,height=2,font=('bold')) 
t_m_1.pack(side=LEFT)

t_2 = 2969
t_m_2 = Button(k_f_2,text=chr(2969)+" : line",command= lambda:charactor_change_loop(t_2),width=5,height=2,font=('bold'))
t_m_2.pack(side=LEFT)

t_3 = 2970
t_m_3 = Button(k_f_2,text=chr(2970)+" : line",command= lambda:charactor_change_loop(t_3),width=5,height=2,font=('bold'))
t_m_3.pack(side=LEFT)

t_4 = 2974
t_m_4 = Button(k_f_2,text=chr(2974)+" : line",command= lambda:charactor_change_loop(t_4),width=5,height=2,font=('bold'))
t_m_4.pack(side=LEFT)

t_5 = 2975
t_m_5 = Button(k_f_2,text=chr(2975)+" : line",command= lambda:charactor_change_loop(t_5),width=5,height=2,font=('bold'))
t_m_5.pack(side=LEFT)

t_6 = 2979
t_m_6 = Button(k_f_2,text=chr(2979)+" : line",command= lambda:charactor_change_loop(t_6),width=5,height=2,font=('bold'))
t_m_6.pack(side=LEFT)

t_7 = 2980
t_m_7 = Button(k_f_2,text=chr(2980)+" : line",command= lambda:charactor_change_loop(t_7),width=5,height=2,font=('bold'))
t_m_7.pack(side=LEFT)

t_8 = 2984
t_m_8 = Button(k_f_2,text=chr(2984)+" : line",command= lambda:charactor_change_loop(t_8),width=5,height=2,font=('bold'))
t_m_8.pack(side=LEFT)

t_9 = 2985
t_m_9 = Button(k_f_2,text=chr(2985)+" : line",command= lambda:charactor_change_loop(t_9),width=5,height=2,font=('bold'))
t_m_9.pack(side=LEFT)

t_10 = 2986
t_m_10 = Button(k_f_2,text=chr(2986)+" : line",command= lambda:charactor_change_loop(t_10),width=5,height=2,font=('bold'))
t_m_10.pack(side=LEFT)

t_11 = 2990
t_m_11 = Button(k_f_2,text=chr(2990)+" : line",command= lambda:charactor_change_loop(t_11),width=5,height=2,font=('bold'))
t_m_11.pack(side=LEFT)

t_12 = 2991
t_m_12 = Button(k_f_2,text=chr(2991)+" : line",command= lambda:charactor_change_loop(t_12),width=5,height=2,font=('bold'))
t_m_12.pack(side=LEFT)

t_13 = 2992
t_m_13 = Button(k_f_2,text=chr(2992)+" : line",command= lambda:charactor_change_loop(t_13),width=5,height=2,font=('bold'))
t_m_13.pack(side=LEFT)

t_14 = 2993
t_m_14 = Button(k_f_2,text=chr(2993)+" : line",command= lambda:charactor_change_loop(t_14),width=5,height=2,font=('bold'))
t_m_14.pack(side=LEFT)

t_15 = 2994
t_m_15 = Button(k_f_2,text=chr(2994)+" : line",command= lambda:charactor_change_loop(t_15),width=5,height=2,font=('bold'))
t_m_15.pack(side=LEFT)

t_16 = 2995
t_m_16 = Button(k_f_2,text=chr(2995)+" : line",command= lambda:charactor_change_loop(t_16),width=5,height=2,font=('bold'))
t_m_16.pack(side=LEFT)

t_17 = 2996
t_m_17 = Button(k_f_2,text=chr(2996)+" : line",command= lambda:charactor_change_loop(t_17),width=5,height=2,font=('bold'))
t_m_17.pack(side=LEFT)

t_18 = 2997
t_m_18 = Button(k_f_2,text=chr(2997)+" : line",command= lambda:charactor_change_loop(t_18),width=5,height=2,font=('bold'))
t_m_18.pack(side=LEFT)

root_window.mainloop()
