# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:05:14 2021

@author: flori
"""

# Conversion de chiffre alpha numérique en chiffres romains


def NbreRomain(n):
    
    for i in range (1, n+1):
        
        if i < 4:
        
             nbre =i*'I'
             
             print(nbre)
             
        elif i == 4:
            
            nbre ='IV'
             
            print(nbre)
            
                   
        elif i == 5:
            
            nbre ='V'
             
            print(nbre)
            
            
        elif i > 5 and i < 9:
            
            nbre ='V' + (i-5)*'I'
             
            print(nbre)
            
            
            
        elif i == 9:
            
            nbre ='IX' 
             
            print(nbre)
            
            
        elif i == 10:
            
            nbre ='X' 
             
            print(nbre)
            
            
        
                    
            
if __name__ == '__main__':
    NbreRomain(8)
            
    
 






