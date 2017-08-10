import os
import shutil
from shutil import copyfile

def rename_files():
    file_list = os.listdir(os.getcwd()+"/message_scrambled")
    #os.chdir(("/Users/rjuelich/PycharmProjects/message3"))
    for file in file_list:
        copyfile(os.getcwd()+"/message_scrambled/"+file, os.getcwd()+"/message_out/"+file.strip('0123456789'))

rename_files()
