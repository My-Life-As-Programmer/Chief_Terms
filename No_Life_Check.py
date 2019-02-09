import pandas as pd
import numpy as np

'''
eagle = pd.read_csv("MSHP_AHWA.CSV",encoding = "ISO-8859-1")
geac3 = pd.read_csv("MSHP_FINGEA3.CSV",encoding = "ISO-8859-1")
geac4 = pd.read_csv("MSHP_FINGEA4.CSV",encoding = "ISO-8859-1")

egl = np.array(eagle)
g3 = np.array(geac3)
g4 = np.array(geac4)
'''

chklst = pd.read_csv("checklist.CSV",encoding = "ISO-8859-1")
chlst = np.array(chklst)
names = []
g3names = []
g4names = []
c = 0


def check_eagle(name):
    if name in g3names:
        print "Eagle --",name
        c +=1
    else:
        #print("none --",name)
        pass

def check_g3(name):
    if name in g3names:
        print "GEAC3 --",name
        c +=1
    else:
        #print("none --",name)
        pass
    

def check_g4(name):
    if name in g4names:
        print "GEAC4 --",name
        c +=1
    else:
        #print("none --",name)
        pass



def start_check2(egl=[],g3=[],g4=[]):
    chklst = pd.read_csv("checklist.CSV",encoding = "ISO-8859-1")
    chlst = np.array(chklst)
    names = []
    g3names = []
    g4names = []
    c = 0
    
    if not egl == []:
        eagle = pd.read_csv("MSHP_AHWA.CSV",encoding = "ISO-8859-1")
        egl = np.array(eagle)
        
    if not g3 == []:
        geac3 = pd.read_csv("MSHP_FINGEA3.CSV",encoding = "ISO-8859-1")
        g3 = np.array(geac3)
        
    if not g4 == []:
        geac4 = pd.read_csv("MSHP_FINGEA4.CSV",encoding = "ISO-8859-1")
        g4 = np.array(geac4)
        

    for i in range(len(egl)):
        if str(egl[i][7]) == "nan" or str(egl[i][7]) == "XXXXXXX": #or str(egl[i][7])== "nan":
            if egl[i][3] == 'X':
                #print(str(len(egl[i][5].split(' '))),'---',egl[i][5].split(' '))
                nm = egl[i][5].split(' ')
                #print(nm[0],nm[1])
                if len(nm)>=2:
                    names.append(nm[0].lower()+' '+nm[1].lower())
                else:
                    names.append(nm[0].lower())
    #print(names)

    for i in range(len(g3)):
        if str(g3[i][4]) == "nan" or str(g3[i][4]) == "XXXXXXX": 
            if g3[i][2] == 'X':
                #print(str(len(egl[i][5].split(' '))),'---',egl[i][5].split(' '))
                nm = g3[i][1]
                g3names.append(str(nm))

    for i in range(len(g4)):
        if str(g4[i][4]) == "nan" or str(g4[i][4]) == "XXXXXXX": 
            if g4[i][2] == 'X':
                #print(str(len(egl[i][5].split(' '))),'---',egl[i][5].split(' '))
                nm = g4[i][1]
                g4names.append(str(nm))

    print "\nMainframe   ---   Name \n"
    for i in range(len(chlst)):
        nm = u', '.join((chlst[i][0],chlst[i][1])).encode('utf-8').strip()
        chk_name = nm#(str(chlst[i][0]).strip().lower()+', '+str(chlst[i][1]).strip().lower())
        check_eagle(chk_name)
        check_g3(chk_name)
        check_g4(chk_name)

    if not c:
        print("Acoounts not found in the No-Life# Records\n")

    #print("Press Enter to stop the script")
    #input()

if __name__ == '__main__':
    start_check2()















