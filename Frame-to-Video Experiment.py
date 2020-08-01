#!/usr/bin/env python
# coding: utf-8

# In[34]:


import cv2
import os

from os.path import isfile, join


# In[37]:


def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    
    #for sorting the file names properly
    print(len(files))
    for i in range(len(files)-1):
        filename = pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height,  width,  layers = img.shape
        size = (width, height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
        
    out =  cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'),  fps,  size)
    
    for i in range(len(frame_array)):
        #writing to a image  array
        out.write(frame_array[i])
    out.release()


# In[38]:


pathIn= 'E:\Data Set VOT\Basketball\Images'
pathOut = 'basketball.avi'
fps = 25.0
convert_frames_to_video(pathIn, pathOut, fps)


# In[1]:


## MANASH PRATIM KAKATI
## PG CERTIFICATION IN AI & ML
## E&ICT ACADAMY, IIT GUWAHATI


# In[ ]:




