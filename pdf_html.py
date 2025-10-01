# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:47:11 2025

@author: Carlos Gil
"""
d1='''
<!DOCTYPE html>
<html>
 <head>
 <title>Page Title</title>
 </head>
 <body>
 '''
x=1

    
d2=''' 
</body>
</html>''' 


li = ['https://www.unam.mx']

for ss in li: '<p <a href="https://www.unam.mx">' + 'file-' + '<\a> <\p>'
k= x+1


filo = open('pdf_html','w')

filo.write(d1) 

    

filo.write(d2)
filo.close()