
"""
Rename files in a directory in a structured way
Arguments:
input_folder - the folder that houses the files you want to copy
output_folder - a user specified folder that exists which is the destination of copied files
label - a description that creates a new name along with a count

"""


import os
import pandas as pd
import shutil


def read_files(fld):
    for root, dirs, files in os.walk(fld):
        return files

def files_and_extensions(paths):

    extensions = []
    files = []
    for fl in paths:
        extensions.append(os.path.splitext(fl)[1])
        files.append(os.path.splitext(fl)[0])
    return files, extensions

def main():
    input_folder = 'combined'
    output_folder = 'output_files' # directory created if does not exist - if exists process is stopped
    label = 'test_image' #new file name description

    directory = os.getcwd()
    file_location = os.path.join(directory,input_folder)
    files = read_files(file_location)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    else:
        raise ValueError("the output folder",output_folder,"already exists. Create a fresh folder or change output folder name")
    if not files:
        raise ValueError("The folder you specified",input_folder," is empty")

    filenames, extensions = files_and_extensions(files)

    new_files = []
    count = 0
    for name, ext, fullname in  zip(filenames, extensions,files):
        count +=1
        new_name = label + str(count) + ext
        new_files.append(new_name)
        new_path = os.path.join(directory,output_folder,new_name)
        old_path = os.path.join(directory,input_folder, fullname)
        shutil.copy(old_path,new_path)
        print("copying file from {} to {} ".format(old_path,new_path))

    reference = pd.DataFrame(zip(files,new_files),columns=('old_path','new_path'))
    reference.to_csv('output_reference.csv')
    print("done")




