# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 08:34:11 2021

@author: CHERIF
"""
banque=["BCT","ATB","BS","BIAT","BNA","BT","STB","AB"]
#banque = {"00":"BCT","01":"ATB","02":"BS","03":"BIAT","04":"BNA","05":"BT","06":"STB","07":"AB"}
   # list (range(1,7))
list=[0,1,2,3,4,5,6,7]

def testRIB(rib):
   
    if len(rib)!=20:
        result=1
    else:
        bq=int(rib[0:2])
        if bq in list:
            cle=int(rib[-2:])
            nbr=int(rib[0:-8])
            mod=nbr%97
            nbr1=int(rib[12:-2])
            #nbr2=int(str(mod)+rib[12:-2])*100
            nbr2=int("%s%s" % (mod,nbr1))*100
            mod1=nbr2%97
            cle1=97-mod1
            #print(bq,nbr,mod,nbr2,mod1,cle,cle1)
            if cle1==cle:
                result=0
            else:
                result=1
           
        else:
            result=1
        
    
    return result 


print('Contrôle RIB')
for x in range (1,5):
    a=input('saisir le RIB numéro ' + str(x) + ': ')
    # a= "05903000050640690041"
    # b="01700022110354508756"
    if testRIB(a) == 0:
        bq=int(a[0:2])
        libbq=banque[bq]
        print("RIB Numéro ",x," : ",a,' valide')
        display = "RIB {} : {} valide"
        print(display.format(x,a))
        #print("RIB Numéro ",x," : ",a,' valide', end=",")
        #print("RIB Numéro ",x," : ",a,' valide', sep=",")
        print("banque: ",libbq)
    else:
        print("RIB Numéro ",x," : ",a,' invalide')

