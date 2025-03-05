import os
import shutil

src=r'C:\Users\Administrator\Downloads'
word_dest=r'C:\Users\Administrator\Downloads\/Wordfiles'
excel_dest=r'C:\Users\Administrator\Downloads\Excelfiles'
pdf_dest=r'C:\Users\Administrator\Downloads\PDFfiles'
imgdest=r"C:\Users\Administrator\Downloads\Imgfile"

word_files=[]
excel_files=[]
pdf_files=[]
imagefiles=[]

def make_name(name,destlist):
    n,e=os.path.splitext(name)
    for filename in destlist:
        dn,de=os.path.splitext(filename)
        if not n[-1].isnumeric():
            if n==dn:
                n=n+'1'
        if n[-1].isnumeric():
            while True:
                if n in dn:
                    n=n[:-1]+'2'
                else:
                    break
    return n+e

for file in os.listdir(src):
    if file.endswith('.doc') or file.endswith('.docx'):
        word_files.append(file)
    if file.endswith('.xlsx'):
        excel_files.append(file)
    if file.endswith('.pdf'):
        pdf_files.append(file)
    if file.endswith('.jpg') or file.endswith('.webp'):
        imagefiles.append(file)

for files in word_files:
    if not os.path.exists(word_dest):
        os.makedirs(word_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(word_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(word_dest))), word_dest)
    print("files transfered ,type: word")

for files in excel_files:
    if not os.path.exists(excel_dest):
        os.makedirs(excel_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(excel_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(excel_dest))), excel_dest)
    print("files transfered ,type: excel")

for files in pdf_files:
    if not os.path.exists(pdf_dest):
        os.makedirs(pdf_dest)
    os.rename(os.path.join(src,files), os.path.join(src, make_name(files, os.listdir(pdf_dest))))
    shutil.move(os.path.join(src, make_name(files, os.listdir(pdf_dest))), pdf_dest)
    print("files transfered ,type: pdf")

for file in imgdest:
    if not os.path.exists(imgdest):
        os.makedirs(imgdest)
    os.rename(os.path.join(src, file), os.path.join(src, make_name(file, os.listdir(imgdest))))
    shutil.move(os.path.join(src, make_name(file, os.listdir(imgdest))), imgdest)
    print("files transfered ,type: image")


