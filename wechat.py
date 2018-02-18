# encoding: utf-8
import itchat
import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib as mpl  
from matplotlib.font_manager import FontManager, FontProperties 

# login in your wechat
itchat.login()
friends = itchat.get_friends(update = True)[0:]
male = 0
female = 0
other = 0
total = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = male + female + other

# for Chinese support
def getChineseFont():  
    return FontProperties(fname='fonts/STKAITI.TTF')  
def draw_it(labels,quants):  
    plt.figure(figsize=(6,8))
    sizes = quants
    colors = ['blue','pink','green']
    explode = (0.05,0,0)
    patches,l_text,p_text = plt.pie(sizes,explode=explode,labels=labels,colors=colors,
                                labeldistance = 1.1,autopct = '%3.1f%%',shadow = False,
                                startangle = 90,pctdistance = 0.6)
    for t in l_text:
        t.set_size=(30)
    for t in p_text:
        t.set_size=(20)
    plt.title(u'微信好友性别分布',fontproperties=getChineseFont())
    plt.axis('equal')
    plt.legend()
    plt.show()
  
labels = [u'Males', u'Females', u'Others']
quants = [float(male)/total * 100, float(female)/total * 100, float(other)/total * 100]   
draw_it(labels,quants) 