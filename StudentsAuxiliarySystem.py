# -*- coding: cp936 -*-
__author__ = 'now2112'


import urllib
import urllib2
import cookielib
import re
import string
import os
import sys
import msvcrt
import itertools

def pwd_input():
    chars = []
    while True:
        newChar = msvcrt.getch()
        if newChar in '\r\n': # 如果是换行，则输入结束
            print ''
            break
        elif newChar == '\b': # 如果是退格，则删除末尾一位
            if chars:
                del chars[-1]
                sys.stdout.write('\b \b') # 删除一个星号
        else:
            chars.append(newChar)
            sys.stdout.write('*') # 显示为星号
    ''.join(chars)
    return chars

class DUT:
    
    def __init__(self):
        #welcome
        self.welcome_name = []
        self.welcome_name_ = []
        self.welcome_name0 = []
        self.welcome_name0_ = []
        self.welcome_ = []
        #grade
        self.lesson_num0 = []
        self.lesson_num0_ = []
        self.lesson_num1 = []
        self.lesson_num1_ = []
        self.lesson = []
        self.lesson_ = []
        self.en_lesson = []
        self.en_lesson_ = []
        self.credit = []
        self.credit_ = []
        self.property = []
        self.property_ = []
        self.grade = []
        self.grade_ = []
        self.reason = []
        self.reason_ = []
        self.sumlesson = []
        self.wrong = []
        #now_grade
        self.now_lesson_num0 = []
        self.now_lesson_num0_ = []
        self.now_lesson_num1 = []
        self.now_lesson_num1_ = []
        self.now_lesson = []
        self.now_lesson_ = []
        self.now_en_lesson = []
        self.now_en_lesson_ = []
        self.now_credit = []
        self.now_credit_ = []
        self.now_property = []
        self.now_property_ = []
        self.now_grade = []
        self.now_grade_ = []
        self.now_sumlesson = []
        #lesson
        self.num_lesson = []
        self.Monday = []
        self.Tuesday = []
        self.Wednesday = []
        self.Thursday = []
        self.Friday = []
        self.Saturday = []
        self.Sunday = []
        self.num_lesson_ = []
        self.Monday_ = []
        self.Tuesday_ = []
        self.Wednesday_ = []
        self.Thursday_ = []
        self.Friday_ = []
        self.Saturday_ = []
        self.Sunday_ = []
        self.lessontable = []
        self.lessontable_ = []
        #news
        self.important_newsurl = []
        self.title = []
        self.newsdate = []
        self.newsdate_ = []
        
        self.urlfile = file("url.txt","w")
        
        self.importantnewsUrl = 'http://teach.dlut.edu.cn/zyxx.htm'
        self.importantnewsUrl0 = 'http://teach.dlut.edu.cn/zyxx/4.htm'
        self.importantnewsUrl1 = 'http://teach.dlut.edu.cn/zyxx/3.htm'
        self.importantnewsUrl2 = 'http://teach.dlut.edu.cn/zyxx/2.htm'
        self.importantnewsUrl3 = 'http://teach.dlut.edu.cn/zyxx/1.htm'
        #登录URL
        self.loginUrl = 'http://202.118.65.20:8089/loginAction.do'
        #成绩URL
        self.gradeUrl = 'http://202.118.65.20:8089/gradeLnAllAction.do?\
type=ln&oper=fa'
        #课表URL
        self.lessonUrl = 'http://202.118.65.20:8089/xkAction.do?actionType=6'
        #本学期成绩URL
        self.grade_nowUrl = 'http://202.118.65.20:8089/bxqcjcxAction.do'
        #欢迎
        self.welcomeUrl = 'http://202.118.65.20:8089/menu/s_top.jsp'
        
        self.cookies = cookielib.CookieJar()
        #表单数据
        while True:
            j = os.system('cls')
            self.wrong = []
            while True:
                j = os.system('cls')
                zjh = raw_input("请输入学号:")
                if zjh != '':
                    break
                print "学号不能为空!"
                xxx = raw_input("只有回车才能返回!")
            print "请输入密码:",
            pwd = pwd_input()
            mm = "".join(itertools.chain(*pwd))
            self.postdata = urllib.urlencode({
                    'zjh' : zjh,
                    'mm' : mm
            })
            
            self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor\
                                                   (self.cookies))
            
            request = urllib2.Request(
                    url = self.loginUrl,
                    data = self.postdata
            )
            
            result = self.opener.open(request)
            page_ = result.read().decode('gbk')
            pattern_ = re.compile('<td class="errorTop.*?<strong.*?\
<font.*?>(.*?)</font.*?</strong.*?<br.*?</td>',re.S)
            
            myItems_ = re.findall(pattern_,page_)
            
            for i in myItems_:
                self.wrong.append(i)
                
            if self.wrong:
                for i in self.wrong:
                    print i
                    xxx = raw_input("只有回车才能返回!")
                    
            if not(self.wrong):
                break
        
        j = os.system('cls')

    #欢迎界面
    def getPage_welcome(self):

        result = self.opener.open(self.welcomeUrl)

        return result.read().decode('gbk')

    #获取成绩页面
    def getPage_grade(self):
        
        result = self.opener.open(self.gradeUrl)
        page_get = result.read().decode('gbk')
        pattern_get = re.compile('<td.*?valign="top".*?\
width="80.*?<iframe.*?name="lnfaIfra".*?\
src="(.*?)".*?width="100.*?height="490.*?scrolling="0.*?\
frameborder="0.*?align="center.*?</iframe>',re.S)
        myItems_get = re.findall(pattern_get,page_get)
        for item in myItems_get:
            self.gradeUrl = 'http://202.118.65.20:8089/' + item
        
        result = self.opener.open(self.gradeUrl)
        
        return result.read().decode('gbk')
    
    #获取本学期成绩页面
    def getPage_grade_now(self):

        result = self.opener.open(self.grade_nowUrl)

        return result.read().decode('gbk')
    
    #获取课表页面
    def getPage_lesson(self):

        result = self.opener.open(self.lessonUrl)

        return result.read().decode('gbk')
    #欢迎部分
    def getWelcome(self):
        page = self.getPage_welcome()
        pattern = re.compile('<td.*?nowrap>&nbsp;(.*?)&nbsp;(.*?)\
<a.*?href.*?</a>',re.S)

        myItems = re.findall(pattern,page)
        for item in myItems:
            self.welcome_name.append(item[0].encode('gbk'))
            self.welcome_name0.append(item[1].encode('gbk'))
        for i in range(len(self.welcome_name)):
            self.welcome_name[i] = self.welcome_name[i].replace("&nbsp"," ")
            self.welcome_name[i] = self.welcome_name[i].replace(";"," ")
            self.welcome_name_.append("".join(self.welcome_name[i].split()))
        for i in range(len(self.welcome_name0)):
            self.welcome_name0[i] = self.welcome_name0[i].replace("&nbsp"," ")
            self.welcome_name0[i] = self.welcome_name0[i].replace(";"," ")
            self.welcome_name0[i] = self.welcome_name0[i].replace("|"," ")
            self.welcome_name0_.append("".join(self.welcome_name0[i].split()))


        j = self.welcome_name_[0] + ' ' + self.welcome_name0_[0]
        print j
        print '\n'
    #获取所有成绩
    def getGrades(self):
        page = self.getPage_grade()
        pattern = re.compile('<tr.*?class="odd.*?<td.*?align="center.*?>(.*?)\
</td>.*?<td.*?align="center.*?>(.*?)</td>.*?<td.*?align="center.*?>(.*?)\
</td>.*?<td.*?align="center.*?>(.*?)</td>.*?<td.*?align="center.*?>(.*?)\
</td>.*?<td.*?align="center.*?>(.*?)</td>.*?<td.*?align="center.*?\
<p.*?align="center.*?>(.*?)</P>.*?</td>.*?<td>.*?<p.*?align="center.*?>(.*?)\
</P>.*?</td>.*?</tr>',re.S)
        
        myItems = re.findall(pattern,page)
        for item in myItems:
            self.lesson_num0.append(item[0].encode('gbk'))
            self.lesson_num1.append(item[1].encode('gbk'))
            self.lesson.append(item[2].encode('gbk'))
            self.en_lesson.append(item[3].encode('gbk'))
            self.credit.append(item[4].encode('gbk'))
            self.property.append(item[5].encode('gbk'))
            self.grade.append(item[6].encode('gbk'))
            self.reason.append(item[7].encode('gbk'))

        for i in range(len(self.lesson_num0)):
            self.lesson_num0_.append("".join(self.lesson_num0[i].split()))
            
        for i in range(len(self.lesson_num1)):
            self.lesson_num1_.append("".join(self.lesson_num1[i].split()))
            
        for i in range(len(self.lesson)):
            self.lesson_.append("".join(self.lesson[i].split()))
            
        for i in range(len(self.en_lesson)):
            self.en_lesson_.append("".join(self.en_lesson[i].split()))
            
        for i in range(len(self.credit)):
            self.credit_.append("".join(self.credit[i].split()))
            
        for i in range(len(self.property)):
            self.property_.append("".join(self.property[i].split()))
            
        for i in range(len(self.grade)):
            self.grade[i] = self.grade[i].replace("&nbsp;"," ")
            self.grade_.append("".join(self.grade[i].split()))
            
        for i in range(len(self.reason)):
            self.reason_.append("".join(self.reason[i].split()))
            
        for i in range(len(self.lesson_num0)):
            self.sumlesson.append(self.lesson_num0_[i] + \
                                  ' ' + self.lesson_num1_[i] + \
                                  ' ' + self.lesson_[i] + ' ' \
                                  + self.en_lesson_[i] + ' ' \
                                  + self.credit_[i] + ' ' + \
                                  self.property_[i] + ' ' + \
                                  self.grade_[i] + ' ' + self.reason_[i] \
                                  + '\n')
            
        for j in self.sumlesson:
            print j
            
        self.getGrade()
    #计算所有成绩    
    def getGrade(self):
        summ = 0.0
        summ_ = 0.0
        weight = 0.0
        weight_ = 0.0
        for i in range(len(self.credit_)):
            if self.grade_[i].isdigit() :
                summ += string.atof(self.credit_[i])*string.atof(self.grade_[i])
                weight += string.atof(self.credit_[i])
            else:
                string.atof(self.credit_[i])
                string.atof(self.grade_[i])
                summ += string.atof(self.credit_[i])*string.atof(self.grade_[i])
                weight += string.atof(self.credit_[i])
        for i in range(len(self.credit)):
            if self.property_[i] == '必修' :
                summ_ += string.atof(self.credit_[i])*string.atof(self.grade_[i])
                weight_ += string.atof(self.credit_[i])
        
        print u"加权总分", summ
        print u"总学分", weight
        print u"加权平均分:", summ / weight
        print u"必修加权总分", summ_
        print u"必修总学分", weight_
        print u"必修加权平均分", summ_ / weight_
    #获取本学期成绩
    def getGrades_now(self):
        page = self.getPage_grade_now()
        pattern = re.compile('<tr.*?class="odd.*?>.*?\
<td.*?align="center.*?>(.*?)</td>.*?<td.*?align="center.*?>(.*?)\
</td>.*?<td.*?align="center.*?>(.*?)</td>.*?<td.*?align="center.*?>(.*?)\
</td>.*?<td.*?align="center.*?>(.*?)</td>.*?<td.*?align="center.*?>(.*?)\
</td>.*?<td.*?align="center.*?>(.*?)</td>.*?</tr>',re.S)
        myItems = re.findall(pattern,page)
        for item in myItems:
            self.now_lesson_num0.append(item[0].encode('gbk'))
            self.now_lesson_num1.append(item[1].encode('gbk'))
            self.now_lesson.append(item[2].encode('gbk'))
            self.now_en_lesson.append(item[3].encode('gbk'))
            self.now_credit.append(item[4].encode('gbk'))
            self.now_property.append(item[5].encode('gbk'))
            self.now_grade.append(item[6].encode('gbk'))

        for i in range(len(self.now_lesson_num0)):
            self.now_lesson_num0_.append("".join(self.now_lesson_num0[i].\
                                                 split()))
            
        for i in range(len(self.now_lesson_num1)):
            self.now_lesson_num1_.append("".join(self.now_lesson_num1[i].\
                                                 split()))
            
        for i in range(len(self.now_lesson)):
            self.now_lesson_.append("".join(self.now_lesson[i].\
                                                 split()))
            
        for i in range(len(self.now_en_lesson)):
            self.now_en_lesson_.append("".join(self.now_en_lesson[i].\
                                                 split()))
            
        for i in range(len(self.now_credit)):
            self.now_credit_.append("".join(self.now_credit[i].\
                                                 split()))
            
        for i in range(len(self.now_property)):
            self.now_property_.append("".join(self.now_property[i].\
                                                 split()))
            
        for i in range(len(self.now_grade)):
            self.now_grade_.append("".join(self.now_grade[i].\
                                                 split()))

        for i in range(len(self.now_lesson_num0)):
            self.now_sumlesson.append(self.now_lesson_num0_[i] + \
                                    ' ' + self.now_lesson_num1_[i] + \
                                    ' ' + self.now_lesson_[i] + \
                                    ' ' + self.now_en_lesson_[i] + \
                                    ' ' + self.now_credit_[i] + \
                                    ' ' + self.now_property_[i] + \
                                    ' ' + self.now_grade_[i] + '\n')
        
        for i in self.now_sumlesson:
            print i
        
        self.getGrade_now()
    #计算本学期成绩    
    def getGrade_now(self):
        now_summ = 0.0
        now_summ_ = 0.0
        now_weight = 0.0
        now_weight_ = 0.0
        for i in range(len(self.now_credit_)):
            if self.now_grade_[i].isdigit():
                now_summ += string.atof(self.now_credit_[i])*string.atof(self.now_grade_[i])
                now_weight += string.atof(self.now_credit_[i])
            elif self.now_grade_[i]:
                string.atof(self.now_credit_[i])
                string.atof(self.now_grade_[i])
                now_summ += string.atof(self.now_credit_[i])*string.atof(self.now_grade_[i])
                now_weight += string.atof(self.now_credit_[i])
        for i in range(len(self.now_credit)):
            if self.now_property_[i] == '必修':
                if self.now_grade_[i]:
                    now_summ_ += string.atof(self.now_credit_[i])*string.atof(self.now_grade_[i])
                    now_weight_ += string.atof(self.now_credit_[i])
        print u"本学期已出分课程加权总分", now_summ
        print u"本学期已出分课程总学分", now_weight
        print u"本学期已出分课程加权平均分:", now_summ / now_weight
        print u"本学期已出分必修课程加权总分", now_summ_
        print u"本学期已出分必修课程总学分", now_weight_
        print u"本学期已出分必修课程加权平均分", now_summ_ / now_weight_
    #获取课表
    def getLesson(self):
        page = self.getPage_lesson()
        #print page
        pattern = re.compile('<tr.*?<td.*?width="11.*?>(.*?)\
</td.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)\
</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?</tr>',re.S)
        myItems = re.findall(pattern,page)
        #for i in myItems:
        #    print i
        for item in myItems:
            self.num_lesson.append(item[0].encode('gbk'))
            self.Monday.append(item[1].encode('gbk'))
            self.Tuesday.append(item[2].encode('gbk'))
            self.Wednesday.append(item[3].encode('gbk'))
            self.Thursday.append(item[4].encode('gbk'))
            self.Friday.append(item[5].encode('gbk'))
            self.Saturday.append(item[6].encode('gbk'))
            self.Sunday.append(item[7].encode('gbk'))
        for i in range(len(self.num_lesson)):
            self.num_lesson_.append("".join(self.num_lesson[i].split()))
            
        for i in range(len(self.Monday)):
            self.Monday[i] = self.Monday[i].replace("&nbsp"," ")
            self.Monday[i] = self.Monday[i].replace(";"," ")
            self.Monday[i] = self.Monday[i].replace("<br>"," ")
            self.Monday_.append("".join(self.Monday[i].split()))
            
        for i in range(len(self.Tuesday)):
            self.Tuesday[i] = self.Tuesday[i].replace("&nbsp"," ")
            self.Tuesday[i] = self.Tuesday[i].replace(";"," ")
            self.Tuesday[i] = self.Tuesday[i].replace("<br>"," ")
            self.Tuesday_.append("".join(self.Tuesday[i].split()))
            
        for i in range(len(self.Wednesday)):
            self.Wednesday[i] = self.Wednesday[i].replace("&nbsp"," ")
            self.Wednesday[i] = self.Wednesday[i].replace(";"," ")
            self.Wednesday[i] = self.Wednesday[i].replace("<br>"," ")
            self.Wednesday_.append("".join(self.Wednesday[i].split()))
            
        for i in range(len(self.Thursday)):
            self.Thursday[i] = self.Thursday[i].replace("&nbsp"," ")
            self.Thursday[i] = self.Thursday[i].replace(";"," ")
            self.Thursday[i] = self.Thursday[i].replace("<br>"," ")
            self.Thursday_.append("".join(self.Thursday[i].split()))
            
        for i in range(len(self.Friday)):
            self.Friday[i] = self.Friday[i].replace("&nbsp"," ")
            self.Friday[i] = self.Friday[i].replace(";"," ")
            self.Friday[i] = self.Friday[i].replace("<br>"," ")
            self.Friday_.append("".join(self.Friday[i].split()))
            
        for i in range(len(self.Saturday)):
            self.Saturday[i] = self.Saturday[i].replace("&nbsp"," ")
            self.Saturday[i] = self.Saturday[i].replace(";"," ")
            self.Saturday[i] = self.Saturday[i].replace("<br>"," ")
            self.Saturday_.append("".join(self.Saturday[i].split()))
            
        for i in range(len(self.Sunday)):
            self.Sunday[i] = self.Sunday[i].replace("&nbsp"," ")
            self.Sunday[i] = self.Sunday[i].replace(";"," ")
            self.Sunday[i] = self.Sunday[i].replace("<br>"," ")
            self.Sunday_.append("".join(self.Sunday[i].split()))
            
        #for i in self.Monday_:
        #    print i
        for i in range(len(self.num_lesson)):
            self.lessontable.append(self.num_lesson_[i] + \
                                    ' ' + self.Monday_[i] + \
                                    ' ' + self.Tuesday_[i] + \
                                    ' ' + self.Wednesday_[i] + \
                                    ' ' + self.Thursday_[i] + \
                                    ' ' + self.Friday_[i] + \
                                    ' ' + self.Saturday_[i] + \
                                    ' ' + self.Sunday_[i] + '\n')
        while True:
            j = os.system('cls')
            print '周一到周日对应1到7,输入0退出'
            ch = input("请输入序号后回车:")
            if ch == 1:
                j = os.system('cls')
                for i in range(len(self.num_lesson)):
                    self.lessontable_.append(self.num_lesson_[i] + \
                                             ' ' + self.Monday_[i] + '\n')
                for i in self.lessontable_:
                    print i
                xxx = raw_input("只有回车才能返回!")
                self.lessontable_ = []
            elif ch == 2:
                j = os.system('cls')
                for i in range(len(self.num_lesson)):
                    self.lessontable_.append(self.num_lesson_[i] + \
                                             ' ' + self.Tuesday_[i] + '\n')
                for i in self.lessontable_:
                    print i
                xxx = raw_input("只有回车才能返回!")
                self.lessontable_ = []
            elif ch == 3:
                j = os.system('cls')
                for i in range(len(self.num_lesson)):
                    self.lessontable_.append(self.num_lesson_[i] + \
                                             ' ' + self.Wednesday_[i] + '\n')
                for i in self.lessontable_:
                    print i
                xxx = raw_input("只有回车才能返回!")
                self.lessontable_ = []
            elif ch == 4:
                j = os.system('cls')
                for i in range(len(self.num_lesson)):
                    self.lessontable_.append(self.num_lesson_[i] + \
                                             ' ' + self.Thursday_[i] + '\n')
                for i in self.lessontable_:
                    print i
                xxx = raw_input("只有回车才能返回!")
                self.lessontable_ = []
            elif ch == 5:
                j = os.system('cls')
                for i in range(len(self.num_lesson)):
                    self.lessontable_.append(self.num_lesson_[i] + \
                                             ' ' + self.Friday_[i] + '\n')
                for i in self.lessontable_:
                    print i
                xxx = raw_input("只有回车才能返回!")
                self.lessontable_ = []
            elif ch == 6:
                j = os.system('cls')
                for i in range(len(self.num_lesson)):
                    self.lessontable_.append(self.num_lesson_[i] + \
                                             ' ' + self.Saturday_[i] + '\n')
                for i in self.lessontable_:
                    print i
                xxx = raw_input("只有回车才能返回!")
                self.lessontable_ = []
            elif ch == 7:
                j = os.system('cls')
                for i in range(len(self.num_lesson)):
                    self.lessontable_.append(self.num_lesson_[i] + \
                                             ' ' + self.Sunday_[i] + '\n')
                for i in self.lessontable_:
                    print i
                xxx = raw_input("只有回车才能返回!")
                self.lessontable_ = []
            elif ch == 0:
                break
            else:
                j = os.system('cls')
                print "输入错误,请重新输入!"
                xxx = raw_input("只有回车才能返回!")
        #for i in self.lessontable:
        #    print i

    #获取重要信息页面1
    def getPage_importantnews(self):

        result = self.opener.open(self.importantnewsUrl)

        return result.read().decode('utf-8').encode('gbk','ignore')
    #获取重要信息页面2
    def getPage_importantnews0(self):

        result = self.opener.open(self.importantnewsUrl0)

        return result.read().decode('utf-8').encode('gbk','ignore')
    #获取重要信息页面3
    def getPage_importantnews1(self):

        result = self.opener.open(self.importantnewsUrl1)

        return result.read().decode('utf-8').encode('gbk','ignore')
    #获取重要信息页面4
    def getPage_importantnews2(self):

        result = self.opener.open(self.importantnewsUrl2)

        return result.read().decode('utf-8').encode('gbk','ignore')
    #获取重要信息页面5
    def getPage_importantnews3(self):

        result = self.opener.open(self.importantnewsUrl3)

        return result.read().decode('utf-8').encode('gbk','ignore')
    #整理重要信息
    def getInformation(self):

        page = self.getPage_importantnews()
        page0 = self.getPage_importantnews0()
        page1 = self.getPage_importantnews1()
        page2 = self.getPage_importantnews2()
        page3 = self.getPage_importantnews3()
        
        page_ = page + page0 + page1 + page2 + page3
        
        pattern = re.compile('</a>.*?<a.*?href="(.*?)".*?class="c66617".*?\
target="_blank.*?title="(.*?)".*?</a>.*?<span.*?class="c66617.*?>.*?<br>.*?\
<span.*?style="color.*?>(.*?)</span>',re.S)
        
        myItems = re.findall(pattern,page_)
        
        for item in myItems:
           self.important_newsurl.append(item[0])
           self.title.append(item[1])
           self.newsdate.append(item[2])

        for i in range(len(self.newsdate)):
            self.newsdate[i] = self.newsdate[i].replace("&nbsp"," ")
            self.newsdate[i] = self.newsdate[i].replace(";"," ")
            self.newsdate_.append("".join(self.newsdate[i].split()))
        
        for i in range(len(self.title)):
            #content = self.newsdate_[i] + ' ' + self.title[i] + ':\n' + \
            #                    self.important_newsurl[i] + \
            #                    '\n********************************************************\n'
            #if 'http://teach.dlut.edu.cn/' in content:
            #    self.urlfile.write(content)
            #else:
                content = self.newsdate_[i] + ' ' + self.title[i] + ':\n' + \
                                'http://teach.dlut.edu.cn/' + \
                                self.important_newsurl[i] + \
                                '\n********************************************************\n'
                self.urlfile.write(content)

#程序框架
print "                     纯爬虫实现大工助手部分功能(简陋版)v1.1"
print "                                                         by now2112"
print "\n"
xxx = raw_input("只有回车才能继续!")
dut = DUT()
while True:
    j = os.system('cls')
    dut.getWelcome()
    print '                     纯爬虫实现大工助手部分功能(简陋版)v1.1'
    print '\n'
    print '1.查所有成绩并计算加权平均                   3.查本学期成绩并计算加权平均'
    print '2.查看本学期课表                             4.查看教务处重要通知'
    print '                                 0.退出'
    ch = raw_input("请输入序号后回车:")
    if ch == '1':
        j = os.system('cls')
        dut.getGrades()
        print "\n"
        xxx = raw_input("只有回车才能返回!")
    elif ch == '2':
        j = os.system('cls')
        dut.getLesson()
        print "注:若课表为空，则是教务处已清空本学期课表信息"
        print "\n"
        xxx = raw_input("只有回车才能返回!")
    elif ch == '3':
        j = os.system('cls')
        dut.getGrades_now()
        print "\n"
        xxx = raw_input("只有回车才能返回!")
    elif ch == '4':
        j = os.system('cls')
        dut.getInformation()
        print "已生成url.txt文件"
        print "\n"
        xxx = raw_input("只有回车才能返回!")
    elif ch == '0':
        break
    else:
        j = os.system('cls')
        print "输入错误,请重新输入!"
        xxx = raw_input("只有回车才能返回!")
