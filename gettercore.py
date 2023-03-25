from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from time import sleep
#import pdb
def starttoget(site,setup,iterator,resultfilter,topage,driver):
    

    
    driver.get(site)

    for i in setup:#只运行一次的内容
        if i[2] == '等待秒数':
            sleep(float(i[3]))
        else:
            element = eval('''driver.find_element(By.{0},'{1}')'''.format(i[0] ,i[1]))
            if i[2] == 'click':
                command = "element.click()"
            else:
                command = "element.{0}('{1}')".format(i[2],i[3])
            print(command)
            command = command.replace('\n', '\\n')
            eval(command)
            sleep(0.5)

    sleep(1)

    resultlist = []
    totalresult = []
    slidetobottom=False
    for i in range(topage):
        print('now i is',i)
        resultlist = []

        print('tracepoint1')
        #开始跳转页面
        stopgotopage = False
        if iterator[0] == '划到页面最底端':
            pagelist=[]
            slidetobottom=True
        else:
            pagelistelement = eval('''driver.find_element(By.{0},'{1}')'''.format(iterator[0] ,iterator[1]))
            pagelist = pagelistelement.find_elements(By.XPATH,'./*')
        print(len(pagelist))
        '''
        while len(pagelist) <= 2:
            sleep(1)
            pagelist = pagelist[0].find_elements(By.XPATH,'./*')
        try:
            while 1:
                for i2 in range(len(pagelist)):
                    pagelist[i2]=pagelist[i2].find_element(By.XPATH,'./*')
        except NoSuchElementException:
            pass
        '''
        print('tracepoint2')
        if len(pagelist) == 0 or len(pagelist) == 1 or topage == 0 or topage == 1:
            print('没有页面或页面为空')
            stopgotopage = True
        print('tracepoint3 and len pagelist',len(pagelist))
        loopbreaklabel = False    
        while stopgotopage == False and slidetobottom == False:
            #pdb.set_trace()
            for i2 in pagelist:
                print('tracepoint4 and i2',i2.text)
                if str(i+1) in i2.text:
                    i2.click()
                    loopbreaklabel = True
                    break
            sleep(1)
            if loopbreaklabel == True:break
            pagelist[-1].click()
        if slidetobottom == True:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(1)
        loopbreaklabel= False
        
        print(i+1,'gotoed')
        #开始获取内容
        for i in resultfilter:
            if i[0] == '寻找模式':
                print('now finding')
                sleep(2)#确保良好的网络以在两秒之内加载完成页面
                resultlist = eval('''driver.find_elements(By.{0},"{1}")'''.format(i[1],i[2]))
            if i[0] == '删除模式':
                resultlist = eval('''list(set(resultlist) - set(driver.find_elements(By.{0},"{1}")))'''.format(i[1],i[2]))
        #整合
        for i in resultlist:
            if i.text != '':
                totalresult.append(i.text)
        print(len(totalresult))
    #去重并输出
    totalresultnodup = list(set(totalresult))
    totalresultnodup.sort(key = totalresult.index)
    return totalresultnodup