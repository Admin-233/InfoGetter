import pdb
import gettercore
import numpy as np
import pandas as pd
from os import rename
from selenium import webdriver
import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
from _tkinter import TclError

frame_count=-1
frame_count_list=[]
frame_setup_frame_count=[]
framelist=[]
frame_sitelist=[]
frame_topagelist=[]
frame_setuplist=[]
frame_setup_framelist=[]
frame_setup_frame_Bylist=[]
frame_setup_frame_value1list=[]
frame_setup_frame_todolist=[]
frame_setup_frame_value2list=[]
frame_setup_frame_destorylist=[]
frame_finditeratorlist=[]
frame_filterlist=[]
frame_filter_framelist=[]
frame_filter_frame_destorylist=[]
frame_filter_frame_modelist=[]
frame_filter_frame_Bylist=[]
frame_filter_frame_value=[]
start_which=[]

def add_frame():
    global frame_count
    
    framelist.append(tk.Frame(root, borderwidth=1, relief="solid"))
    belongtoinaddframe=framelist[frame_count]
    belongtoinaddframe.pack(pady=5)
    label = tk.Label(belongtoinaddframe, text="欢迎使用InfoGetter \n")
    label.pack()
    
    label = tk.Label(belongtoinaddframe, text="目标地址:")
    label.pack()
    frame_sitelist.append(tk.Entry(belongtoinaddframe))
    frame_sitelist[frame_count].pack()

    label = tk.Label(belongtoinaddframe, text="筛选到页数(或者滑到底端的次数)")
    label.pack()
    frame_topagelist.append(tk.Entry(belongtoinaddframe))
    frame_topagelist[frame_count].pack()

    label = tk.Label(belongtoinaddframe, text="先执行的操作")
    label.pack()
    button = tk.Button(belongtoinaddframe, text="+", command=add_setup)#placeholder
    button.pack()
    
    frame_setuplist.append(tk.Frame(belongtoinaddframe, borderwidth=1, relief="solid"))
    frame_setuplist[frame_count].pack(pady=5)

    label = tk.Label(belongtoinaddframe, text="寻找页面列表")
    label.pack()
    try:
        frame_finditeratorlist[frame_count]
    except IndexError:
        frame_finditeratorlist.append([])
    frameforfinditerator = tk.Frame(belongtoinaddframe, borderwidth=1, relief="solid")
    frameforfinditerator.pack(pady=5)
    label = tk.Label(frameforfinditerator, text="以")
    label.pack(side='left')
    frame_finditeratorlist[frame_count].append(ttk.Combobox(frameforfinditerator, values=['划到页面最底端' ,'XPATH' ,'CLASS_NAME' ,'CSS_SELECTOR' ,'ID' ,'LINK_TEXT' ,'NAME' ,'PARTIAL_LINK_TEXT' ,'TAG_NAME']))
    frame_finditeratorlist[frame_count][-1].pack(side='left')
    label = tk.Label(frameforfinditerator, text="寻找")
    label.pack(side='left')
    frame_finditeratorlist[frame_count].append(ttk.Combobox(frameforfinditerator, values=['']))
    frame_finditeratorlist[frame_count][-1].pack(side='left')

    label = tk.Label(belongtoinaddframe, text="筛选结果")
    label.pack()
    button = tk.Button(belongtoinaddframe, text="+", command=add_filter)#placeholder
    button.pack()
    
    frame_filterlist.append(tk.Frame(belongtoinaddframe, borderwidth=1, relief="solid"))
    frame_filterlist[frame_count].pack(pady=5)
    
    label.pack()
    
    button = tk.Button(belongtoinaddframe, text="开始获取并导出", command=start_now)#lambda:start_now(start_which[frame_count]))#placeholder
    button.pack()
    
    frame_count+=1
    frame_count_list.append(frame_count)
    start_which.append(frame_count)
    
def add_setup():
    
    try:
        frame_setup_framelist[frame_count]
    except IndexError:
        frame_setup_framelist.append([])

    frame_setup_framelist[frame_count].append(tk.Frame(frame_setuplist[frame_count], borderwidth=1, relief="solid"))
    frame_setup_framelist[frame_count][-1].pack()

    belongto = frame_setup_framelist[frame_count][-1]
    try:
        frame_setup_frame_destorylist[frame_count]
    except IndexError:
        frame_setup_frame_destorylist.append([])
    try:
        frame_setup_frame_Bylist[frame_count]
    except IndexError:
        frame_setup_frame_Bylist.append([])
    try:
        frame_setup_frame_value1list[frame_count]
    except IndexError:
        frame_setup_frame_value1list.append([])
    try:
        frame_setup_frame_todolist[frame_count]
    except IndexError:
        frame_setup_frame_todolist.append([])
    try:
        frame_setup_frame_value2list[frame_count]
    except IndexError:
        frame_setup_frame_value2list.append([])

    label = tk.Label(belongto, text="以")
    label.pack(side='left')
    
    frame_setup_frame_Bylist[frame_count].append(ttk.Combobox(belongto, values=['XPATH' ,'CLASS_NAME' ,'CSS_SELECTOR' ,'ID' ,'LINK_TEXT' ,'NAME' ,'PARTIAL_LINK_TEXT' ,'TAG_NAME']))
    frame_setup_frame_Bylist[frame_count][-1].pack(side='left')
    
    label = tk.Label(belongto, text="寻找")
    label.pack(side='left')
    
    frame_setup_frame_value1list[frame_count].append(ttk.Combobox(belongto, values=['']))
    frame_setup_frame_value1list[frame_count][-1].pack(side='left')

    label = tk.Label(belongto, text="并且")
    label.pack(side='left')
    
    frame_setup_frame_todolist[frame_count].append(ttk.Combobox(belongto, values=['send_keys' ,'submit' ,'clear' ,'click' ,'等待秒数']))
    frame_setup_frame_todolist[frame_count][-1].pack(side='left')

    frame_setup_frame_value2list[frame_count].append(ttk.Combobox(belongto, values=['']))
    frame_setup_frame_value2list[frame_count][-1].pack(side='left')

    frame_setup_frame_destorylist[frame_count].append(belongto.destroy)
    delete_button = tk.Button(belongto, text="-", command=frame_setup_frame_destorylist[frame_count][-1])
    delete_button.pack()

    '''
    add_setup()#init setup
    frame_setup_frame_destorylist[-1][-1]()
    add_filter()#init filter
    frame_filter_frame_destorylist[-1][-1]()
    '''


def add_filter():
    
    try:
        frame_filter_framelist[frame_count]
    except IndexError:
        frame_filter_framelist.append([])

    frame_filter_framelist[frame_count].append(tk.Frame(frame_filterlist[frame_count], borderwidth=1, relief="solid"))
    frame_filter_framelist[frame_count][-1].pack()

    belongtoinaddfilter = frame_filter_framelist[frame_count][-1]
    try:
        frame_filter_frame_destorylist[frame_count]
    except IndexError:
        frame_filter_frame_destorylist.append([])
    try:
        frame_filter_frame_Bylist[frame_count]
    except IndexError:
        frame_filter_frame_Bylist.append([])
    try:
        frame_filter_frame_modelist[frame_count]
    except IndexError:
        frame_filter_frame_modelist.append([])
    try:
        frame_filter_frame_value[frame_count]
    except IndexError:
        frame_filter_frame_value.append([])

    label = tk.Label(belongtoinaddfilter, text="使用")
    label.pack(side='left')

    frame_filter_frame_modelist[frame_count].append(ttk.Combobox(belongtoinaddfilter, values=['寻找模式','删除模式']))
    frame_filter_frame_modelist[frame_count][-1].pack(side='left')
    
    label = tk.Label(belongtoinaddfilter, text="以")
    label.pack(side='left')
    
    frame_filter_frame_Bylist[frame_count].append(ttk.Combobox(belongtoinaddfilter, values=['XPATH' ,'CLASS_NAME' ,'CSS_SELECTOR' ,'ID' ,'LINK_TEXT' ,'NAME' ,'PARTIAL_LINK_TEXT' ,'TAG_NAME']))
    frame_filter_frame_Bylist[frame_count][-1].pack(side='left')
    
    label = tk.Label(belongtoinaddfilter, text="寻找")
    label.pack(side='left')

    frame_filter_frame_value[frame_count].append(ttk.Combobox(belongtoinaddfilter, values=['']))
    frame_filter_frame_value[frame_count][-1].pack(side='left')

    frame_filter_frame_destorylist[frame_count].append(belongtoinaddfilter.destroy)
    delete_button = tk.Button(belongtoinaddfilter, text="-", command=frame_filter_frame_destorylist[frame_count][-1])
    delete_button.pack()

def start_now(startindex = 0):
    
    try:
        frame_setup_framelist[startindex]
    except IndexError:
        frame_setup_framelist.append([])
    try:
        frame_filter_framelist[startindex]
    except IndexError:
        frame_filter_framelist.append([])
        
    site = frame_sitelist[startindex].get()
    topage = int(frame_topagelist[startindex].get())
    driver = webdriver.Chrome()
    setup = []
    iterator = []
    resultfilter=[]
    for i in range(len(frame_setup_framelist[startindex])):
        setup.append([])
        try:
            setup[-1].append(frame_setup_frame_Bylist[startindex][i].get())
            setup[-1].append(frame_setup_frame_value1list[startindex][i].get())
            setup[-1].append(frame_setup_frame_todolist[startindex][i].get())
            setup[-1].append(frame_setup_frame_value2list[startindex][i].get())
        except TclError:
            setup.pop()

    for i in frame_finditeratorlist:
        iterator.append(frame_finditeratorlist[startindex][0].get())
        iterator.append(frame_finditeratorlist[startindex][1].get())


    try:
        for i in range(len(frame_filter_framelist[startindex])):
            resultfilter.append([])
            resultfilter[-1].append(frame_filter_frame_modelist[startindex][i].get())
            resultfilter[-1].append(frame_filter_frame_Bylist[startindex][i].get())
            resultfilter[-1].append(frame_filter_frame_value[startindex][i].get())
    except TclError:
        resultfilter.pop()

    print(site,'\n',setup,'\n',iterator,'\n',resultfilter,'\n',topage,'\n',driver)
    resultlist=gettercore.starttoget(site,setup,iterator,resultfilter,topage,driver)
    data = pd.DataFrame({'Result':np.array(resultlist)})
    data.to_excel(asksaveasfilename()+'.xlsx')

def load_config(startindex = 0):
    configlists = np.load(askopenfilename())
    for i in range(5):
        if i == 0:site = configlists["arr_{0}".format(i)].tolist()
        if i == 1:topage = configlists["arr_{0}".format(i)].tolist()
        if i == 2:setup = configlists["arr_{0}".format(i)].tolist()
        if i == 3:iterator = configlists["arr_{0}".format(i)].tolist()
        if i == 4:resultfilter = configlists["arr_{0}".format(i)].tolist()
    frame_sitelist[startindex].delete(0,'end')
    frame_sitelist[startindex].insert(0,site)
    frame_topagelist[startindex].delete(0,'end')
    frame_topagelist[startindex].insert(0,topage)
    for i in range(len(setup)):
        add_setup()
        frame_setup_frame_Bylist[startindex][i].delete(0,'end')
        frame_setup_frame_Bylist[startindex][i].insert(0,setup[i][0])
        frame_setup_frame_value1list[startindex][i].delete(0,'end')
        frame_setup_frame_value1list[startindex][i].insert(0,setup[i][1])
        frame_setup_frame_todolist[startindex][i].delete(0,'end')
        frame_setup_frame_todolist[startindex][i].insert(0,setup[i][2])
        frame_setup_frame_value2list[startindex][i].delete(0,'end')
        frame_setup_frame_value2list[startindex][i].insert(0,setup[i][3])
    frame_finditeratorlist[startindex][0].delete(0,'end')
    frame_finditeratorlist[startindex][0].insert(0,iterator[0])
    frame_finditeratorlist[startindex][1].delete(0,'end')
    frame_finditeratorlist[startindex][1].insert(0,iterator[1])
    for i in range(len(resultfilter)):
        add_filter()
        frame_filter_frame_modelist[startindex][i].delete(0,'end')
        frame_filter_frame_modelist[startindex][i].insert(0,resultfilter[i][0])
        frame_filter_frame_Bylist[startindex][i].delete(0,'end')
        frame_filter_frame_Bylist[startindex][i].insert(0,resultfilter[i][1])
        frame_filter_frame_value[startindex][i].delete(0,'end')
        frame_filter_frame_value[startindex][i].insert(0,resultfilter[i][2])
        
def export_config(startindex = 0):#Because of some reason ,only frame one's config can be read

    try:
        frame_setup_framelist[startindex]
    except IndexError:
        frame_setup_framelist.append([])
    try:
        frame_filter_framelist[startindex]
    except IndexError:
        frame_filter_framelist.append([])

    site = frame_sitelist[startindex].get()
    topage = int(frame_topagelist[startindex].get())
    setup = []
    iterator = []
    resultfilter=[]
    for i in range(len(frame_setup_framelist[startindex])):
        setup.append([])
        try:
            setup[-1].append(frame_setup_frame_Bylist[startindex][i].get())
            setup[-1].append(frame_setup_frame_value1list[startindex][i].get())
            setup[-1].append(frame_setup_frame_todolist[startindex][i].get())
            setup[-1].append(frame_setup_frame_value2list[startindex][i].get())
        except TclError:
            setup.pop()

    for i in frame_finditeratorlist:
        iterator.append(frame_finditeratorlist[startindex][0].get())
        iterator.append(frame_finditeratorlist[startindex][1].get())


    try:
        for i in range(len(frame_filter_framelist[startindex])):
            resultfilter.append([])
            resultfilter[-1].append(frame_filter_frame_modelist[startindex][i].get())
            resultfilter[-1].append(frame_filter_frame_Bylist[startindex][i].get())
            resultfilter[-1].append(frame_filter_frame_value[startindex][i].get())
    except TclError:
        resultfilter.pop()
    npsite = np.array(site)
    nptopage = np.array(topage)
    npsetup = np.array(setup)
    npiterator = np.array(iterator)
    npresultfilter = np.array(resultfilter)
    configfilename = asksaveasfilename()
    if configfilename[-13:] == '.getterconfig':
        configfilename=configfilename[:-13]
    np.savez(configfilename,npsite,nptopage,npsetup,npiterator,npresultfilter)
    try:rename(configfilename+'.npz',configfilename+'.getterconfig')
    except FileNotFoundError:pass
        
        
def download_driver1():
    tk.messagebox.showinfo(title='Link',message='https://chromedriver.storage.googleapis.com/index.html?path=111.0.5563.19/')
def download_driver2():
    tk.messagebox.showinfo(title='Link',message='https://chromedriver.storage.googleapis.com/index.html?path=110.0.5481.77/')
def download_driver3():
    tk.messagebox.showinfo(title='Link',message='https://chromedriver.storage.googleapis.com/index.html?path=109.0.5414.74/')
#主程序
root = tk.Tk()

root.title("InfoGetter")
menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu2 = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="载入配置" ,command = load_config)
filemenu.add_command(label="导出配置" ,command = export_config)
filemenu2.add_command(label='在浏览器中输入Chrome://version以查看版本')
filemenu2.add_command(label='ChromeDriver 111' ,command = download_driver1)
filemenu2.add_command(label='ChromeDriver 110' ,command = download_driver2)
filemenu2.add_command(label='ChromeDriver 109' ,command = download_driver3)
menubar.add_cascade(label="文件", menu=filemenu)
menubar.add_cascade(label='下载ChromeDriver.exe', menu=filemenu2)

root.config(menu=menubar)

add_frame()#Because of some reason ,more frame are not support yet


root.mainloop()