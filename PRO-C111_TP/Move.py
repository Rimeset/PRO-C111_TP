import os 
import shutil

from_dir="E:/My_stuff/Documents/My_folder/Coding/Projects_and_others"
to_dir="E:/My_stuff/Documents/My_folder/Coding/Python/Projects/PRO-C111_TP"

list_name=os.listdir(from_dir)


for file_name in list_name:
    name,extension=os.path.splitext(file_name)
    
    if extension=='':
        continue
    if extension in ['.docx','.pdf','.xlsx','.png','.bmp']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+'Doc_Files'
        path3=to_dir+'/'+'Doc_Files'+'/'+file_name
        
        if os.path.exists(path2):
            print('Moving '+file_name+'...')
            shutil.move(path1,path3)
        else:
            os.mkdir(path2)
            shutil.move(path1,path3)