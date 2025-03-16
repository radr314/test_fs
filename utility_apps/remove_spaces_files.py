import os
# from pathlib import Path
from copy import deepcopy
import logging

logging.basicConfig(filename="logs/file_modification.log",level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
def modify_file_name(file):
    current_name=deepcopy(file)
    if " " in file.split("/")[-1]:
        new_file_name=file.split('/')[-1].replace(' ','_')
        new_name=file.replace(file.split("/")[-1],new_file_name)
        os.rename(current_name,new_name)


def recr_fill(contents,i,prefix=""):
    if len(contents)==i+1:
        return
    if os.path.isdir(contents[i]):
        contents.extend([prefix+contents[i]+"/"+k for k in os.listdir(contents[i])])
        contents.pop(i)
        recr_fill(contents,i,prefix)
    else:
        recr_fill(contents,i+1,prefix)
    return contents

if __name__=="__main__":
    try:
        contents=os.listdir()
        logging.info(f"targeted directory : {contents}")
        contents=recr_fill(contents,0)
        logging.info(f"targeted directory : {contents}")
        outs=map(modify_file_name,contents)
        logging.info(f"targeted directory : {outs}")

    except Exception as err:
        logging.exception(f"Exception {err}")



