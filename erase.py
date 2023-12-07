import os, shutil

# Removes old Stock Folder and recreates it to remove old stocks
def erase(folder):
    try:
        shutil.rmtree(folder)
    except:
        print("No old stock folder found")
    os.mkdir(folder)