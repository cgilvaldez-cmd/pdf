# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 21:12:32 2025

@author: Carlos Gil
"""


d1='''
<!DOCTYPE html> <html> <head> <title>Page Title</title> </head> <body>
'''
  
d2='''
</body> </html>
'''

li= ['https://www.cleancode.com']

filo = open('pdf_web', 'w')

filo.write(d1)

for ss in li:
    v1= '<p> <a href=https:// + sswww.cleancode.com/'+ ss +'<embed src= "NIHMS256807-supplement-Supp.pdf" type= "application/pdf" width="100%" height="600px"</a>, <p>/>'
    filo.write(v1)

filo.write(d2)
filo.close()
