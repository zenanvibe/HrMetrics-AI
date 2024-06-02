import os
from download_model import download
from zipfile import ZipFile

def unzip(filePath,toPath):
    with ZipFile(filePath, 'r') as zObject: 
        # Extracting all the members of the zip  
        # into a specific location. 
        zObject.extractall(path=toPath)

if not os.path.isdir('./models'):
    print("Models Not Found")
    print("Installing Models")
    os.mkdir('./models')
    download()
    print("Unzipping the model")
    unzip('./models/leave.zip','./models/')
    os.remove('./models/leave.zip')
    print("Models Downloaded successfully")