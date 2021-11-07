import seaborn as sns
import matplotlib
import matplotlib.pyplot as py
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.cm as cm
matplotlib.use("TkAgg")
from matplotlib.colors import Normalize
from datetime import datetime
from tkinter import *
from tkinter import Label
import pandas as pd
import numpy as np
import re
import calendar
import PIL
from PIL import ImageTk, Image
from tkcalendar import Calendar,DateEntry
from collections import OrderedDict
from tkinter import Frame
from textblob import TextBlob as tb
import tkinter.messagebox as tm
from sklearn import preprocessing 
from sklearn.metrics import accuracy_score 
from sklearn.tree import DecisionTreeClassifier
import openpyxl
from openpyxl import *
import xlrd
import xlsxwriter
import io
import os
import path
import numpy as np
import math
import random
import seaborn as sns
from xlutils.copy import copy
from string import ascii_letters 
from tkinter.filedialog import asksaveasfile  
from matplotlib.backends.backend_pdf import PdfPages
pd.options.mode.chained_assignment=None



# Creating the data frame to read the csv file
df = pd.read_csv('D:\python\datasheet2.csv')
df.drop(index = 10472 , inplace = True)
df.drop(index = 9148,inplace=True)
#Creating the  second data frame to read the review csv file for adding new data
review_df = pd.read_csv('D:\python\datasheet2.csv')

#cleaning data for size
newSize = []

for row in df.Size:
    newrow = row[:-1]
    try:
        newSize.append(float(newrow))
    except:
        newSize.append(0) #When it says - Size Varies.
    
df.Size = newSize

df.Size.head()



#Cleaning the data of the Installs column
df['Installs'] = df['Installs'].str.strip('+')
df['Installs'] = df['Installs'].str.replace(',','')
df['Installs'] = df['Installs'].astype(int)
# CLEANING DATA FOR COLUMN 'Price'
df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].apply(lambda x: x.replace('$', ''))
# df['Price'] = df['Price'].astype(float)
#Copying the orignal dataframe df into sample for question 6

# Converting the last Updated column in the form 01-02-2003
df['Last Updated'] = df['Last Updated'].astype('datetime64[ns]')
# Now we will be creating a column that will consist of only years
df['Year'] = pd.DatetimeIndex(df['Last Updated']).year
# Now we will create a pandas series object that will be grouped by year and category
CatYear = df.groupby(by=['Category', 'Year'])
# Now we will convert into dictionary
TrendDict = CatYear.Installs.mean().to_dict()

#For question 6 we will be creating a dictionary
Year_Category = df.groupby(by = ['Year','Category'])
Year_cat_installs = Year_Category.Installs.mean()
#dictionary created
a_dict = Year_cat_installs.to_dict()

#For question 10 again we  will be creating a dictionary
df['Month'] = pd.DatetimeIndex(df['Last Updated']).month
CatMonth = df.groupby(by = ['Category','Month'])
CatMonthInstalls = CatMonth.Installs.mean()
month_dict = CatMonthInstalls.to_dict()

#Reading the dataset2  for the questions
df2 = pd.read_csv('D:\python\dataset3.csv')
dropind = df2[df2['Sentiment'].isnull() == True].index
df2.drop(index = dropind,inplace = True)

Label_font = ("Calibri", 22, "bold")
Label1_font = ("Calibri", 15, "bold")
Button_font = ("Calibri", 13, 'bold')
Button1_font = ("Calibri", 15, 'bold')


cat = list(df['Category'].unique())
Label_font = ("Calibri", 22, "bold")
Label1_font = ("Calibri", 15, "bold")
Button_font = ("Calibri", 13, 'bold')
Button1_font = ("Calibri", 15, 'bold')


def createWindow(window):
    window.geometry('40000x2500')
    window.resizable(True, True)
    window.configure(background="black")
    
    
def adjustWindow(window,screen):
    w = screen.winfo_screenwidth() # width of the screen
    h = screen.winfo_screenheight() # height of the screen
    window.geometry('%dx%d' % (w, h)) # set the dimensions of the screen and where it is placed
    window.resizable(True, True) # disabling the resize option for the window
    window.configure(background='white') # making the background white of the window


dataframe=df
def home_page():
    screen1.destroy()
    screen2.destroy()
    screen4.destroy()
    screen8.destroy()
    screen9.destroy()
    screen14.destroy()
    screen14_1.destroy()
    screen15.destroy()
    screen16.destroy()
    screen17.destroy()
    screen18.destroy()
    screen18_1.destroy()
    screena1.destroy()
    screend1.destroy()
    screenr1.destroy()
    screenr2.destroy()
    screens1.destroy()
    screenc1.destroy()
    


def backtohome():
    global home
    backtohome = Tk()
    backtohome.title("HOMEPAGE")
    createWindow(backtohome)
    l = Label(backtohome, text="ANALYSIS OF GOOGLE PLAYSTORE", width="500", height="2", font=Label_font,fg='white', bg='#174873').pack()

    l1 = Label(backtohome, text="Percentage download in each category", width="40", height="1", font=Label_font,fg='white', bg='#174873').place(x=25, y=90)
    b1 = Button(backtohome, text="FIG 1", bg="#e79700", width="5", height="1", font=Button_font, fg='white',command=fig1).place(x=25, y=90)

    l2 = Label(backtohome, text="Number of Downloads", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=140)
    b2 = Button(backtohome, text="FIG 2", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),g='white', command=fig2).place(x=25, y=140)

    l3 = Label(backtohome, text="Most,Least,Average Category", width="40", height="1", font=Label_font, fg='white', bg='#174873').place(x=25, y=190)
    b3 = Button(backtohome, text="FIG 3", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig3).place(x=25, y=190)

    l4 = Label(backtohome, text="Highest maximum average ratings", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=240)
    b4 = Button(backtohome, text="FIG 4", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig4).place(x=25, y=240)

    l5 = Label(backtohome, text="App according To size", width="40", height="1", font=Label_font,fg='white', bg='#174873').place(x=25, y=290)
    b5 = Button(backtohome, text="FIG 5", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig5).place(x=25, y=290)

    l6 = Label(backtohome, text="Downloads over period of three years", width="40", height="1", font=Label_font,fg='white', bg='#174873').place(x=25, y=340)
    b6 = Button(backtohome, text="FIG 6", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig6).place(x=25, y=340)

    l7 = Label(backtohome, text="Android version is not an issue", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=390)
    b7 = Button(backtohome, text="FIG 7", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig7).place(x=25, y=390)

    l8 = Label(backtohome, text="Most likely to be downloaded", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=440)
    b8 = Button(backtohome, text="FIG 8", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig8).place(x=25, y=440)

    l9 = Label(backtohome, text="Co-relation of downloads & ratings", width="40", height="1", font=Label_font,fg='white', bg='#174873').place(x=25, y=490)
    b9 = Button(backtohome, text="FIG 9", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig9).place(x=25, y=490)

    l10 = Label(backtohome, text="Qualifies as teen versus mature 17+.", width="40", height="1", font=Label_font,fg='white', bg='#174873').place(x=25, y=540)
    b10 = Button(backtohome, text="FIG 10", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'),fg='white', command=fig10).place(x=25, y=540)

    l11 = Label(home, text="Year has generated highest no of install for each app", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=90)
    b11 = Button(home, text="FIG 11", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig11).place(x=650, y=90)

    l12 = Label(home, text="Generate most positive & negative sentiments", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=140)
    b12 = Button(home, text="FIG 12", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig12).place(x=650, y=140)

    l13 = Label(home, text="Relation between Sentiment-polarity & subjectivity ", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=190)
    b13 = Button(home, text="FIG 13", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig13).place(x=650, y=190)

    l14 = Label(home, text="Reviews categorized as positive,negative & neutral", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=240)
    b14 = Button(home, text="FIG 14", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig14).place(x=650, y=240)

    l15 = Label(home, text="Advisable to launch app like 10 Best foods for you?", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=290)
    b15 = Button(home, text="FIG 15", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig15).place(x=650, y=290)

    l16 = Label(home, text="Indicator to aver. downloads generated entire year?", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=340)
    b16 = Button(home, text="FIG 16", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig16).place(x=650, y=340)

    l17 = Label(home, text="Size of App influence number of installs", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=390)
    b17 = Button(home, text="FIG 17", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig17).place(x=650, y=390)

    l18 = Label(home, text="Interface to add new data to both datasets", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=440)
    b18 = Button(home, text="FIG 18", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig18).place(x=650, y=440)
    
    l19 = Label(home, text="Apps free vs Paid", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=490)
    b19 = Button(home, text="FIG 19", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig19).place(x=650, y=490)            
                 
    backtohome.mainloop()


def fig1():
    fig1 = Tk()
    fig1.title("QUESTION 1")
    createWindow(fig1)
    Label(fig1, text="What is the percentage download in each category on the playstore ? ", width="100", height="4",font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig1, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)

    f = Figure(figsize=(11, 7), dpi=75)
    a = f.add_subplot(111)

    a.pie(df['Category'].value_counts().values, autopct='%1.1f%%',pctdistance = 1.1 , labeldistance = 1.2)
    a.legend(df['Category'].value_counts().index, loc='center left', bbox_to_anchor=(1.04, 0.5), ncol=1)

    canvas = FigureCanvasTkAgg(f, fig1)
    canvas.get_tk_widget().place(x=5, y=100)
    canvas.draw()

    fig1.mainloop()


def fig2():
    fig2 = Tk()
    fig2.title("QUESTION 2")
    createWindow(fig2)
    Label(fig2,text="How many apps have managed to get the following number of downloads \n a) Between 10,000 and 50,000 \n b) Between 50,000 and 150000 \n c) Between 150000 and 500000 \n d) Between 500000 and 5000000 \n e) More than 5000000",width="80", height="7", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig2, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)

    cut_bins = df.Installs.unique()
    #print(cut_bins)
    req_cut_bins = [10000, 50000, 150000, 500000, 5000000, 50000000, 10000000000]
    InstallCout = pd.cut(df['Installs'], req_cut_bins,labels=['10k-50k', '50k-150k', '150k-500k', '500k-5000k', '5000k-50000k', '50000k +'],include_lowest=True,right = False)

    figure1 = py.Figure(figsize=(6,7), dpi=70)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, fig2)
    bar1.get_tk_widget().place(x =500,y=150)
    InstallCout.value_counts(sort = False).plot(kind='bar', legend=False, ax=ax1)
    ax1.set_title('No of Apps Vs. No of Downloads')
    fig2.mainloop()

def fig3():
    fig3 = Tk()
    fig3.title("QUESTION 3")
    createWindow(fig3)
    Label(fig3,text="Which category of apps have managed to get most, least and \n an average of 2,50,000 downloads atleast ?",width="100", height="3", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig3, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    Label(fig3,text="Apps which has Maximum downloads ",width="50", height="2", font=Label1_font, fg='white', bg='#174873').place(x=700, y=120)
    Label(fig3,text="Communication = 8.435989e+07",width="50", height="2", font=Label1_font, fg='white', bg='#174873').place(x=700, y=180)
    Label(fig3,text="Apps which has downloads ",width="50", height="2", font=Label1_font, fg='white', bg='#174873').place(x=700, y=240)
    Label(fig3,text="Medical = 115026",width="50", height="2", font=Label1_font, fg='white', bg='#174873').place(x=700, y=300)
    Label(fig3,text="Apps which have average of 2,50,000 ",width="50", height="2", font=Label1_font, fg='white', bg='#174873').place(x=700, y=360)
    Label(fig3,text="Entertaintment, Tools,Game",width="50", height="2", font=Label1_font, fg='white', bg='#174873').place(x=700, y=420)
    

    # THIS MAKES A SERIES OF PANDAS (OBJECT THAT CONTAINS CATEGORIES AND MEAN INSTALL OF EACH CATEGORY)
    a = df.groupby('Category')['Installs'].mean()
    #THIS WILL TELL THE MAXIMUM INSTALLED
    print(a[a == a.max()])
    #THIS  WILL TELL THE CATEGORY WITH MINIMUM INSTALLATION
    print(a[a == a.min()])
    #THIS WILL TELL THE CATEGORY WITH AVERAGE INSTALLATIONS
    figure3 = Figure(figsize=(10, 8), dpi=60)
    ax3 = figure3.add_subplot(111)
    bar2 = FigureCanvasTkAgg(figure3, fig3)
    bar2.get_tk_widget().place(x = 5 , y = 78)
    #THIS MAKES A SERIES OF PANDAS (OBJECT THAT CONTAINS CATEGORIES AND MEAN INSTALL OF EACH CATEGORY)AND PLOT THE GRAPH
    df.groupby('Category')['Installs'].mean().plot(kind = 'bar' ,legend = False , ax = ax3)
    bar2.draw()
    fig3.mainloop()

def fig4():
    fig4 = Tk()
    fig4.title("QUESTION 4")
    createWindow(fig4)
    Label(fig4, text="Which category of apps have managed to get the highest maximum average ratings from the users ?",width="110", height="3", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    Label(fig4, text="Events has the highest ratings with 4.4355",width="50", height="3", font=Label1_font, fg='white', bg='#174873').place(x=710, y=120)
    b1 = Button(fig4, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    f = Figure(figsize=(11, 9), dpi=65)
    ax = f.add_subplot(111)

    a = df.groupby('Category')['Rating'].mean()
    print(a[a == a.max()])
    x_axis = list(a.to_dict().keys())
    y_axis = list(a.to_dict().values())
    ax.scatter(x_axis, y_axis)
    ax.set_xticklabels(x_axis, rotation=90, ha='center')

    canvas = FigureCanvasTkAgg(f, fig4)
    canvas.get_tk_widget().place(x=5, y=78)
    canvas.draw()
    fig4.mainloop()

def getTrendDict(TrendDict,Category):
    years = []
    install = []
    for category , installs in TrendDict.items():
        if list(category)[0] == Category:
            years.append(list(category)[1])
            install.append(installs)
    return years,install
def new_plot(TrendDict,Category):
    years,install = getTrendDict(TrendDict,Category)
    py.xticks(ticks = years , labels = years)
    py.plot(years,install)
    py.show()
def fig5():
    fig5 = Tk()
    fig5.title("QUESTION 5")
    createWindow(fig5)
    Label(fig5,text="app download according to size!",width="110", height="3", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b =  Button(fig5, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    #Now starting with the drop down list
    cut_bins = df.Size.unique()
    #print(cut_bins)
    req_cut_bins = [10, 20, 30,1000]
    SizeCout = pd.cut(df['Size'], req_cut_bins,labels=['10M-20M', '20M-30M', '30M+'],include_lowest=True,right = False)

    figure1 = py.Figure(figsize=(6,7), dpi=70)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1,fig5)
    bar1.get_tk_widget().place(x =750,y=100)
    SizeCout.value_counts(sort = False).plot(kind='bar', legend=False, ax=ax1)
    ax1.set_title('No of Apps Vs. Size of App')
    fig5.mainloop()

#this will return the category and corresponding number of installs
def get_parameters(a_dict,year):
    category = []
    install = []
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category.append(list(years)[1])
            install.append(installs)
    return category,install
def figure6(a_dict,variable):
    year = int(variable)
    category,install = get_parameters(a_dict,year)
    py.title(year)
    index = np.arange(len(category))
    py.xticks(index, category, fontsize=7, rotation=90)
    py.bar(category, install)
    py.show()
def year_2016(a_dict,year):
    category1 = []
    install1 = []
    fig2016 = Tk()
    fig2016.title('2016')
    createWindow(fig2016)
    Label(fig2016,text="For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads.\n What is the percentage increase or decrease that the apps have got over the period of three years ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category1.append(list(years)[1])
            install1.append(installs)
    #print(category1)
    #print(install1)
    #now creating an dictionary
    dict_2016 = dict(zip(category1,install1))
    maximum = max(dict_2016,key = dict_2016.get)
    print(maximum,dict_2016[maximum])
    minimum = min(dict_2016,key = dict_2016.get)
    print(minimum,dict_2016[minimum])
    Label(fig2016,text="MAXIMUM: VIDEO_PLAYERS -  12222178.57142857\nMINIMUM: WEATHER - 750.0",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=200, y=200)
    fig2016.mainloop()
def year_2017(a_dict,year):
    category1 = []
    install1 = []
    fig2017 = Tk()
    fig2017.title('2017')
    createWindow(fig2017)
    Label(fig2017,text="For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads.\n What is the percentage increase or decrease that the apps have got over the period of three years ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category1.append(list(years)[1])
            install1.append(installs)
    #print(category1)
    #print(install1)
    #now creating an dictionary
    dict_2017 = dict(zip(category1,install1))
    maximum = max(dict_2017,key = dict_2017.get)
    print(maximum,dict_2017[maximum])
    minimum = min(dict_2017,key = dict_2017.get)
    print(minimum,dict_2017[minimum])
    Label(fig2017,text="MAXIMUM: GAME - 7631323.026881721\nMINIMUM: MEDICAL - 17026.93181818182",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=200, y=200)
    fig2017.mainloop()
def year_2018(a_dict,year):
    category1 = []
    install1 = []
    fig2018 = Tk()
    fig2018.title('2018')
    createWindow(fig2018)
    Label(fig2018,text="For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads.\n What is the percentage increase or decrease that the apps have got over the period of three years ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    for years,installs in a_dict.items():
        if list(years)[0] == year:
            category1.append(list(years)[1])
            install1.append(installs)
    #print(category1)
    #print(install1)
    #now creating an dictionary
    dict_2018 = dict(zip(category1,install1))
    maximum = max(dict_2018,key = dict_2018.get)
    print(maximum,dict_2018[maximum])
    minimum = min(dict_2018,key = dict_2018.get)
    print(minimum,dict_2018[minimum])
    Label(fig2018,text="MAXIMUM: COMMUNICATION - 118791514.18248175\nMINIMUM: MEDICAL - 164144.5357142857",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=200, y=200)
    fig2018.mainloop()
def fig6():
    fig6 = Tk()
    fig6.title("QUESTION 6")
    createWindow(fig6)
    Label(fig6,text="For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads.\n What is the percentage increase or decrease that the apps have got over the period of three years ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig6, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    OPTIONS = ['2016','2017','2018']
    variable = StringVar(fig6)
    variable.set('CATEGORY')
    w = OptionMenu(fig6, variable, *OPTIONS)
    w.place(x=250, y=220)
    w.configure(bg="#e79700", fg='white', height="1", font=Button1_font)
    b = Button(fig6, text='SHOW', command = lambda:figure6(a_dict,variable.get()))
    b.place(x=550, y=220)
    b1 = Button(fig6,text='2016',width = '7',height = '2',command = lambda:year_2016(a_dict,2016))
    b1.place(x=250,y=300)
    b2 = Button(fig6, text='2017', width='7', height='2', command=lambda: year_2017(a_dict, 2017))
    b2.place(x=250, y=400)
    b3 = Button(fig6, text='2018', width='7', height='2', command=lambda: year_2018(a_dict, 2018))
    b3.place(x=250, y=500)
    fig6.mainloop()

def androidv():
    Installs=[]
    for i in df['Installs']: 
        if i=='Free':
            Installs.append(0)
        else:
            Installs.append(int(i.rstrip('+').replace(',','')))
   
    

    n=df['Android Ver']
    s=Installs
    num=['A','B']
    v=[None]*len(n)
    
    d=[None]*len(n)
    for i in range(0,len(n)):
        if re.search('^V',str(n[i])):
            #num.append('A')
            v[i]=s[i]
        else:
            #num.append('B')
           d[i]=s[i]

        
    a=[None]*2
    a[0]=sum(list(filter(None, v)))
    a[1]=sum(list(filter(None, d)))
    g=sns.barplot(x=a, y=num, palette='husl')
    py.title('Android Version type vs. downloads',fontsize=10)
    py.xlabel('Installs', fontsize = 10)
    py.ylabel('Android Version', fontsize = 10)
    
    fig7=g.get_figure()
    fig7.savefig('a.png')
    Image.open('a.png').save('a.png','PNG')

def fig7():
    fig7 = Toplevel()
    fig7.title("QUESTION 7")
    createWindow(fig7)
    Label(fig7,text="All those apps,whose android version is not an issue and can work with varying devices.\n What is the percentage increase or decrease in the downloads ?",width="170", height="5", font=Label1_font, fg='white', bg='#800000').place(x=0, y=0)
    b1 = Button(fig7, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    android_df = df.copy()
    android_df = android_df[android_df['Android Ver'] == 'Varies with device']
    android_df.sort_values('Year',inplace = True)#inplace means do that task in that same dataframe return none
    year = ['2013','2014','2015','2016','2017','2018']
    k = []
    d=[]
    for i in range(2018 - 2012 + 1):
        k.append(android_df[android_df.Year == (2012 + i)]['Installs'].sum())#total installs for each year
    for i in range(2018 - 2012):
        m=((k[i + 1] - k[i]) / (k[i] ))* 100#2013-2012/2012*100
        d.append(m)
        print(d)
    Label(fig7,text="2013 to 2014 Download percent change : 403.1137332022288\n2014 to 2015 Download percent change : 81.86387622149837\n2015 to 2016 Download percent change : 1806.729112102136\n2016 to 2017 Download percent change : 41.47751974465249\n2017 to 2018 Download percent change : 12104.35411777218",width="65", height="8", font=Label1_font, fg='white', bg='#174873').place(x=650, y=300)
    f = Figure(figsize=(11, 8), dpi=55)
    ax7 = f.add_subplot(111)
    ax7.plot(year,d,linestyle='--',color='r')
    ax7.set_title("Year wise App Andoid Version",fontsize=20)
    ax7.set_xticklabels(year,ha='center')
    ax7.set_xlabel('Years',fontsize=20)
    ax7.set_ylabel('Varied Downloads',fontsize=20)
    canvas = FigureCanvasTkAgg(f, fig7)#object of canvas
    canvas.get_tk_widget().place(x=50, y=150)#to get the widget into canvas
    canvas.draw()#to plot
    f.tight_layout()
   


def fig8():
    fig8 = Tk()
    fig8.title("QUESTION 8")
    createWindow(fig8)
    Label(fig8,text="Amongst sports, entertainment,social media,news,events,travel and games,\n Which is the category of app that is most likely to be downloaded in the coming years,\n kindly make a prediction and back it with suitable findings ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig8, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    # Now starting with the drop down list
    OPTIONS = ['SPORTS','ENTERTAINMENT','SOCIAL','NEWS_AND_MAGAZINES','EVENTS','NEWS','EVENTS','TRAVEL_AND_LOCAL','GAME']
    variable = StringVar(fig8)
    variable.set('CATEGORY')
    w = OptionMenu(fig8, variable, *OPTIONS)
    w.place(x=250, y=220)
    w.configure(bg="#e79700", fg='white', height="1", font=Button1_font)
    b = Button(fig8, text='SHOW', command=lambda: new_plot(TrendDict, variable.get()))
    b.place(x=550, y=220)
    fig8.mainloop()


def fig9():
    fig9 = Toplevel(home)
    fig9.title("QUESTION 9")
    createWindow(fig9)
    Label(fig9,text="All those apps who have managed to get over 1,00,000 downloads,\n have they managed to get an average rating of 4.1 and above? \n An we conclude something in co-relation to the number of downloads and the ratings received ?",width="160", height="5", font=Label1_font, fg='white', bg='#800000').place(x=0, y=0)
    b1 = Button(fig9, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    x=dataframe[['Category','Rating','Installs']]
    z=x.to_dict(orient='split')
    cat =dataframe['Category'].unique()
    cat=cat.tolist()
    d1=[]
    for i in cat:
        count=0
        for j in range(len(z['data'])):
            if(i==z['data'][j][0]):
                if(z['data'][j][1]>=4.1 and z['data'][j][2]>=100000):
                    count+=1
        d1.append(count)
    a = x[['Rating','Installs']]
    rat = a[(a['Rating']>=4.1) & (a['Installs']>=100000)]
    corr = rat['Installs'].corr(rat['Rating'])
#    print(corr)
#    print(np.corrcoef(rat['Installs'],rat['Rating']))
    figure9 = py.Figure(figsize = (17,8) , dpi = 70)
    ax9 = figure9.add_subplot(1,2,1)
    ax9.set_title('APP WITH 4.1+ RATING AND 1,00,000+ DOWNLOADS',fontsize=20)
    ax9.plot(cat,d1,color='orange')
    ax9.set_xticklabels(cat,rotation=90,ha='center')
    ax9.set_ylabel('No. of Apps',fontsize=20)
    ax9.set_xlabel('CATEGORIES',fontsize=20)
    ax9b = figure9.add_subplot(1,2,2)
    ax9b.scatter(rat['Rating'],rat['Installs'],marker="8",c='r')
    ax9b.set_ylabel("Downloads",fontsize=20)
    ax9b.set_xlabel("Rating",fontsize=20)
    ax9b.set_title("Correlation between Downloads and Rating is (-0.00838)",fontsize=20)
    canvas = FigureCanvasTkAgg(figure9, fig9)
    canvas.get_tk_widget().place(x=50, y=130)
    canvas.draw()
    figure9.tight_layout()

def find_month(month_dict,Category):
    month = []
    install = []
    for category,installs in month_dict.items():
        if list(category)[0] == Category:
            month.append(list(category)[1])
            install.append(installs)
    return month,install
def get_month(month_dict,Category):
    month,install = find_month(month_dict,Category)
    print(month)
    print(install)
    dict_month_installs = dict(zip(month,install))
    maximum = max(dict_month_installs,key = dict_month_installs.get)
    print(maximum,dict_month_installs[maximum])
    return month,install
def fig10():
    fig10 = Toplevel(home)
    fig10.title("QUESTION 10")
    createWindow(fig10)
    Label(fig10,text="Across all the years,which month has seen the maximum downloads for each of the category.\n What is the ratio of downloads for the app that qualifies as teen versus mature 17+ ?",width="170", height="5", font=Label1_font, fg='white', bg='#174873').grid(row=0,column=0)
    cat = dataframe['Category'].unique()
    b1 = Button(fig10, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    cat=cat.tolist()
    x = dataframe[['Category','Installs','Month']]
    df = x.to_dict(orient='split')
    downloads = {}
    for i in cat:
      downloads[i] = [0]*13
    for i in cat:
      for j in range(len(df['data'])):
        if (i==df['data'][j][0]):
          month = df['data'][j][2]
          downloads[i][month] += df['data'][j][1]
    max_month = [0]*13
    max_category = [0]*13
    for j in range(1,13):
      ins = 0
      for i in cat:
        c = ''
        if(downloads[i][j] > ins):
          ins = downloads[i][j]
          c = i
          max_month[j] = ins
          max_category[j] = c  
    max_month.pop(0)
    max_category.pop(0)
    l4=['Month','Category','Downloads']
                
    c=0
    for i in range(len(l4)):
      Label(fig10, text=l4[i],width="20", height="2", font=Label1_font, fg='white', bg='#174873').place(x=700+c, y=150)
      c+=200
    c=10
    for i in range(len(max_month)):
      Label(fig10, text=calendar.month_name[i+1],width="20", height="1", font=Label1_font, fg='white', bg='#174873').place(x=700, y=200+c)
      c+=40
    c=10
    for i in range(len(max_month)):
      Label(fig10, text=max_category[i],width="20", height="1", font=Label1_font, fg='white', bg='#174873').place(x=900, y=200+c)
      c+=40
    c=10
    for i in range(len(max_month)):
      Label(fig10, text=max_month[i],width="20", height="1", font=Label1_font, fg='white', bg='#174873').place(x=1100, y=200+c)
      c+=40
    df = dataframe[['Content Rating','Installs']]
    teen  = []
    mature = []
    for i in range(len(df)):
      if(df['Content Rating'].iloc[i]=="Teen"):
        teen.append(df['Installs'].iloc[i])
      elif(df['Content Rating'].iloc[i]=="Mature 17"):
        mature.append(df['Installs'].iloc[i])
    teen_t = sum(teen)
    mature_t = sum(mature)
    total = teen_t  + mature_t
    teen_t = round((teen_t/total)*100,3)
    mature_t = round((mature_t/total)*100,3)
    percentage = [teen_t,mature_t]
    explode = (0.01,0.03)
    figure10 = py.Figure(figsize = (6,7) , dpi = 70)
    ax9 = figure10.add_subplot(111)
    ax9.pie(percentage,labels=('Teen','Mature 17+'),colors = ('Blue','Yellow'),autopct="%1.1f%%",startangle=90, pctdistance=0.85, explode = explode)
    ax9.axis('equal')
    ax9.set_title("TEEN VS MATURE 17",fontsize=20)
    canvas = FigureCanvasTkAgg(figure10, fig10)
    canvas.get_tk_widget().place(x=150, y=130)
    canvas.draw()
    figure10.tight_layout()



   
   
    
def fig11():
    fig11 = Toplevel(home)
    fig11.title("QUESTION 11")
    createWindow(fig11)
    Label(fig11,text="Which quarter of which year has generated the highest number of install for each app used in the study?",width="170", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig11, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    cat =dataframe['Category'].unique()
    cat=cat.tolist()
    x = dataframe[['App','Category','Installs','Year','Month']]
    df = x.to_dict(orient='split')
    q1=[1,2,3]
    q2=[4,5,6]
    q3=[7,8,9]
    q4=[10,11,12]
    year = [2015,2016,2017,2018]
    quarter = {}
    for i in year:
      quarter[i] = [0]*4
    for i in range(len(x)):
      for j in year:
        if(df['data'][i][3] == j):
          if(df['data'][i][4] in q1):
            quarter[j][0] += df['data'][i][2]
          if(df['data'][i][4] in q2):
            quarter[j][1] += df['data'][i][2]
          if(df['data'][i][4] in q3):
            quarter[j][2] += df['data'][i][2]
          if(df['data'][i][4] in q4):
            quarter[j][3] += df['data'][i][2]
    q = ['Q1','Q2','Q3','Q4']
    figure11 = py.Figure(figsize = (6,7) , dpi = 70)
    ax11 = figure11.add_subplot(111)
    width = 0.25
    pos = list(range(len(quarter)))
    ax11.bar(pos,quarter[2015],width,alpha=0.5,color='blue',label='2015')
    ax11.bar([p + width for p in pos],quarter[2016],width,alpha=0.5,color='yellow',label='2016')
    ax11.bar([p + width*2 for p in pos],quarter[2017],width,alpha=0.5,color='red',label='2017')
    ax11.bar([p + width*3 for p in pos],quarter[2018],width,alpha=0.5,color='black',label='2018')
    ax11.set_xticks([p + 1.5*width for p in pos])
    ax11.set_xticklabels(year)
    ax11.set_xlim(min(pos)-width, max(pos)+width*8)
    ax11.set_ylim([0,1000000000])
    ax11.legend(q, loc='upper left')
    ax11.set_xlabel("QUARTERS",fontsize=20)
    ax11.set_ylabel("DOWNLOADS",fontsize=20)
    ax11.set_title("Downloads in each quarter of the year",fontsize=20)
    canvas = FigureCanvasTkAgg(figure11, fig11)
    canvas.get_tk_widget().place(x=400, y=130)
    canvas.draw()
    figure11.tight_layout()
                

        
    

def fig12():
    fig12 = Tk()
    fig12.title("QUESTION 12")
    createWindow(fig12)
    Label(fig12,text="Which of all the apps given have managed to generate the most positive and negative sentiments. \n Also figure out the app which has generated approximately the same ratio for positive and negative sentiments ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig12, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)

    polarity_sum = df2.groupby('App')['Sentiment_Polarity'].sum().sort_values()
    #print("Positive Rated :\n", polarity_sum.nlargest(1))
    #print("Negative Rated :\n", polarity_sum.nsmallest(1))
    apps = list(df2.App.unique())
    ratios = list()
    for app in apps:
        find = df2.loc[df2.App == app]
        pos_rat = find.loc[df2.Sentiment == 'Positive']['Sentiment_Polarity'].sum() / len(find)
        neg_rat = find.loc[df2.Sentiment == 'Negative']['Sentiment_Polarity'].sum() / len(find) * -1
        if abs(pos_rat - neg_rat) < 0.005:
            ratios.append((app, pos_rat, neg_rat))
    print('Apps with similar ratio for positive and Negative Sentiments are :')
    print(ratios)
    category1=StringVar()
    droplist_cat=OptionMenu(fig12,category1, *ratios)
    droplist_cat.config(width=100)
    category1.set(" Apps with same ratios")
    droplist_cat.grid(row=1,column=3,padx=120,pady=520)
    Label(fig12,text="App having Most Positive Sentiment : 10 Best Foods for You : 91.322167 \n \n App having Most Negative Sentiment : Be A Legend: Soccer : -9.726559 ",width="100", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)
    Label(fig12,text="Apps having same ratios ",width="40", height="2", font=Label1_font, fg='black', bg='white').place(x=200, y=460)
    

    fig12.mainloop()

    

def fig13():
    fig13 = Tk()
    fig13.title("QUESTION 13")
    createWindow(fig13)
    Label(fig13,text="Study and find out the relation between the Sentiment-polarity and sentiment-subjectivity of all the apps ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig13, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    #Label(fig13, text="The correlation value is:0.2", width="60", height="2", font=Label1_font,fg='white', bg='#174873').place(x=200, y=150)
    sns.scatterplot(x = 'Sentiment_Polarity',y = 'Sentiment_Subjectivity',data = df2)
    py.show()
    Label(fig13,text="Complete Analysis",width="30", height="2", font=Label1_font, fg='white', bg='#174873').place(x=0, y=150)
    
    #print(df2['Sentiment_Polarity'].corr([df2['Sentiment_Subjectivity']]))
    print(df2.columns)
    m=df2.describe()
    print(m)
    Label(fig13,text="Analysis \n------\n Count \n mean \n std \n min \n 25% \n 50% \n 75%\n max",width="20", height="12", font=Label1_font, fg='white', bg='#174873').place(x=0, y=250)
    Label(fig13,text="Sentiment polarity \n------\n 37472 \n 0.182146 \n 0.351301 \n -1\n 0 \n 0.15 \n 0.4 \n 1",width="30", height="12", font=Label1_font, fg='white', bg='#174873').place(x=150, y=250)
    Label(fig13,text="Sentiment subjectivity \n -----\n 37432 \n 0.4920704 \n 0.259949 \n 0\n 0.35 \n 0.514 \n 0.65 \n 1",width="30", height="12", font=Label1_font, fg='white', bg='#174873').place(x=450, y=250)
    Label(fig13,text="From the table we can conclude 75% of apps have sentiment polarity 0.4 and the corresponding subjectivity is 0.65",width="100",height="3",font=Label1_font,fg='white',bg='#e79700').place(x=0, y=550)
    
    
    
    
    
    
    fig13.mainloop()
    
    
def search_review(fig,search):
    if(len(search)==0):
        tm.showerror("Invalid!","App Name cannot be empty")
        searchEntry.focus_set()
    else:
        search = str(search)
        conn = pymysql.connect(host="localhost",user="root",passwd="",database="playstore")
        cur = conn.cursor()
        query = """ SELECT App,Positive,Negative,Neutral FROM app_review WHERE App = %s"""
        params = (search)
        cur.execute(query,params)
        search_query = cur.fetchall()
        conn.commit()
        conn.close()
        c=100
        texts = ['App Name :','No. of Positive Sentiments :','No. of Negative Sentiments :','No. of Neutral Sentiments :']
        for i in range(4):
          Label(fig, text=texts[i],width="60", height="3", font=Label1_font, fg='white', bg='#174873',anchor=W).place(x=50,y=300+c)
          Label(fig, text=search_query[0][i],width="20", height="3", font=Label1_font, fg='white', bg='#174873').place(x=300,y=300+c)
          c+=60
        figure14 = py.Figure(figsize = (7,8) , dpi = 75)
        ax14 = figure14.add_subplot(111)
        print(search_query)
        s = [int(x) for x in search_query[0][1:]]
        l = ['Positive','Negative','Neutral']
        ax14.bar(l,s,color=['r','g','b'])
        ax14.set_xticklabels(l, ha='center')
        ax14.set_ylabel("No. of Sentimnts",fontsize=20)
        ax14.set_xlabel("Sentiments",fontsize=20)
        ax14.set_title("Classification of Sentiments",fontsize=20)
        canvas = FigureCanvasTkAgg(figure14, fig)
        canvas.get_tk_widget().place(x=700, y=150)
        canvas.draw()
        figure14.tight_layout()

    
def fig14():
    fig14 = Toplevel(home)
    fig14.title("QUESTION 14")
    createWindow(fig14)
    Label(fig14, text="Generate an interface where the client can see the reviews categorized as positive.negative and neutral ,once they \n have selected the app from a list of apps available for the study.",width="170", height="5", font=Label1_font, fg='white', bg='#800000').place(x=0, y=0)
    b1 = Button(fig14, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
#    df1 = df2[['App','Translated_Review','Sentiment_Polarity']]   
#    apps = list(df1['App'].unique())
#    df1 = df1.to_dict(orient='split')
#    df = pd.DataFrame(columns=['App','Positive','Negative','Neutral'],index=range(len(apps)))
#    c =  0
#    for a in apps:
#      counts = [0,0,0]
#      df['App'].iloc[c] = a  
#      for i in range(len(df1['data'])):
#        if(df1['data'][i][0]==a):
#          if(df1['data'][i][2]>0):
#            counts[0] += 1
#          elif(df1['data'][i][2]<0):
#            counts[1] += 1
#          elif(df1['data'][i][2]==0):
#            counts[2] += 1
#      df['Positive'].iloc[c] = counts[0]
#      df['Negative'].iloc[c] = counts[1]
#      df['Neutral'].iloc[c] = counts[2]
#      c+=1
#    final_df = df
#    final_df.to_excel('sentiments.xlsx')
    search = StringVar()
    global searchEntry
    Label(fig14, text="Search an App : ",width="50", height="5", font=Label1_font, fg='white', bg='#174873',anchor=N).place(x=100, y=200)
    searchEntry = Entry(fig14,textvar=search)
    searchEntry.place(x=300,y=260)
    b2 = Button(fig14, text="Search", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=lambda:search_review(fig14,search.get())).place(x=150,y=250)
    

    


def fig15():
    fig15 = Tk()
    fig15.title("QUESTION 15")
    createWindow(fig15)
    Label(fig15, text="Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these apps ?",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig15, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    kk = df2.loc[(df2.App == '10 Best Foods for You') & (df2.Sentiment == 'Positive')]
    print(len(kk))
    print(kk['Sentiment_Polarity'].sum())
    Label(fig15,text="The Total number of positive Sentiments recieved by the App are 162 \n\n and Total Sentiment Polarity is 95.37216720779222 \n So it is Advisable to Launch the app like '10 BEST FOODS FOR YOU'",width="100", height="8", font=Label1_font, fg='black', bg='white').place(x=200, y=200)
    fig15.mainloop()


def fig16():
    fig16 = Toplevel(home)
    fig16.title("QUESTION 16")
    createWindow(fig16)
    Label(fig16, text="Which month(s) of the year , is the best indicator to the avarage downloads that an app will generate over the entire year?",width="170", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig16, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    label = [0]*13
    for i in range(1,13):
      label[i] = calendar.month_name[i]
    x = dataframe[['Month','Installs']]
    df = x.groupby('Month')['Installs'].mean()
    p = label.pop(0)
    my_cmap = cm.get_cmap('jet')
    my_norm = Normalize(vmin=-3,vmax=3)
    t = np.array(list(range(5)))
    figure16 = py.Figure(figsize = (9,7) , dpi = 65)
    ax16 = figure16.add_subplot(111)
    ax16.bar(label,df,color=my_cmap(my_norm(t)))
    ax16.set_ylabel('DOWNLOADS',fontsize=20)
    ax16.set_xlabel('MONTHS',fontsize=20)
    ax16.set_title("Comparison of average downloads monthwise",fontsize=20)
    ax16.set_xticklabels(label,rotation=90)
    canvas = FigureCanvasTkAgg(figure16, fig16)
    canvas.get_tk_widget().place(x=370, y=150)
    canvas.draw()
    figure16.tight_layout()

def fig17():
    global fig17y,fig17z
    fig17 = Toplevel(home)
    fig17.title("QUESTION 17")
    createWindow(fig17)
    Label(fig17, text="Does the size of the App influence the number of installs that it gets ? if,yes the trend is positive or negative with the increase in the app size.",width="170", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig17, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    count=[0,0,0,0,0,0,0,0]
    fig17y=count#updated list stored for fig 17
    y = list([count[0],count[1],count[2]])
    # print(dataframe[dataframe.Rating>=4.1])
    z = ['10-20','20-30','30+']
    fig17z=['10-20','20-30','30-40','40-50','50-60','60-70','70-80','80+']#for fig 17
    figure17 = py.Figure(figsize = (9,8) , dpi = 65)
    ax17 = figure17.add_subplot(111)
    ax17.plot(fig17z,fig17y,linestyle='dashed',color='b')
    ax17.set_ylabel('Number of Downloads',fontsize=15)
    ax17.set_xlabel('Size of App in MB',fontsize=15)
    ax17.set_title('Trend of Size vs Downloads',fontsize=15)  
    canvas = FigureCanvasTkAgg(figure17, fig17)
    canvas.get_tk_widget().place(x=300, y=100)
    canvas.draw()
    figure17.tight_layout()

def validate(event,input):
  if(input=='Application Name'):
    if all(x.isalnum() or x.isspace() for x in app.get()) and (len(app_name.get())> 0):
      catEntry.focus_set()
      catEntry.config(state='normal')
    else:
      tm.showerror("Invalid!" ,"Application name not valid . Spaces are allowed.")
      appEntry.focus_set()
  elif(input=='Category'):
    if(category.get()!='--select category --'):
      ratEntry.focus_set()
      ratEntry.config(state='normal')
    else:
      tm.showerror("Invalid!" ,"Category is not selected.")
      catEntry.focus_set()
  elif(input=='Ratings'):
    rating = float(ratings.get())
    if(isinstance(rating,(int,float)) and (0<=rating<=5)):
      reEntry.focus_set()
      reEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Rating should be a floating number between 0 & 5!")
      ratEntry.focus_set()
  elif(input=='Reviews'):
    if(str(reviews.get()).isnumeric()):
      sizeEntry.focus_set()
      sizeEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Reviews should be a whole number!")
      reEntry.focus_set()
  elif(input=='Size'):
    if(len(size.get())>0):
      insEntry.focus_set()
      insEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Size cannot be empty!")
      sizeEntry.focus_set()
  elif(input=='Installs'):
    if(str(installs.get()).isnumeric()):
      typeEntry.focus_set()
      typeEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Installs should be a whole number!")
      insEntry.focus_set()
  elif(input=='Type'):
    if(apptype.get()!='--select type --'):
      priceEntry.focus_set()
      priceEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Type cannot be empty!")
      typeEntry.focus_set()
  elif(input=='Price'):
    if(len(price.get())>0):
      conEntry.focus_set()
      conEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Price cannot be empty!")
      priceEntry.focus_set()
  elif(input=='Content Rating'):
    if(contentrating.get()!='--select content rating --'):
      gEntry.focus_set()
      gEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Content Rating cannot be empty!")
      conEntry.focus_set()
  elif(input=='Genres'):
    if(genres.get()==category.get()):
      luEntry.focus_set()
      luEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Genre should be same as category!")
      gEntry.focus_set()
  elif(input=='Last Updated'):
    if(len(lastupdated.get())>0):
      cvEntry.focus_set()
      cvEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Last Updated cannot be empty!")
      luEntry.focus_set()
  elif(input=='Current Version'):
    if(len(currentver.get())>0):
      avEntry.focus_set()
      avEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Current Version cannot be empty!")
      cvEntry.focus_set()
  elif(input=='Android Version'):
    if(len(androidver.get())>0):
      print("Success")
    else:
      tm.showerror("Invalid!","Android Version cannot be empty!")
      avEntry.focus_set()
  elif(input=='Application'):
    if all(x.isalnum() or x.isspace() for x in application.get()) and (len(application.get())> 0):
      reviewEntry.focus_set()
      reviewEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Application Name not valid .Spaces are allowed. ")
      appEntry2.focus_set()
  elif(input=='Translated Review'):
    if(len(trans_review.get())>0):
      sentEntry.focus_set()
      sentEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Translated Review cannot be empty")
      reviewEntry.focus_set()
  elif(input=='Sentiment'):
    if(str(sentiment.get())!='--select sentiment --'):
      polEntry.focus_set()
      polEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Sentiment cannot be empty")
      sentEntry.focus_set()
  elif(input=='Sentiment Polarity'):
    polarity = float(senti_polarity.get())
    if(isinstance(polarity,(int,float))):
      subEntry.focus_set()
      subEntry.config(state='normal')
    else:
      tm.showerror("Invalid!","Sentiment Polarity should be a floating number")
      polEntry.focus_set()
  elif(input=='Sentiment Subjectivity'):
    if(isinstance(float(senti_subject.get()),(int,float))):
      print("Success")
    else:
      tm.showerror("Invalid!","Sentiment Subjectivity should be a floating number")
      subEntry.focus_set()
#--
def check_entry(new_entry):
    global df
    Label(new_entry,text="Updated succesfully", width="25", height="1", font=Label_font, bg='brown', fg='white').place(x=50,y=600)
    d = datetime.strptime(str(lastupdated.get()),'%d/%m/%Y')
    appdetails = {'App': app.get(), 'Category': category.get(), 'Rating': ratings.get(), 'Reviews': reviews.get(),
                  'Size': size.get(), 'Installs': installs.get(), 'Type': apptype.get(), 'Price': price.get(),
                  'Content Rating': contentrating.get(), 'Genres': genres.get(), 'Last Updated': d,
                  'Current Ver': currentver.get(), 'Android Ver': androidver.get(),'Year':d.year,'Month':d.month}
    column = list(appdetails.keys())
    new_data_frame = pd.DataFrame([appdetails],columns = column)
    df = df.append(new_data_frame,ignore_index=True,sort = False)
    df.to_csv("APP_DETAILS.csv",index=False)
    
def check_review(new_review):
    global review_df
    Label(new_review,text="Updated succesfully", width="25", height="1", font=Label_font, bg='brown', fg='white',anchor=W).place(x=50,y=520)
    review_details = {'App':application.get(),'Translated_Review':trans_review.get(),'Sentiment':sentiment.get(),'Sentiment_Polarity': senti_polarity.get(),'Sentiment_Subjectivity':senti_subject.get()}
    column = list(review_details.keys())
    new_data_frame = pd.DataFrame([review_details],columns = column)
    review_df = review_df.append(new_data_frame,ignore_index = True , sort = False)
    review_df.to_csv("REVIEW.csv",index=False)
    
def new_entry():
    global app, category, ratings, reviews, size, installs, apptype, price, contentrating, genres, lastupdated, currentver, androidver
    global appEntry,catEntry,ratEntry,reEntry,sizeEntry,insEntry,typeEntry,priceEntry,conEntry,gEntry,luEntry,cvEntry,avEntry
    new_entry = Toplevel(fig18)
    new_entry.title("New Entry")
    createWindow(new_entry)

    app = StringVar(new_entry)
    category = StringVar(new_entry)
    ratings = StringVar(new_entry)
    reviews = StringVar(new_entry)
    size = StringVar(new_entry)
    installs = StringVar(new_entry)
    apptype = StringVar(new_entry)
    price = StringVar(new_entry)
    contentrating = StringVar(new_entry)
    genres = StringVar(new_entry)
    lastupdated = StringVar(new_entry)
    currentver = StringVar(new_entry)
    androidver = StringVar(new_entry)

    Label(new_entry, text="Enter a New App Entry ", width="500", height="2", font=Label_font, fg='white',bg='#800000').pack()

    Label(new_entry, text="", bg='#1aff8c', width='125', height='35').place(x=50, y=120)
    Label(new_entry, text="Application Name", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=130, y=160)
    appEntry=Entry(new_entry, textvar=app)
    appEntry.place(x=300, y=160)
    appEntry.bind("<Return>", lambda event : validate(event, "Application Name"))
    appEntry.bind("<Tab>", lambda event : validate(event, "Application Name"))
    
    Label(new_entry, text="Category", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=130,y=210)
    catEntry=Entry(new_entry, textvar=category)
    catEntry.place(x=300, y=210)
    list1 = cat
    droplist = OptionMenu(new_entry, category, *list1)
    droplist.config(width=17)
    category.set('--select category --')
    droplist.place(x=300, y=210)
    catEntry.bind("<Return>", lambda event : validate(event, "Category"))
    catEntry.bind("<Tab>", lambda event : validate(event, "Category"))
    
    Label(new_entry, text="Ratings", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=130,y=260)
    ratEntry=Entry(new_entry, textvar=ratings)
    ratEntry.place(x=300, y=260)
    ratEntry.bind("<Return>", lambda event : validate(event, "Ratings"))
    ratEntry.bind("<Tab>", lambda event : validate(event, "Ratings"))
    
    Label(new_entry, text="Reviews", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=130,y=310)
    reEntry=Entry(new_entry, textvar=reviews)
    reEntry.place(x=300, y=310)
    reEntry.bind("<Return>", lambda event : validate(event, "Reviews"))
    reEntry.bind("<Tab>", lambda event : validate(event, "Reviews"))

    Label(new_entry, text="Size", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=130,y=360)
    sizeEntry=Entry(new_entry, textvar=size)
    sizeEntry.place(x=300, y=360)
    sizeEntry.bind("<Return>", lambda event : validate(event, "Size"))
    sizeEntry.bind("<Tab>", lambda event : validate(event, "Size"))
    
    Label(new_entry, text="Installs", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=130,y=410)
    insEntry=Entry(new_entry, textvar=installs)
    insEntry.place(x=300, y=410)
    insEntry.bind("<Return>", lambda event : validate(event, "Installs"))
    insEntry.bind("<Tab>", lambda event : validate(event, "Installs"))
    
    Label(new_entry, text="Type", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=130,y=460)
    typeEntry=Entry(new_entry, textvar=apptype)
    typeEntry.place(x=300, y=460)
    list2 = ['Free','Paid']
    droplist = OptionMenu(new_entry, apptype, *list2)
    droplist.config(width=17)
    apptype.set('--select type --')
    droplist.place(x=300, y=460)
    typeEntry.bind("<Return>", lambda event : validate(event, "Type"))
    typeEntry.bind("<Tab>", lambda event : validate(event, "Type"))
    
    Label(new_entry, text="Price", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=500,y=160)
    priceEntry=Entry(new_entry, textvar=price)
    priceEntry.place(x=670, y=160)
    priceEntry.bind("<Return>", lambda event : validate(event, "Price"))
    priceEntry.bind("<Tab>", lambda event : validate(event, "Price"))
    
    Label(new_entry, text="Content Rating", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=500, y=210)
    conEntry=Entry(new_entry, textvar=contentrating)
    conEntry.place(x=670, y=210)
    list3 = ['Everyone', 'Teen', 'Everyone 10', 'Mature 17', 'Adults only 18','Unrated']
    droplist = OptionMenu(new_entry, contentrating, *list3)
    droplist.config(width=17)
    contentrating.set('--select content rating --')
    droplist.place(x=670, y=210)
    conEntry.bind("<Return>", lambda event : validate(event, "Content Rating"))
    conEntry.bind("<Tab>", lambda event : validate(event, "Content Rating"))
    
    Label(new_entry, text="Genres", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=500,y=260)
    gEntry=Entry(new_entry, textvar=genres)
    gEntry.place(x=670, y=260)
    list1 = cat
    droplist = OptionMenu(new_entry, genres, *list1)
    droplist.config(width=17)
    genres.set('--select genres --')
    droplist.place(x=670, y=260)
    gEntry.bind("<Return>", lambda event : validate(event, "Genres"))
    gEntry.bind("<Tab>", lambda event : validate(event, "Genres"))
    
    Label(new_entry, text="Last Updated", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=500, y=310)
    luEntry=DateEntry(new_entry , textvariable = lastupdated , date_pattern='dd/mm/y')
    luEntry.place(x=670, y=310)
    luEntry.bind("<Return>", lambda event : validate(event, "Last Updated"))
    luEntry.bind("<Tab>", lambda event : validate(event, "Last Updated"))
    
    Label(new_entry, text="Current Version", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=500, y=360)
    cvEntry=Entry(new_entry, textvar=currentver)
    cvEntry.place(x=670, y=360)
    cvEntry.bind("<Return>", lambda event : validate(event, "Current Version"))
    cvEntry.bind("<Tab>", lambda event : validate(event, "Current Version"))
    
    Label(new_entry, text="Android Version", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c', anchor=W).place(x=500, y=410)
    avEntry=Entry(new_entry, textvar=androidver)
    avEntry.place(x=670, y=410)
    avEntry.bind("<Return>", lambda event : validate(event, "Android Version"))
    avEntry.bind("<Tab>", lambda event : validate(event, "Android Version"))
    
    ratEntry.config(state='disabled')
    reEntry.config(state='disabled')
    sizeEntry.config(state='disabled')
    insEntry.config(state='disabled')
    typeEntry.config(state='disabled')
    priceEntry.config(state='disabled')
    conEntry.config(state='disabled')
    # luEntry.config(state='disabled')
    cvEntry.config(state='disabled')
    avEntry.config(state='disabled')
    Button(new_entry, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=lambda : check_entry(new_entry)).place(x=500, y=460)

def new_review():
    global application, trans_review, sentiment, senti_polarity, senti_subject
    global appEntry2, reviewEntry, sentEntry, polEntry, subEntry
    new_review = Toplevel(fig18)
    new_review.title("New Review")
    createWindow(new_review)
    application = StringVar(new_review)
    trans_review = StringVar(new_review)
    sentiment = StringVar(new_review)
    senti_polarity = StringVar(new_review)
    senti_subject = StringVar(new_review)

    Label(new_review, text="Enter a New App Review", width="500", height="2", font=Label_font, fg='white',bg='#800000').pack()
    Label(new_review, text="", bg='#1aff8c', width='80', height='30').place(x=50, y=120)
    
    Label(new_review, text="Application", font=("Open Sans", 11, 'bold'),fg='#004d26', bg='#1aff8c', anchor=W).place(x=130, y=160)
    appEntry2 = Entry(new_review, textvar=application)
    appEntry2.place(x=350, y=160)
    appEntry2.bind("<Return>", lambda event : validate(event, "Application"))
    appEntry2.bind("<Tab>", lambda event : validate(event, "Application"))
    
    Label(new_review, text="Translated Review", font=("Open Sans", 11, 'bold'),fg='#004d26', bg='#1aff8c',anchor=W).place(x=130, y=210)          
    reviewEntry = Entry(new_review, textvar=trans_review)
    reviewEntry.place(x=350, y=210)
    reviewEntry.bind("<Return>", lambda event : validate(event, "Translated Review"))
    reviewEntry.bind("<Tab>", lambda event : validate(event, "Translated Review"))
    
    Label(new_review, text="Sentiment", font=("Open Sans", 11, 'bold'),fg='#004d26', bg='#1aff8c', anchor=W).place(x=130,y=260)
    sentEntry = Entry(new_review, textvar=sentiment)
    sentEntry.place(x=350, y=260)
    list1 = ['Positive','Negative','Neutral']
    droplist = OptionMenu(new_review, sentiment, *list1)
    droplist.config(width=17)
    sentiment.set('--select sentiment --')
    droplist.place(x=350, y=260)
    sentEntry.bind("<Return>", lambda event : validate(event, "Sentiment"))
    sentEntry.bind("<Tab>", lambda event : validate(event, "Sentiment"))
    
    Label(new_review, text="Sentiment Polarity", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c',anchor=W).place(x=130, y=310)
    polEntry = Entry(new_review, textvar=senti_polarity)
    polEntry.place(x=350, y=310)
    polEntry.bind("<Return>", lambda event : validate(event, "Sentiment Polarity"))
    polEntry.bind("<Tab>", lambda event : validate(event, "Sentiment Polarity"))
    
    Label(new_review, text="Sentiment Subjectivity", font=("Open Sans", 11, 'bold'), fg='#004d26', bg='#1aff8c',anchor=W).place(x=130, y=360)
    subEntry = Entry(new_review, textvar=senti_subject)
    subEntry.place(x=350, y=360)
    subEntry.bind("<Return>", lambda event : validate(event, "Sentiment Subjectivity"))
    subEntry.bind("<Tab>", lambda event : validate(event, "Sentiment Subjectivity"))
    reviewEntry.config(state='disabled')
    sentEntry.config(state='disabled')
    polEntry.config(state='disabled')
    subEntry.config(state='disabled')    
    Button(new_review, text='Submit', width=15, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=lambda : check_review(new_review)).place(x=350, y=410)

def fig18():
    global fig18
    fig18 = Toplevel(home)
    fig18.title("QUESTION 18")
    createWindow(fig18)
    Label(fig18, text="Provide an interface to add new data to both the datasets provided.", width="170", height="5",font=Label1_font, fg='white', bg='#800000').place(x=0, y=0)
    b1 = Button(fig18, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    b2 = Button(fig18, text="New App Record", bg="#e79700", width="25", height="1", font=Button1_font, fg='white',command=new_entry).place(x=250, y=220)
    b3 = Button(fig18, text="Review App", bg="#e79700", width="25", height="1", font=Button1_font, fg='white',command=new_review).place(x=650, y=220)

    
    

    
    
def fig19():
    global fig19
    fig19=Tk()
    fig19.title("QUESTION 19")
    createWindow(fig19)
    Label(fig19,text="No of Installs for free apps and paid apps",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig19, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    f = Figure(figsize=(12, 8), dpi=80)
    a = f.add_subplot(111)

    a.pie(df['Type'].value_counts().values, autopct='%1.1f%%',pctdistance = 1.1 , labeldistance = 1.2)
    a.legend(df['Type'].value_counts().index, loc='center left', bbox_to_anchor=(1.04, 0.5), ncol=1)

    canvas = FigureCanvasTkAgg(f, fig19)
    canvas.get_tk_widget().place(x=5, y=100)
    canvas.draw()

    fig19.mainloop()

def fig20():
    global fig20
    fig20=Tk()
    fig20.title("QUESTION 20")
    createWindow(fig20)
    Label(fig20,text="Apps which have been given most reviews",width="120", height="5", font=Label1_font, fg='white', bg='#174873').place(x=0, y=0)
    b1 = Button(fig20, text="HOME PAGE", bg="#e79700", width="10", height="1", font=Button1_font, fg='white',command=backtohome).place(x=0, y=0)
    df['Reviews']=df['Reviews'].astype(int)
    top5reviews=df.nlargest(15,'Reviews')
    top5reviews = top5reviews.sort_values(by='Reviews', ascending=False).drop_duplicates('App')
    top5reviews.plot(x='App',y='Reviews', kind='bar')
    py.xlabel('Applications')
    py.ylabel('Reviews')
    py.title('Top 5 Applications with highest Reviews')
    f = Figure(figsize=(12, 8), dpi=80)
    canvas = FigureCanvasTkAgg(f, fig20)
    canvas.get_tk_widget().place(x=5, y=100)
    canvas.draw()
    

def home():
    global home
    home = Tk()
    home.title("HOMEPAGE")
    createWindow(home)
    l = Label(home, text="ANALYSIS OF GOOGLE PLAYSTORE", width="500", height="2", font=Label_font, fg='white',bg='#174873').pack()

    l1 = Label(home, text="Percentage download in each category", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=90)
    b1 = Button(home, text="FIG 1", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig1).place(x=25, y=90)

    l2 = Label(home, text="Number of Downloads", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=140)
    b2 = Button(home, text="FIG 2", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig2).place(x=25, y=140)

    l3 = Label(home, text="Most,Least,Average Category", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=190)
    b3 = Button(home, text="FIG 3", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig3).place(x=25, y=190)

    l4 = Label(home, text="Highest maximum average ratings", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=240)
    b4 = Button(home, text="FIG 4", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig4).place(x=25, y=240)

    l5 = Label(home, text="App according to Size", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=290)
    b5 = Button(home, text="FIG 5", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig5).place(x=25, y=290)

    l6 = Label(home, text="Downloads over period of three years", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=340)
    b6 = Button(home, text="FIG 6", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig6).place(x=25, y=340)

    l7 = Label(home, text="Android version is not an issue", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=390)
    b7 = Button(home, text="FIG 7", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig7).place(x=25, y=390)

    l8 = Label(home, text="Most likely to be downloaded", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=440)
    b8 = Button(home, text="FIG 8", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig8).place(x=25, y=440)

    l9 = Label(home, text="Co-relation of downloads & ratings", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=490)
    b9 = Button(home, text="FIG 9", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig9).place(x=25, y=490)

    l10 = Label(home, text="Qualifies as teen versus mature 17+.", width="40", height="1", font=Label_font, fg='white',bg='#174873').place(x=25, y=540)
    b10 = Button(home, text="FIG 10", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig10).place(x=25, y=540)

    l11 = Label(home, text="No of Installs in a Quater ", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=90)
    b11 = Button(home, text="FIG 11", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig11).place(x=650, y=90)

    l12 = Label(home, text="Generate most positive & negative sentiments", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=140)
    b12 = Button(home, text="FIG 12", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig12).place(x=650, y=140)

    l13 = Label(home, text="Relation between Sentiment-polarity & subjectivity ", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=190)
    b13 = Button(home, text="FIG 13", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig13).place(x=650, y=190)

    l14 = Label(home, text="Reviews categorized as positive,negative & neutral", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=240)
    b14 = Button(home, text="FIG 14", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig14).place(x=650, y=240)

    l15 = Label(home, text="Advisable to launch app like 10 Best foods for you?", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=290)
    b15 = Button(home, text="FIG 15", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig15).place(x=650, y=290)

    l16 = Label(home, text="Indicator to aver. downloads generated entire year?", width="50", height="1",font=Label_font, fg='white', bg='#174873').place(x=650, y=340)
    b16 = Button(home, text="FIG 16", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig16).place(x=650, y=340)

    l17 = Label(home, text="Size of App influence number of installs", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=390)
    b17 = Button(home, text="FIG 17", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig17).place(x=650, y=390)

    l18 = Label(home, text="Interface to add new data to both datasets", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=440)
    b18 = Button(home, text="FIG 18", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig18).place(x=650, y=440)
   
    l19 = Label(home, text="Apps Free vs Paid", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=490)
    b19 = Button(home, text="FIG 19", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig19).place(x=650, y=490)              
    
    l20 = Label(home, text="Most reviewed app", width="50", height="1", font=Label_font,fg='white', bg='#174873').place(x=650, y=540)
    b20 = Button(home, text="FIG 20", bg="#e79700", width="5", height="1", font=("Open Sans", 13, 'bold'), fg='white',command=fig20).place(x=650, y=540)

    
    home.mainloop()
#Calling the main function
home()

