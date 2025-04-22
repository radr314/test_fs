import os
import time
list_imgs=os.listdir('./images/')

directory='images'
unnamed_files=[]
for i in list_imgs:
    if not i.startswith('image_'):
        unnamed_files.append(i)
unnamed_files.sort(key=lambda f: os.path.getctime(os.path.join(directory,f)))

def get_max_image_name(list_images:list):
    m=0
    for i in list_images:
        if i.startswith('image_'):
            try:
                val=int(i.split('image_')[1].split('.')[0])
                if val>m:
                    m=val
            except IndexError as err:
                print(i)
                raise err
    return m

val=get_max_image_name(list_imgs)

for i in unnamed_files:
    val+=1
    os.rename(f'images/{i}',f'images/image_{val}.png')
