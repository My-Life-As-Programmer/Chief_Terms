import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import requests
import json
import re
import itertools
import getpass
import base64
#import Check_Mainframe

'''
cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("https://chief.mssm.edu/employee_records")
'''
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
base_url = "https://chief.mssm.edu"#/employee_records"
username =''
password = ''
list_ln = ''



# function to read the webpage

def read_page(url):
    #br.open(url)
    d ={'MsnyuhealthAccount' : '', 'MssmcampusAccount' : ''}
    #print"----------------in read page---------------"
    #print url
    #print"----------------- Start Here ---------------"
    br.open(url)
    soup = BeautifulSoup(br.response(),"lxml")
    divs = soup.find_all("div",class_=["span-9"]) #- works  -- gives 3 divs , span-9 with account details , span-9 with options, span-9-last with log
    
    # for network accounts
    div = str(divs[0])#.encode("ISO-8859-1")
    div = '<html><head> </head> <body>'+div+'</body></html>'
    sp = BeautifulSoup(div,"lxml")
    tok = sp.text.split()
    reg = ['Accounts','Mainframe','mainframe','accounts','No','found.']
    tok1 = [x for x in tok if x not in reg]
    temptok = ' '.join(tok1)
    #print temptok    
    pattern = re.compile('..\w{3,6}\d{1,2}.\w{3,6}\d{1,2}.{1,15}')
    tok2 = [x for x in tok1 if not pattern.match(x)]
    #t = pattern.sub(' ',temptok)
    #print tok2
    #d = dict(itertools.izip_longest(*[iter(tok2)] * 2, fillvalue=""))
    for i in range(0,len(tok2),2):
        if tok2[i] == 'MsnyuhealthAccount':
            if not d['MsnyuhealthAccount']:
                d['MsnyuhealthAccount'] += tok2[i+1]
            else:
                d['MsnyuhealthAccount'] += '\t'+tok2[i+1]
                
        if tok2[i] == 'MssmcampusAccount':
            if not d['MssmcampusAccount']:
                d['MssmcampusAccount'] += tok2[i+1]
            else:
                d['MssmcampusAccount'] += '\t'+tok2[i+1]        
    #print d
    
    #for key in d:
    #    print key,' - ',d[key]
    if not d['MsnyuhealthAccount']:
        d['MsnyuhealthAccount'] = 'NA'
    if not d['MssmcampusAccount']:
        d['MssmcampusAccount'] = 'NA'
    
    #print d
    
    #''' --testing
    # works for Dept name
    div = str(divs[1])
    div = '<html><head> </head> <body>'+div+'</body></html>'
    sp = BeautifulSoup(div,"lxml")
    div = sp.find("div",class_=["ticket"])
    div = '<html><head> </head> <body>'+str(div)+'</body></html>'
    sp = BeautifulSoup(div,"lxml")
    dept = sp.text.strip()
    if dept:
        dept = dept.split()[0]
        #print dept.split()[0]
    else:
        dept ='NA'
        #print 'nope'

    # for account details
    div = soup.find_all("div",{'id':'account_search'})#,class_=["span-27 last"])
    div = '<html><head> </head> <body>'+str(div)+'</body></html>'
    sp = BeautifulSoup(div,"lxml")
    div = sp.find_all("span",class_=["instruction"])
    div = '<html><head> </head> <body>'+str(div)+'</body></html>'
    sp = BeautifulSoup(div,"lxml")
    details = sp.text.strip().split(', ')
    #print details,len(details)
    ln = details[len(details)-1].strip(']')
    name = details[0]
    ind =[i for i, c in enumerate(name) if c.isupper()]
    lastname = name[ind[1]:]
    firstname = name[ind[0]:ind[1]].strip()
    #print lastname,firstname,ln,dept,d['MsnyuhealthAccount'],d['MssmcampusAccount']
    row = lastname+','+firstname+','+ln+','+dept+','+d['MsnyuhealthAccount']+','+d['MssmcampusAccount']
    with open('checklist.csv','a') as f:
        f.write(row+'\n')
    print row
    #testing'''

def start_chief_term():
    
    #br.open("https://chief.mssm.edu")#/employee_records")
    #base_url = "https://chief.mssm.edu"#/employee_records"
    
    try :
        br.open("https://chief.mssm.edu/employee_records")

        br.select_form(nr=0)
        br.form['login'] = username
        br.form['password'] = password
        br.submit()
        
        br.open("https://chief.mssm.edu/employee_records")
    
    except:
        print 'Please check the connection and try again'

    soup = BeautifulSoup(br.response(),"lxml")
    mydivs = soup.find_all("div", class_=["span-9"])

    wdivs = []

    #print(len(mydivs))
    for div in mydivs:
        if div.attrs["class"] == ["span-9"]:
            wdivs.append(div)
            #print (div.attrs)

    #print len(wdivs)
    a_tags =wdivs[0].find_all('a', class_='linky', href=True)
    a_tags +=wdivs[1].find_all('a', class_='linky', href=True)
    print 'Number of Terminations : ',len(a_tags)
    print '\n'

    for i in range(len(a_tags)):
        read_page(base_url+a_tags[i]['href'])


# for custon number of termminnations

def start_cust_term():

    list_str = raw_input('Please enter Life Numbers seperated by a comma ( , ) :\n')
    list_ln = list_str.strip().split(',')
    try :
        br.open("https://chief.mssm.edu/employee_records")
        br.select_form(nr=0)
        br.form['login'] = username
        br.form['password'] = password
        br.submit()

        br.select_form(nr=0)
    except:
        print 'Please check the connection and try again'
    
    
    for rec in list_ln:
        br.form['search'] = rec  
        br.submit()
        try:
            read_page(br.geturl())
        except:
            print '\nWrong Life# -- ',rec,'\n'
        br.back()
        br.select_form(nr=0)
        
        
# Main script sraerts here

if __name__ == '__main__':
    
    try:
        with open('password.txt','r') as f:
            ls = f.read().split('\n')
            username = ls[0]
            password = base64.b64decode(ls[1])
    except:
        username = raw_input('enter username for chief : ')
        password =  getpass.getpass('enter password for chief : ')   
        with open('password.txt','w') as f:
            f.write(username+'\n'+base64.b64encode(password))
    br.open("https://chief.mssm.edu")#/employee_records")

    br.select_form(nr=0)
    br.form['login'] = username
    br.form['password'] = password

    inp = raw_input('please enter 0 for Chief Terminations or 1 for Custom Terminations : ')

    with open('checklist.csv','w') as f:
        f.write('last_name,first_name,life_num,dept,AD,MSSM\n')

    
    if inp == '0':
        start_chief_term()
    elif inp == '1':
        start_cust_term()
    else :
        print 'Invalid input, please try again...'
    
    raw_input('\nPress Enter to Search for Mainframe Accounts')#Stop the Script\n')
    #Check_Mainframe.start_check1()
    
    
