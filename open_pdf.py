# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 22:21:52 2025

@author: Carlos Gil
"""

import os
import glob
import subprocess

folder_path = r"C:\Users\Carlos Gil\Desktop\Unrequited"
print('La carpeta de acceso es', {folder_path})    

def abrir_pdf(folder_path):
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    
    if not pdf_files:
        print('No hay archivos pdf en', {folder_path})
    
    for pdf_file in pdf_files:
        if os.name == 'nt':
            os.startfile(pdf_file)

abrir_pdf(folder_path)        