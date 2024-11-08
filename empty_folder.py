import os
def empty_folder(path: str):
    for i in os.listdir(path):
        os.remove(fr"{path}/{i}")