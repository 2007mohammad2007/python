


from tkinter import *
import tkinter as tk
from tkinter import ttk , PhotoImage
from PIL import Image, ImageTk , ImageDraw
from urllib import request
from io import BytesIO
import threading
import csv
import Pmw
#--------------------------------------------------------------------
screen = Tk()
#======================
global setting , data , font_color , foreground_color , background_color , color , theme , error_color  
# def language_ar():
#         global language_data
#         language_data = 'تاريخ'
#         nb.tab(0, text=language_data)

# def language_en():
#         global language_data
#         language_data = 'data'
#         nb.tab(0, text=language_data)
#_____________________________________________________________________________________________________________
def light_color():
    global color 
    config(True)
def dark_color():
    global color
    config(False)
i = 1 
if i == 1 :
    background_color = '#CCCCCC'
    font_color = '#101010'
    foreground_color = '#6F6F6F'
    error_color = "#FF0000"
    i = i + 1    
def config(color_value):
    global color, background_color, font_color, foreground_color , setting , frl , frame_button , screen2
    color = color_value
    if color == True:
        background_color = '#CCCCCC'
        font_color = '#101010'
        foreground_color = '#6F6F6F'

    else:
        background_color = '#1F1F1F'
        font_color = '#EEEEEE'
        foreground_color = '#101010'
    screen2.destroy()
    screen2 = Frame(width='800' , height= '800' , bg=background_color )
    screen2.place(x=0,y=0)
    frl.destroy()
    frl = Frame(width=frame_width , height= '800' , bg=foreground_color )
    frl.place(x=0,y=0)
    frl.lift()
    frame_button = Button(frl , text = '=' , fg= font_color , bg = background_color , font= 20 ,width=3, height=1 , command=frame_en , bd=0)
    frame_button.place(x=5 , y=2)
    frame_en()
    frame_en()
    setting_button_def()
    setting_button_def()

if background_color == "#FF0000" or background_color == "#Ff0000" or background_color == "#ff0000" or background_color == "#fF0000" :
    error_color = "#000000"
else :
    error_color = "#FF0000"

#========================

#_______________________
def En():
    global color 
    config_language(True)

def Ar():
    global color
    config_language(False)

l = 1 
if l == 1 :
    lang = True
    title = "Calculator"
    form = "Form"
    to = "To"
    day = "Day"
    month = "Month"
    year = "Year"
    day_ = "Day         : "
    month_ ="Month      : "
    year_ = "Year        : "
    Total_day_ = "Total Day : "
    error_ = "❗INPUT ERROR❗"
    submit_ = "SUBMIT"
    color_app_ = "Color APP"
    dark_ = "Dark"
    light_ = "Light"
    Ar_ = "Ar"
    En_ = "En"
    lang_app_ = "Language APP"
    setting_ = "Setting"
    calculate_history = "Calculate History"
    k = "\\"
    background_theme = "Background Color"
    foreground_theme = "Foreground Color"
    font_theme = "Font Color"    
    i = i + 1    

def config_language(lang_value):
    global lang,  background_theme , foreground_theme , font_theme ,background_color,k,lang, color_app_, dark_ , light_ , Ar_ , En_ , lang_app_ , setting_ , calculate_history ,  font_color, foreground_color , setting , frl , frame_button , screen2 , title , form , to , day , day_ , month , month_ , year , year_ ,Total_day_ ,error_ ,submit_
    lang = lang_value
    if lang == True:
        title = "Calculator"
        form = "Form"
        to = "To"
        day = "Day"
        month = "Month"
        year = "Year"
        day_ = "Day         : "
        month_ ="Month      : "
        year_ = "Year        : "
        Total_day_ = "Total Day : "
        error_ = "❗INPUT ERROR❗"
        submit_ = "SUBMIT"
        color_app_ = "COLOR APP"
        dark_ = "Dark"
        light_ = "Light"
        Ar_ = "Ar"
        En_ = "En"
        lang_app_ = "Language App"
        setting_ = "Setting"
        calculate_history = "Calculate History"
        background_theme = "Background Color"
        foreground_theme = "Foreground Color"
        font_theme = "Font Color"
        k = "\\"

    else:
        title = "الة حاسبة"
        form = "من"
        to = "الى"
        day = "اليوم"
        month = "الشهر"
        year = "السنة"
        day_ = ":           اليوم"
        month_ =":          الشهر"
        year_ = ":           السنة"
        Total_day_ = ":   مجموع الايام"
        error_ = "❗خطأ بالمدخلات❗"
        submit_ = "تأكيد"
        color_app_ = "لون التطبيق"
        dark_ = "غامق"
        light_ = "فاتح"
        Ar_ = "عربي"
        En_ = "انجليزي"
        lang_app_ = "لغة التطبيق"
        setting_ = "                الاعدادات"
        calculate_history = "            حساب التاريخ"
        k = "/"
        background_theme = "لون الخلفية"
        foreground_theme = "لون المقدمة"
        font_theme = "   لون الخط"
    screen2.destroy()
    screen2 = Frame(width='800' , height= '800' , bg=background_color )
    screen2.place(x=0,y=0)
    frl.destroy()
    frl = Frame(width=frame_width , height= '800' , bg=foreground_color )
    frl.place(x=0,y=0)
    frl.lift()
    frame_button = Button(frl , text = '=' , fg= font_color , bg = background_color , font= 20 ,width=3, height=1 , command=frame_en , bd=0)
    frame_button.place(x=5 , y=2)
    frame_en()
    frame_en()
    setting_button_def()
    setting_button_def()


#=======================
screen.title(title)
window_width = 800
window_height = 790
window_top = 0
window_left= 500
#place and size window
screen.geometry(f"{window_width}x{window_height}+{window_left}+{window_top}")
width_size = False
height_size = False
#resizeable 
screen.resizable(width_size , height_size)
screen.config(bg=background_color)
#------------------------------
screen2 = Frame(width='800' , height= '800' , bg=background_color )
screen2.place(x=0,y=0)
#------------------------------
setting = None
data = None
#=================================
ll = 1
if ll == 1 :
    foreground_theme_y1 = 205
    foreground_theme_y2 = 200
    font_theme_y1 = 255
    font_theme_y2 = 250

    ll =+1
E = 1
if E == 1:
    error__ = ""
    E +=1 

def background_theme_def():
    global background_Theme_entry ,background_theme_error,theme, background_color , screen2 , frl , frame_button , error1__  , error__, foreground_theme , font_Theme_label , font_theme_y1 , foreground_theme_y1 , font_theme_y2 , foreground_theme_y2
    theme = background_Theme_entry.get()
    
    if len(theme) != 6 or theme.upper() == "YELLOW" :
            if theme.upper() == "RED" or theme == "احمر" or theme == "أحمر" :
                if error1__ == "" :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    background_color = f'#FF0000'
                    error__ = ""
                else :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    background_color = f'#FF0000'
                    error__ = ""
            elif theme.upper() == "BLUE" or theme == "أزرق" or theme == "ازرق" :
                if error1__ == "" :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    background_color = f'#0000FF'
                    error__ = ""
                else :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    background_color = f'#0000FF'
                    error__ = ""
            elif theme.upper() == "YELLOW" or theme == "اصفر" or theme == "أصفر" :
                if error1__ == "" :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    background_color = f'#FFFF00'
                    error__ = ""
                else :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    background_color = f'#FFFF00'
                    error__ = ""
            elif theme.upper() == "GREEN" or theme == "اخضر" or theme == "أخضر" :
                if error1__ == "" :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    background_color = f'#00FF00'
                    error__ = ""
                else :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    background_color = f'#00FF00'
                    error__ = ""
            elif theme.upper() == "BLACK" or theme == "أسود" or theme == "اسود" :
                if error1__ == "" :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    background_color = f'#000000'
                    error__ = ""
                else :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    background_color = f'#000000'
                    error__ = ""
            elif theme.upper() == "WHITE" or theme == "ابيض" or theme == "أبيض" :
                if error1__ == "" :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    background_color = f'#FFFFFF'
                    error__ = ""
                else :
                    foreground_theme_y1 = 205
                    foreground_theme_y2 = 200
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    background_color = f'#FFFFFF'
                    error__ = ""
            else:
                if error1__ == "" :
                    foreground_theme_y1 = 255
                    foreground_theme_y2 = 250
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    if lang == True :
                        error__ = "❗INPUT ERROR❗" 
                    else :
                        error__ = "❗خطا بالمدخلات❗" 
                else:
                    foreground_theme_y1 = 255
                    foreground_theme_y2 = 250
                    font_theme_y1 = 355
                    font_theme_y2 = 350
                    if lang == True :
                        error__ = "❗INPUT ERROR❗" 
                    else :
                        error__ = "❗خطا بالمدخلات❗" 


    else :
        if any(char in theme for char in "qwrtyuiopsgjhklzxnvm"):
            if error1__ == "":
                foreground_theme_y1 = 255
                foreground_theme_y2 = 250
                font_theme_y1 = 305
                font_theme_y2 = 300 
                if lang == True :
                    error__ = "❗INPUT ERROR❗" 
                else :
                    error__ = "❗خطا بالمدخلات❗" 
            else :
                foreground_theme_y1 = 255
                foreground_theme_y2 = 250
                font_theme_y1 = 355
                font_theme_y2 = 350 
        else :
            if error1__ == "" :
                foreground_theme_y1 = 205
                foreground_theme_y2 = 200
                font_theme_y1 = 255
                font_theme_y2 = 250
                background_color = f'#{theme}'
                error__ = ""
            else :
                foreground_theme_y1 = 205
                foreground_theme_y2 = 200
                font_theme_y1 = 305
                font_theme_y2 = 300
                background_color = f'#{theme}'
                error__ = ""


    screen2.destroy()
    screen2 = Frame(width='800' , height= '800' , bg=background_color )
    screen2.place(x=0,y=0)
    frl.destroy()
    frl = Frame(width=frame_width , height= '800' , bg=foreground_color )
    frl.place(x=0,y=0)
    frl.lift()
    frame_button = Button(frl , text = '=' , fg= font_color , bg = background_color , font= 20 ,width=3, height=1 , command=frame_en , bd=0)
    frame_button.place(x=5 , y=2)
    frame_en()
    frame_en()
    setting_button_def()
    setting_button_def()
#_______________
E1 = 1 
if E1 == 1:
    error1__ = ""
    E1 +=1
def foreground_theme_def():
    global foreground_Theme_entry ,foreground_theme_error,lang,background_color, foreground_color , screen2 , frl , frame_button , error1__  , error2__, foreground_theme , font_Theme_label , font_theme_y1 , foreground_theme_y1 , font_theme_y2 , foreground_theme_y2
    theme1 = foreground_Theme_entry.get()
     
    if len(theme1) != 6 or theme1.upper() == "YELLOW" :
        if theme1.upper() == "RED" or theme1 == "احمر" or theme1 == "أحمر" :
                if error__ == "" :
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    foreground_color = f'#FF0000'
                    error1__ = ""
                else :
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    foreground_color = f'#FF0000'
                    error1__ = ""
        elif theme1.upper() == "BLUE" or theme1 == "أزرق" or theme1 == "ازرق" :
                if error__ == "" :
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    foreground_color = f'#0000FF'
                    error1__ = ""
                else :
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    foreground_color = f'#0000FF'
                    error1__ = ""
        elif theme1.upper() == "YELLOW" or theme1 == "اصفر" or theme1 == "أصفر" :
                if error__ == "" :
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    foreground_color = f'#FFFF00'
                    error1__ = ""
                else :
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    foreground_color = f'#FFFF00'
                    error1__ = ""
        elif theme1.upper() == "GREEN" or theme1 == "اخضر" or theme1 == "أخضر" :
                if error__ == "" :
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    foreground_color = f'#00FF00'
                    error1__ = ""
                else :
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    foreground_color = f'#00FF00'
                    error1__ = ""
        elif theme1.upper() == "BLACK" or theme1 == "أسود" or theme1 == "اسود" :
                if error__ == "" :
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    foreground_color = f'#000000'
                    error1__ = ""
                else :
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    foreground_color = f'#000000'
                    error1__ = ""
        elif theme1.upper() == "WHITE" or theme1 == "ابيض" or theme1 == "أبيض" :
                if error__ == "" :
                    font_theme_y1 = 255
                    font_theme_y2 = 250
                    foreground_color = f'#FFFFFF'
                    error1__ = ""
                else :
                    font_theme_y1 = 305
                    font_theme_y2 = 300
                    foreground_color = f'#FFFFFF'
                    error1__ = ""
        else:
                if error__== "":
                    font_theme_y1 = 305
                    font_theme_y2 = 300 
                    if lang == True :
                        error1__ = "❗INPUT ERROR❗" 
                    else :
                        error1__ = "❗خطا بالمدخلات❗" 
                else :
                    font_theme_y1 = 355
                    font_theme_y2 = 350 
                    if lang == True :
                        error1__ = "❗INPUT ERROR❗" 
                    else : 
                        error1__ = "❗خطا بالمدخلات❗"              

    else :
        if any(char in theme1 for char in "qwrtyuiopsgjhklzxnvm"):
            if error__== "":
                font_theme_y1 = 305
                font_theme_y2 = 300 
                if lang == True :
                    error1__ = "❗INPUT ERROR❗" 
                else :
                    error1__ = "❗خطا بالمدخلات❗" 
            else :
                font_theme_y1 = 355
                font_theme_y2 = 350 
                if lang == True :
                    error1__ = "❗INPUT ERROR❗" 
                else :
                    error1__ = "❗خطا بالمدخلات❗" 
        else :         
            font_theme_y1 = 255
            font_theme_y2 = 250
            foreground_color = f'#{theme1}'
            error1__ = ""

    screen2.destroy()
    screen2 = Frame(width='800' , height= '800' , bg=background_color )
    screen2.place(x=0,y=0)
    frl.destroy()
    frl = Frame(width=frame_width , height= '800' , bg=foreground_color )
    frl.place(x=0,y=0)
    frl.lift()
    frame_button = Button(frl , text = '=' , fg= font_color , bg = background_color , font= 20 ,width=3, height=1 , command=frame_en , bd=0)
    frame_button.place(x=5 , y=2)
    frame_en()
    frame_en()
    setting_button_def()
    setting_button_def()
    
#_____________________
E2 = 1 
if E2 == 1:
    error2__ = ""
def font_theme_def():
    global font_Theme_entry ,font_theme_error, font_color , screen2 , frl , frame_button   , error2__, font_theme , font_Theme_label , font_theme_y1 , foreground_theme_y1 , font_theme_y2 , foreground_theme_y2
    theme2 = font_Theme_entry.get()
    
    if len(theme2) != 6 or theme2.upper() == "YELLOW":
        if theme2.upper() == "RED" or theme2 == "احمر" or theme2 == "أحمر" :
                    font_color = f'#FF0000'
                    error2__ = ""
        elif theme2.upper() == "BLUE" or theme2 == "أزرق" or theme2 == "ازرق" :
                    font_color = f'#0000FF'
                    error2__ = ""
        elif theme2.upper() == "YELLOW" or theme2 == "اصفر" or theme2 == "أصفر" :
                    font_color = f'#FFFF00'
                    error2__ = ""
        elif theme2.upper() == "GREEN" or theme2 == "اخضر" or theme2 == "أخضر" :
                    font_color = f'#00FF00'
                    error2__ = ""
        elif theme2.upper() == "BLACK" or theme2 == "أسود" or theme2 == "اسود" :
                    font_color = f'#000000'
                    error2__ = ""
        elif theme2.upper() == "WHITE" or theme2 == "ابيض" or theme2 == "أبيض" :
                    font_color = f'#FFFFFF'
                    error2__ = ""
        else:        
            if lang == True :
                error2__ = "❗INPUT ERROR❗" 
            else :
                error2__ = "❗خطا بالمدخلات❗"   

    else :
        if any(char in theme2 for char in "qwrtyuiopsgjhklzxnvm"):
            if lang == True :
                error1__ = "❗INPUT ERROR❗" 
            else :
                error1__ = "❗خطا بالمدخلات❗" 
        else:
            font_color = f'#{theme2}'
            error2__ = ""

    screen2.destroy()
    screen2 = Frame(width='800' , height= '800' , bg=background_color )
    screen2.place(x=0,y=0)
    frl.destroy()
    frl = Frame(width=frame_width , height= '800' , bg=foreground_color )
    frl.place(x=0,y=0)
    frl.lift()
    frame_button = Button(frl , text = '=' , fg= font_color , bg = background_color , font= 20 ,width=3, height=1 , command=frame_en , bd=0)
    frame_button.place(x=5 , y=2)
    frame_en()
    frame_en()
    setting_button_def()
    setting_button_def()
    
                
#----------------------------------
dfd = True
def data_button_def():
    global data_button , color, background_color, font_color, foreground_color, submit2 , data , check_error , label_first_day , label_first_form , label_first_month , label_first_year , label_second_day , label_second_month ,  label_second_to , label_second_year , first_label , first_label2 , second_label , second_label2,setting , dfd ,  data , entry_First_day , entry_First_month , entry_First_year ,error , First_month , First_year , entry_second_day , entry_second_month , entry_second_year , second_month , second_year , Av_year, Av_month , Av_day , Total_day , day_number , days_number , year_number , month_number , days_label , day_label , month_label , year_label
    if dfd == True:
        data = Frame( screen , width=window_width , height=window_height , bg=background_color)
        data.place(x=50,y=0)
        frl.lift()
        if setting :
            setting.destroy()
        dfd = False
#============================================================================================================
        def time_calculation():
            global Av_day , Av_month , Av_year , RY , ty , tm , Total_day
            day1= int(entry_First_day.get())
            day2= int(entry_second_day.get())
            month1 = int(entry_First_month.get())
            month2 = int(entry_second_month.get())
            year1 = int(entry_First_year.get())
            year2 = int(entry_second_year.get())
            Av_day = 0
            Av_year = 0
            Av_month = 0
            if year1 > year2  :
                if day1 >= day2 :
                    Av_day = day1 - day2
                else :
                    if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12 :
                        day1 = day1 + 31
                    elif month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11 :
                        day1 = day1 + 30
                    elif month1 == 2 and year1 % 4 ==0 :
                        day1 = day1 + 29
                    elif month1 == 2 and year1 % 4 != 0 :
                        day1 = day1 + 28
                    month1 = month1 - 1 
                    Av_day = day1 - day2
                if month1 >= month2:
                    Av_month = month1 - month2
                else :
                    month1 = month1 + 12
                    year1 = year1 - 1
                    Av_month = month1 - month2
                Av_year = year1 - year2
            elif year1 < year2  :
                if day2 >= day1 :
                    Av_day = day2 - day1
                else :
                    if month2 == 1 or month2 == 3 or month2 == 5 or month2 == 7 or month2 == 8 or month2 == 10 or month2 == 12 :
                        day2 = day2 + 31
                    elif month2 == 4 or month2 == 6 or month2 == 9 or month2 == 11 :
                        day2 = day2 + 30
                    elif month2 == 2 and year2 % 4 ==0 :
                        day2 = day2 + 29
                    elif month2 == 2 and year2 % 4 != 0 :
                        day2 = day2 + 28
                    month2 = month2 - 1 
                    Av_day = day2 - day1
                if month2 >= month1:
                    Av_month = month2 - month1
                else :
                    month2 = month2 + 12
                    year2 = year2 - 1
                    Av_month = month2 - month1
                Av_year = year2 - year1               
            else :
                if month1 > month2 :
                    if day2 > day1 :
                        if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12 :
                            day1 = day1 + 31
                        elif month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11 :
                            day1 = day1 + 30
                        elif month1 == 2 and year1 % 4 ==0 :
                            day1 = day1 + 29
                        elif month1 == 2 and year1 % 4 != 0 :
                            day1 = day1 + 28
                        month1 = month1 -1
                        Av_day = day1 - day2
                    else :
                        Av_day = day1 - day2
                    Av_month = month1 - month2
                elif month1 < month2:
                    if day2 < day1 :
                        if month2 == 1 or month2 == 3 or month2 == 5 or month2 == 7 or month2 == 8 or month2 == 10 or month2 == 12 :
                            day2 = day2 + 31
                        elif month2 == 4 or month2 == 6 or month2 == 9 or month2 == 11 :
                            day2 = day2 + 30
                        elif month2 == 2 and year2 % 4 ==0 :
                            day2 = day2 + 29
                        elif month2 == 2 and year2 % 4 != 0 :
                            day2 = day2 + 28
                        month2 = month2 - 1 
                        Av_day = day2 - day1                    
                    else : 
                        Av_day = day2 - day1
                    Av_month = month2 - month1
                else :
                    if day1 > day2 :
                        Av_day = day1 - day2
                    else :
                        Av_day = day2 - day1
                Av_year = 0
            RY = float(Av_year / 4)
            ty = Av_year * 365
            tm = float(Av_month/12) * 365
            Total_day = int(Av_day + ty + RY + tm)
#============================================================================================================
        def validate_entry():
            new_value = entry_First_day.get()
            
            return new_value.isdigit()
#============================================================================================================
        def validate_entry2():
            new_value2 = entry_second_day.get()
            
            return new_value2.isdigit()
#============================================================================================================ 
        def validate_entry():
            global First_month , First_year , error
  
            First_day = entry_First_day.get()
            First_month = entry_First_month.get()
            First_year = entry_First_year.get()            
            if len(First_day) > 0 and First_day.isdigit() and len(First_month) > 0 and len(First_year)> 0 and First_month.isdigit() and First_year.isdigit() :
                if int(First_month) == 1 or int(First_month) == 3 or int(First_month) == 5  or int(First_month) == 7  or int(First_month) == 8 or int(First_month) == 10 or int(First_month) == 12 :
                    if int(First_day) > 31 or int(First_day) < 1:
                        if int(First_day) > 31 :
                            big = '31'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, big)
                        
                        elif int(First_day) < 1:
                            small = '1'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, small)                            
                            
                            
                    else:
                        entry_First_day.delete(2, tk.END)
                        
                        
                elif int(First_month) == 4 or int(First_month) == 6 or int(First_month) == 9  or int(First_month) == 11 :
                    if int(First_day) > 30 or int(First_day) < 1:
                        if int(First_day) > 30 :
                            big = '30'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, big)
                        
                        elif int(First_day) < 1:
                            small = '1'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, small)                            
                        
                            
                    else:
                        entry_First_day.delete(2, tk.END)
                        

                elif int(First_month) == 2 and int(First_year) % 4 !=0:
                    if int(First_day) > 28 or int(First_day) < 1:
                        if int(First_day) > 28 :
                            big = '28'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, big)
                        
                        elif int(First_day) < 1:
                            small = '1'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, small)                            
                            
                            
                    else:
                        entry_First_day.delete(2, tk.END)
                         

                elif int(First_month) == 2 and int(First_year) % 4 == 0:
                    if int(First_day) > 29 or int(First_day) < 1:
                        if int(First_day) > 29 :
                            big = '29'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, big)
                        
                        elif int(First_day) < 1:
                            small = '1'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, small)                            
                            
                            
                    else:
                        entry_First_day.delete(2, tk.END)
                              
                else :
                    if int(First_day) > 31 or int(First_day) < 1:
                        if int(First_day) > 31 :
                            big = '31'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, big)
                        
                        elif int(First_day) < 1:
                            small = '1'
                            entry_First_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_day.insert(0, small)                            
                            
                            
                    else:
                        entry_First_day.delete(2, tk.END)
                                                                                   

            if len(First_month) > 0 and First_month.isdigit():
                if int(First_month) > 12 or int(First_month) < 1:
                        if int(First_month) > 12 :
                            big = '12'
                            entry_First_month.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_month.insert(0, big)
                        
                        elif int(First_month) < 1:
                            small = '1'
                            entry_First_month.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_month.insert(0, small)                            
                            
                            
                else:
                    entry_First_month.delete(2, tk.END)
                    

            if len(First_year) > 0 and First_year.isdigit():
                if  int(First_year) < 1:
                        if int(First_year) < 1:
                            small = '1'
                            entry_First_year.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_First_year.insert(0, small)                            
                            
                            
                else:
                    entry_First_year.delete(4, tk.END)
            validate_entry2()
#============================================================================================================
        def submit():
                global error , entry_First_day , entry_First_month , entry_First_year , entry_second_day , entry_second_month , entry_second_year , day_number , days_number , year_number , month_number
                error = False
                
                try :
                    entry_value_day = int(entry_First_day.get())
                    entry_value_day / 1 
                    entry_value_month = int(entry_First_month.get())
                    entry_value_month / 1  
                    entry_value_year = int(entry_First_year.get())
                    entry_value_year / 1 
                    entry_value_day2 = int(entry_second_day.get())
                    entry_value_day2 / 1 
                    entry_value_month2 = int(entry_second_month.get())
                    entry_value_month2 / 1  
                    entry_value_year2 = int(entry_second_year.get())
                    entry_value_year2 / 1                  

                    
                except:
                    error = True    
                if error == True  :
                    check_error.config(text=error_)
                    day_number.config(text='')
                    days_number.config(text='')
                    month_number.config(text='')
                    year_number.config(text='')
                    day_label.config(text='')
                    days_label.config(text='')
                    month_label.config(text='')
                    year_label.config(text='')
                else :
                    time_calculation()
                    check_error.config(text='') 
                    day_number.config(text=f'{Av_day}')
                    days_number.config(text=f'{Total_day}')
                    month_number.config(text=f'{Av_month}')
                    year_number.config(text=f'{Av_year}')
                    day_label.config(text=day_)
                    days_label.config(text=Total_day_)
                    month_label.config(text=month_)
                    year_label.config(text=year_)                  
#============================================================================================================
        def validate_entry2():
            global  second_year , second_month ,entry_First_day , lang
            second_day = entry_second_day.get()
            second_month = entry_second_month.get()
            second_year = entry_second_year.get()            
            if len(second_day) > 0 and second_day.isdigit() and len(second_month) > 0 and len(second_year)> 0 and second_month.isdigit() and second_year.isdigit() :
                if int(second_month) == 1 or int(second_month) == 3 or int(second_month) == 5  or int(second_month) == 7  or int(second_month) == 8 or int(second_month) == 10 or int(second_month) == 12 :
                    if int(second_day) > 31 or int(second_day) < 1:
                        if int(second_day) > 31 :
                            big = '31'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, big)
                        
                        elif int(second_day) < 1:
                            small = '1'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, small)                            
            
                    else:
                        entry_second_day.delete(2, tk.END)
                        
                elif int(second_month) == 4 or int(second_month) == 6 or int(second_month) == 9  or int(second_month) == 11 :
                    if int(second_day) > 30 or int(second_day) < 1:
                        if int(second_day) > 30 :
                            big = '30'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, big)
                        
                        elif int(second_day) < 1:
                            small = '1'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, small)                            
                    else:
                        entry_second_day.delete(2, tk.END)

                elif int(second_month) == 2 and int(second_year) % 4 !=0:
                    if int(second_day) > 28 or int(second_day) < 1:
                        if int(second_day) > 28 :
                            big = '28'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, big)
                        
                        elif int(second_day) < 1:
                            small = '1'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, small)                            
            
                    else:
                        entry_second_day.delete(2, tk.END)   

                elif int(second_month) == 2 and int(second_year) % 4 == 0:
                    if int(second_day) > 29 or int(second_day) < 1:
                        if int(second_day) > 29 :
                            big = '29'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, big)
                        
                        elif int(second_day) < 1:
                            small = '1'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, small)                            
            
                    else:
                        entry_second_day.delete(2, tk.END) 
                else :
                    if int(second_day) > 31 or int(second_day) < 1:
                        if int(second_day) > 31 :
                            big = '31'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, big)
                        
                        elif int(second_day) < 1:
                            small = '1'
                            entry_second_day.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_day.insert(0, small)                                                       


            if len(second_month) > 0 and second_month.isdigit():
                if int(second_month) > 12 or int(second_month) < 1:
                        if int(second_month) > 12 :
                            big = '12'
                            entry_second_month.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_month.insert(0, big)
                        
                        elif int(second_month) < 1:
                            small = '1'
                            entry_second_month.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_month.insert(0, small)                            
            
                else:
                    entry_second_month.delete(2, tk.END)

            if len(second_year) > 0 and second_year.isdigit():
                if  int(second_year) < 1:
                        if int(second_year) > 31 :
                            big = '31'
                            entry_second_year.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_year.insert(0, big)
                        
                        elif int(second_year) < 1:
                            small = '1'
                            entry_second_year.delete(0, tk.END)  # حذف القيمة الحالية
                            entry_second_year.insert(0, small)                            
            
                else:
                    entry_second_year.delete(4, tk.END)
            submit()
#============================================================================================================
        if lang == True :
            first_label = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg=font_color)
            first_label.place(x=290 , y= 100)

            first_label2 = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg=font_color)
            first_label2.place(x=370 , y= 100)

            label_first_form = Label(data ,  width=30 , height=2 , text=form , bg = background_color, bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_form.place(x=50, y=20)

            label_first_day = Label(data ,  width=10 , height=1 , text=day , bg =background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_day.place(x=220, y=70)

            label_first_year = Label(data ,  width=10 , height=1 , text=year , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_year.place(x=380, y=70)

            label_first_month = Label(data ,  width=10 , height=1 , text=month , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_month.place(x=300, y=70)

    #---------------------------------------------------------------
            label_second_to = Label(data ,  width=30 , height=2 , text=to , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_to.place(x=50, y=120)
            
            label_second_day = Label(data ,  width=10 , height=1 , text=day , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_day.place(x=220, y=170)

            label_second_year = Label(data ,  width=10 , height=1 , text=year , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_year.place(x=380, y=170)

            label_second_month = Label(data ,  width=10 , height=1 , text=month , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_month.place(x=300, y=170)

    #========================================================
            entry_First_day = Entry(data ,width=4 ,font=60  , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_First_day.place(x=250, y=100)
            entry_First_day.lift()




            entry_First_month = Entry(data ,width=4 ,font=60 , bg =foreground_color , fg = font_color , insertbackground=font_color , bd = 0 )
            entry_First_month.place(x=330, y=100)
            entry_First_month.lift()
            

            entry_First_year = Entry(data ,width=5 ,font=60 , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_First_year.place(x=410, y=100)
            entry_First_year.lift()
    #---------------------------------------------------
            second_label = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg= font_color)
            second_label.place(x=290 , y= 200)

            second_label2 = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg= font_color)
            second_label2.place(x=370 , y= 200)

            entry_second_day = Entry(data ,width=4 ,font=60  , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_second_day.place(x=250, y=200)
            entry_second_day.lift()



            entry_second_month = Entry(data ,width=4 ,font=60 , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_second_month.place(x=330, y=200)
            entry_second_month.lift()

            entry_second_year = Entry(data ,width=5 ,font=60 , bg =foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_second_year.place(x=410, y=200)
            entry_second_year.lift()      

            submit2 = Button(data , width=19 , height=1 , command=validate_entry  , bg = foreground_color, fg = font_color , text=submit_ , font= 60)
            submit2.place(x = 250 , y = 300)

            check_error = Label(data ,  width=19 , height=1 , text='' , bg = background_color , bd= 0 , fg = error_color , font= 60)
            check_error.place(x = 250 , y = 360)
    #==================================================================================================================================
            day_label = Label(data ,width=10 , height=1 , text=f'' , bg = background_color, bd= 0 , fg = font_color , font= 60 )
            day_label.place(x=250 , y = 480)

            month_label = Label(data ,width=10 , height=1 , text=f'' , bg =background_color , bd= 0 , fg = font_color , font= 60 )
            month_label.place(x=250 , y = 440)

            year_label = Label(data ,width=10 , height=1 , text=f'' , bg =background_color , bd= 0 , fg = font_color , font= 60 )
            year_label.place(x=250 , y = 400)
            
            days_label = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            days_label.place(x=250 , y = 520)

            day_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            day_number.place(x=400 , y = 480)

            month_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            month_number.place(x=400 , y = 440)

            year_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            year_number.place(x=400 , y = 400)
            
            days_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            days_number.place(x=400 , y = 520)
        else:
            first_label = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg=font_color)
            first_label.place(x=190 , y= 100)

            first_label2 = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg=font_color)
            first_label2.place(x=115 , y= 100)

            label_first_form = Label(data ,  width=30 , height=2 , text=form , bg = background_color, bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_form.place(x=130, y=20)

            label_first_day = Label(data ,  width=10 , height=1 , text=day , bg =background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_day.place(x=200, y=70)

            label_first_year = Label(data ,  width=10 , height=1 , text=year , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_year.place(x=40, y=70)

            label_first_month = Label(data ,  width=10 , height=1 , text=month , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_first_month.place(x=120, y=70)

    #---------------------------------------------------------------
            label_second_to = Label(data ,  width=30 , height=2 , text=to , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_to.place(x=130, y=120)
            
            label_second_day = Label(data ,  width=10 , height=1 , text=day , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_day.place(x=200, y=170)

            label_second_year = Label(data ,  width=10 , height=1 , text=year , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_year.place(x=40, y=170)

            label_second_month = Label(data ,  width=10 , height=1 , text=month , bg = background_color , bd= 0 , fg = font_color , font= 60 , justify='left')
            label_second_month.place(x=120, y=170)

    #========================================================
            entry_First_day = Entry(data ,width=4 ,font=60  , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_First_day.place(x=230, y=100)
            entry_First_day.lift()




            entry_First_month = Entry(data ,width=4 ,font=60 , bg =foreground_color , fg = font_color , insertbackground=font_color , bd = 0 )
            entry_First_month.place(x=150, y=100)
            entry_First_month.lift()
            

            entry_First_year = Entry(data ,width=5 ,font=60 , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_First_year.place(x=70, y=100)
            entry_First_year.lift()
    #---------------------------------------------------
            second_label = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg= font_color)
            second_label.place(x=190 , y= 200)

            second_label2 = Label(data , text=k , font=("Arial", 16) , width=4 , bd=0 , bg=background_color , fg= font_color)
            second_label2.place(x=115 , y= 200)

            entry_second_day = Entry(data ,width=4 ,font=60  , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_second_day.place(x=230, y=200)
            entry_second_day.lift()



            entry_second_month = Entry(data ,width=4 ,font=60 , bg = foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_second_month.place(x=150, y=200)
            entry_second_month.lift()

            entry_second_year = Entry(data ,width=5 ,font=60 , bg =foreground_color , fg = font_color , insertbackground=font_color , bd = 0)
            entry_second_year.place(x=70, y=200)
            entry_second_year.lift()      

            submit2 = Button(data , width=19 , height=1 , command=validate_entry  , bg = foreground_color, fg = font_color , text=submit_ , font= 60)
            submit2.place(x = 70 , y = 300)

            check_error = Label(data ,  width=19 , height=1 , text='' , bg = background_color , bd= 0 , fg = error_color , font= 60)
            check_error.place(x = 70 , y = 360)
    #==================================================================================================================================
            day_label = Label(data ,width=10 , height=1 , text=f'' , bg = background_color, bd= 0 , fg = font_color , font= 60 )
            day_label.place(x=200 , y = 480)

            month_label = Label(data ,width=10 , height=1 , text=f'' , bg =background_color , bd= 0 , fg = font_color , font= 60 )
            month_label.place(x=200 , y = 440)

            year_label = Label(data ,width=10 , height=1 , text=f'' , bg =background_color , bd= 0 , fg = font_color , font= 60 )
            year_label.place(x=200 , y = 400)
            
            days_label = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            days_label.place(x=200 , y = 520)

            day_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            day_number.place(x=30 , y = 480)

            month_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            month_number.place(x=30 , y = 440)

            year_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            year_number.place(x=30 , y = 400)
            
            days_number = Label(data ,width=10 , height=1 , text=f'' , bg = background_color , bd= 0 , fg = font_color , font= 60 )
            days_number.place(x=30 , y = 520)            
#______________________________________
    elif dfd == False:
        data.destroy()
        dfd = True
#----------------------------------
sb = True 
def setting_button_def():
    global sb , setting , error1__ ,background_theme_error , error2__ ,foreground_Theme_entry , error_color , font_Theme_entry , foreground_theme_error  , font_theme_error , font_theme_y1 , foreground_theme_y1 , foreground_theme_y2 , font_theme_y2 , data , dfd , font_color  , foreground_color , background_color , color , lang , background_Theme_entry , font_Theme_label 
    if sb== True:
        setting = Frame( screen , width=window_width , height=window_height , bg=background_color)
        setting.place(x=50,y=0)
        frl.lift()
        if data :
            data.destroy()
        sb = False
#---------------------------
#                 background_color = '#EEEEEE'
#                 font_color = '#101010'
#                 foreground_color = '#4F4F4F'
#                 background_color = '#1F1F1F'
#                 font_color = '#EEEEEE'
#                 foreground_color = '#101010'
#=============================================
        if lang == True :
            background_theme_error = Label(setting ,  width=19 , height=1 , text=error__ , bg = background_color , bd= 0 , fg = error_color , font= 60)
            background_theme_error.place(x = 300 , y = 200)
            foreground_theme_error = Label(setting ,  width=19 , height=1 , text=error1__ , bg = background_color , bd= 0 , fg = error_color , font= 60)
            foreground_theme_error.place(x = 300 , y = foreground_theme_y2+50)
            font_theme_error = Label(setting ,  width=19 , height=1 , text=error2__, bg = background_color , bd= 0 , fg = error_color , font= 60)
            font_theme_error.place(x = 300 , y = font_theme_y2+50)
            #==========================
            dark_button = Button(setting , text = light_ , fg= font_color , bg = foreground_color , font= 20 ,width=4, height=1 ,command=light_color  , bd=0)
            dark_button.place( x= 573 , y = 50 )
            light_button = Button(setting , text = dark_ , fg= font_color , bg = foreground_color, font= 20 ,width=4, height=1 , command=dark_color , bd=0)
            light_button.place( x= 627 , y = 50 )
            label_dark_light = Label(setting , text=color_app_ , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            label_dark_light.place( x= 200 , y = 55 )
            #======================================
            Ar_button = Button(setting , text = Ar_ , fg= font_color , bg = foreground_color , font= 20 ,width=5, height=1 ,command=Ar  , bd=0)
            Ar_button.place( x= 570 , y = 100 )
            En_button = Button(setting , text = En_ , fg= font_color , bg = foreground_color, font= 20 ,width=5, height=1 , command=En , bd=0)
            En_button.place( x= 635 , y = 100 )
            label_Ar_En = Label(setting , text=lang_app_ , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            label_Ar_En.place( x= 200 , y = 105 )
            #======================================
            background_Theme_label = Label(setting , text=background_theme , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            background_Theme_label.place( x= 200 , y = 155)
            background_Theme_entry = Entry(setting ,width=7 ,font=60  , bg = foreground_color  , fg = font_color , insertbackground=font_color , bd = 0)
            background_Theme_entry.place(x = 500 , y = 155 ) 
            background_Theme_submit = Button(setting , text = submit_ , fg= font_color , bg = foreground_color , font= 10 ,width=10 ,command=background_theme_def  , bd=0)
            background_Theme_submit.place(x = 600 , y = 150 ) 
            #======================================
            foreground_Theme_label = Label(setting , text=foreground_theme , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            foreground_Theme_label.place( x= 200 , y = foreground_theme_y1)
            foreground_Theme_entry = Entry(setting ,width=7 ,font=60  , bg = foreground_color  , fg = font_color , insertbackground=font_color , bd = 0)
            foreground_Theme_entry.place(x = 500 , y = foreground_theme_y1 ) 
            foreground_Theme_submit = Button(setting , text = submit_ , fg= font_color , bg = foreground_color , font= 10 ,width=10 ,command=foreground_theme_def  , bd=0)
            foreground_Theme_submit.place(x = 600 , y = foreground_theme_y2 )
            #======================================
            font_Theme_label = Label(setting , text=font_theme , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            font_Theme_label.place( x= 200 , y = font_theme_y1)
            font_Theme_entry = Entry(setting ,width=7 ,font=60  , bg = foreground_color  , fg = font_color , insertbackground=font_color , bd = 0)
            font_Theme_entry.place(x = 500 , y = font_theme_y1 ) 
            font_Theme_submit = Button(setting , text = submit_ , fg= font_color , bg = foreground_color , font= 10 ,width=10 ,command=font_theme_def  , bd=0)
            font_Theme_submit.place(x = 600 , y = font_theme_y2 )        
        else :
            background_theme_error = Label(setting ,  width=19 , height=1 , text=error__ , bg = background_color , bd= 0 , fg = error_color , font= 60)
            background_theme_error.place(x = 300 , y = 200)
            foreground_theme_error = Label(setting ,  width=19 , height=1 , text=error1__ , bg = background_color , bd= 0 , fg = error_color , font= 60)
            foreground_theme_error.place(x = 300 , y = foreground_theme_y2+50)
            font_theme_error = Label(setting ,  width=19 , height=1 , text=error2__, bg = background_color , bd= 0 , fg = error_color , font= 60)
            font_theme_error.place(x = 300 , y = font_theme_y2+50)
            #============================================
            dark_button = Button(setting , text = light_ , fg= font_color , bg = foreground_color , font= 20 ,width=4, height=1 ,command=light_color  , bd=0)
            dark_button.place( x= 104 , y = 50 )
            light_button = Button(setting , text = dark_ , fg= font_color , bg = foreground_color, font= 20 ,width=4, height=1 , command=dark_color , bd=0)
            light_button.place( x= 50 , y = 50 )
            label_dark_light = Label(setting , text=color_app_ , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            label_dark_light.place( x= 400 , y = 55 )
            #======================================
            Ar_button = Button(setting , text = Ar_ , fg= font_color , bg = foreground_color , font= 20 ,width=5, height=1 ,command=Ar  , bd=0)
            Ar_button.place( x= 115 , y = 100 )
            En_button = Button(setting , text = En_ , fg= font_color , bg = foreground_color, font= 20 ,width=5, height=1 , command=En , bd=0)
            En_button.place( x= 50 , y = 100 )
            label_Ar_En = Label(setting , text=lang_app_ , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            label_Ar_En.place( x= 400 , y = 105 )  
            #======================================
            background_Theme_label = Label(setting , text=background_theme , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            background_Theme_label.place( x= 400 , y = 155)
            background_Theme_entry = Entry(setting ,width=7 ,font=60  , bg = foreground_color  , fg = font_color , insertbackground=font_color , bd = 0)
            background_Theme_entry.place(x = 200 , y = 155 ) 
            background_Theme_submit = Button(setting , text = submit_ , fg= font_color , bg = foreground_color , font= 10 ,width=10 ,command=background_theme_def  , bd=0)
            background_Theme_submit.place(x = 50 , y = 150 )
            #======================================
            foreground_Theme_label = Label(setting , text=foreground_theme , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            foreground_Theme_label.place( x= 400 , y = foreground_theme_y1)
            foreground_Theme_entry = Entry(setting ,width=7 ,font=60  , bg = foreground_color  , fg = font_color , insertbackground=font_color , bd = 0)
            foreground_Theme_entry.place(x = 200 , y = foreground_theme_y1 ) 
            foreground_Theme_submit = Button(setting , text = submit_ , fg= font_color , bg = foreground_color , font= 10 ,width=10 ,command=foreground_theme_def  , bd=0)
            foreground_Theme_submit.place(x = 50 , y = foreground_theme_y2 )
            #======================================
            font_Theme_label = Label(setting , text=font_theme , font=("Arial", 16)  , bd=0 , bg=background_color , fg=font_color)
            font_Theme_label.place( x= 400 , y = font_theme_y1)
            font_Theme_entry = Entry(setting ,width=7 ,font=60  , bg = foreground_color  , fg = font_color , insertbackground=font_color , bd = 0)
            font_Theme_entry.place(x = 200 , y = font_theme_y1 ) 
            font_Theme_submit = Button(setting , text = submit_ , fg= font_color , bg = foreground_color , font= 10 ,width=10 ,command=font_theme_def  , bd=0)
            font_Theme_submit.place(x = 50 , y = font_theme_y2 )   

    elif sb == False:
        setting.destroy()
        sb = True      
#=================================
fr = True
def frame_en():
    global frl , fr , data_button , setting_button , lang
    if lang == True:
        if fr == True:
            fr = False
            frl.config(width=200)
            data_button = Button(frl, text = calculate_history , fg= font_color , bg = background_color , font= 15 ,width=15, height=1 , anchor='w' , command=data_button_def ,bd=0)
            data_button.place(x=5 , y=60)
            setting_button = Button(frl, text = setting_ , fg= font_color , bg = background_color , font= 15 ,width=15, height=1 , anchor='w', command=setting_button_def ,bd=0)
            setting_button.place(x=5 , y=650)
            frl.lift()
        elif fr == False :
            frl.config(width=50)
            fr = True
            if data_button :
                data_button.destroy()
            if setting_button :
                setting_button.destroy()
            frl.lift()
    else :
        if fr == True:
            fr = False
            frl.config(width=200)
            frl.place(x=600 , y=0)
            data_button = Button(frl, text = calculate_history , fg= font_color , bg = background_color , font= 15 ,width=15, height=1 , anchor='w' , command=data_button_def ,bd=0)
            data_button.place(x=15 , y=60)
            setting_button = Button(frl, text = setting_ , fg= font_color , bg = background_color , font= 15 ,width=15, height=1 , anchor='w', command=setting_button_def ,bd=0)
            setting_button.place(x=15 , y=650)
            frame_button.place(x=145 , y=2)
            frl.lift()
        elif fr == False :
            frl.config(width=50)
            frl.place(x=750 , y = 0 )
            fr = True
            if data_button :
                data_button.destroy()
            if setting_button :
                setting_button.destroy()
            frame_button.place(x=5 , y=2)
            frl.lift()       

#-----------------------------------------
frame_width = 50
frl = Frame(width=frame_width , height= '800' , bg=foreground_color )
frl.place(x=0,y=0)
frl.lift()
frame_button = Button(frl , text = '=' , fg= font_color , bg = background_color , font= 20 ,width=3, height=1 , command=frame_en , bd=0)
frame_button.place(x=5 , y=2)



screen.mainloop()

