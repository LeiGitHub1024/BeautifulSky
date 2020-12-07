# 遍历cityscapes/gtFine/train 下面每个文件夹里的json
import os
import json
import numpy as np
from tqdm import tqdm

# g = os.walk("./cityscapes/gtFine/train") 
# okJson = []
# for path,dir_list,file_list in g:  
#   for dir_name in dir_list:
#     dir = os.path.join(path, dir_name)
#     d = os.walk(dir) 
#     for path1,_,file_list1 in d:
#       for file_name1 in tqdm(file_list1):
#         file_path1 = os.path.join(path1, file_name1)
#         postfix = os.path.splitext(file_name1)[-1]
#         if postfix == ".json":
#           with open(file_path1,'r') as load_f:
#             load_dict = json.load(load_f)
#             for i in load_dict['objects']:
#               if(i['label']=="sky"):
#                 okJson.append(file_path1)
#                 break 

# np.save("filename.npy",okJson)






b = np.load("filename.npy")
print(b)
array = []
for i in tqdm(b):
  base = i[0:-13]
  array.append(base + "color.png")
  array.append(base + "instanceIds.png")
  array.append(base + "instanceTrainIds.png")
  array.append(base + "labelIds.png")
  array.append(base + "labelTrainIds.png")
  array.append(i)
np.save("array.npy",array)


import shutil
c = np.load("array.npy")
for i in tqdm(c):
  if os.path.exists(i):
    shutil.move( i, "./target/")       







