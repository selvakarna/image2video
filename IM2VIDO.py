import numpy as np
from cv2 import VideoWriter, VideoWriter_fourcc
import os
import glob
import cv2
from pprint import pprint
import sys,os
from datetime import datetime

import datetime

strt_time = datetime.datetime.now()


FPS =10
seconds =10


cwd = os.getcwd()
input_dir = os.path.join(cwd,'fstfrm')

def color_gray(input_dir):
    


    data_path = os.path.join(input_dir,'*jpg')
    files = glob.glob(data_path)

    RGB=[]

    for f1 in sorted(files):
            RGB = cv2.imread(f1)
            h=np.shape(RGB)
         
    output_dir=input_dir
    videoheight=h[0]

    videowidth=h[1]
 
   
    out_videoname='se'
    video_outputname=output_dir+"/"+out_videoname+'.mp4'
    video_out = os.path.join(output_dir, video_outputname)
################################################################################################  
    files =  glob.glob(data_path)
    file_count = len(files)
    out = cv2.VideoWriter(video_out,cv2.VideoWriter_fourcc(*'DIVX'), float(FPS), (videowidth,videoheight))
    for f1 in sorted(files):

        RGB = cv2.imread(f1)
        n=25
        sum=0
        i=1
        while i<n:
          
            out.write(RGB)

            i=i+1
    out.release()

## Main Function 

color_gray(input_dir)
end_time = datetime.datetime.now()




























