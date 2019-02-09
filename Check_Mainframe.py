import pandas as pd
import numpy as np
import No_Life_Check

alluser = pd.read_csv("MSHP_ALLU.CSV",encoding = "ISO-8859-1")
geac3 = pd.read_csv("MSHP_FINGEA3.CSV",encoding = "ISO-8859-1")
geac4 = pd.read_csv("MSHP_FINGEA4.CSV",encoding = "ISO-8859-1")
eagle = pd.read_csv("MSHP_AHWA.CSV",encoding = "ISO-8859-1")
chklst = pd.read_csv("checklist.CSV",encoding = "ISO-8859-1")

ausr = np.array(alluser)
g3 = np.array(geac3)
g4 = np.array(geac4)
egl = np.array(eagle)


def check(uid,name,emp):
    aug3,aug4,aueg,g3x,g4x,egx,racfid = 0,0,0,0,0,0,'none'
    if emp:
        #print("employee")
        for i in range(len(ausr)):
            if ausr[i][20] == uid or str(ausr[i][15]).lower() == name:
                
                if ausr[i][3] == 'X':
                    aueg = 1 #print('Eagle----')
                    racfid = ausr[i][0]
                    
                if ausr[i][5] == 'X':
                    aug3 = 1 #print('Geac 3----')
                    if not racfid:
                        racfid = ausr[i][0]
                        
                if ausr[i][6] == 'X':
                    aug4 = 1 #print('Geac 4----')
                    if not racfid:
                        racfid = ausr[i][0]
                        
                #print(ausr[i][15],'---->',arr[i][20])
                break;
            
        for i in range(len(g3)):
            if g3[i][4] == uid or str(g3[i][1]).lower() == name:
                if g3[i][2] == 'X':
                    g3x = 1
                    #print('Geac3----')
                    racfid = g3[i][0]
                break;


        for i in range(len(g4)):
            if g4[i][4] == uid or str(g4[i][1]).lower() == name:
                if g4[i][2] == 'X':
                    g4x = 1
                    #print("g4")
                    #print('Geac4----')
                    racfid = g4[i][0]
                break;

        for i in range(len(egl)):
            if egl[i][7] == uid :
                if egl[i][3] == 'X':
                    egx = 1
                    #print('Eagle----')
                    racfid = egl[i][0]
                if egl[i][2] == 'X':
                    #egx = 1
                    #print(' AHW----')#,end="")
                    pass
                break;
            
        if not egx:
            for i in range(len(egl)):
                if str(egl[i][5]) != "nan" and not egl[i][7]:
                    nm = egl[i][5].split(' ')
                    if len(nm)>=2:
                        chk_nm = nm[0].lower()+' '+nm[1].lower()
                    else:
                        chk_nm = nm[0].lower()
                            
                    if egl[i][7] == uid or chk_nm == name:
                        if egl[i][3] == 'X':
                            egx = 1
                            #print('Eagle----')
                            racfid = egl[i][0]
                        if egl[i][2] == 'X':
                            #egx = 1
                            #print(' AHW----')#,end="")
                            pass
                        break;     
    else:
        #print("consultant")
        for i in range(len(ausr)):
            if str(ausr[i][15]).lower() == name:
                
                if ausr[i][3] == 'X':
                    aueg = 1 #print('Eagle----')
                    racfid = ausr[i][0]
                    
                if ausr[i][5] == 'X':
                    aug3 = 1 #print('Geac 3----')
                    if not racfid:
                        racfid = ausr[i][0]
                        
                if ausr[i][6] == 'X':
                    aug4 = 1 #print('Geac 4----')
                    if not racfid:
                        racfid = ausr[i][0]
                        
                #print(ausr[i][15],'---->',arr[i][20])
                break;
            
        for i in range(len(g3)):
            if str(g3[i][1]).lower() == name or g3[i][4] == uid:
                if g3[i][2] == 'X':
                    g3x = 1
                    #print('Geac3----')
                    racfid = g3[i][0]
                break;


        for i in range(len(g4)):
            if str(g4[i][1]).lower() == name or g4[i][4] == uid:
                if g4[i][2] == 'X':
                    g4x = 1
                    #print('Geac4----')
                    racfid = g4[i][0]
                break;
        for i in range(len(egl)):
            if str(egl[i][5]) != "nan" and not egl[i][7]:
                nm = egl[i][5].split(' ')
                if len(nm)>=2:
                    chk_nm = nm[0].lower()+' '+nm[1].lower()
                else:
                    chk_nm = nm[0].lower()
                            
                if egl[i][7] == uid or chk_nm == name:
                    if egl[i][3] == 'X':
                        egx = 1
                        #print('Eagle----')
                        racfid = egl[i][0]
                    if egl[i][2] == 'X':
                        #egx = 1
                        #print(' AHW----',end="")
                        pass
                    break;

    # printing if the user has eagle , geac3,geac4
    if aueg or egx:
        print(' Eagle---')#,end="")
    if  aug3 or  g3x:
        print(' Geac3---')#,end="")
    if  aug4 or  g4x:
        print(' Geac4---')#,end="")
    print racfid,'----',uid,'----',name+'\n'
# module ends


def start_check1():
    chlst = np.array(chklst)
   
    print("\nMainframe  ---  Life# --- Name \n")
    for i in range(len(chlst)):
        ln = str(chlst[i][2])
        nm = u', '.join(((chlst[i][0]).strip(),(chlst[i][1]).strip())).encode('utf-8').strip()
        if str(chlst[i][2])[0] == 'E':
            check(ln.lower(),nm.lower(),0)#check(str(chlst[i][2]),(str(chlst[i][0]).strip().lower()+', '+str(chlst[i][1]).strip().lower()),0)
        else:
            check(ln.lower(),nm.lower(),1)#check(str(chlst[i][2]),(str(chlst[i][0]).strip().lower()+', '+str(chlst[i][1]).strip().lower()),1)

    print('========== Checking for account in No-Life# list ==========')
    No_Life_Check.start_check2(egl,g3,g4)
    print("Press Enter to stop the script")
    raw_input()

if __name__ == '__main__':
    start_check1()
