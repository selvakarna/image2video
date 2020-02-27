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


def stag_1(input_dir,output_dir,dcmaxis_dir,dcmdecimal_val,actl_center):

    FPS =10
    seconds =10


 

    def color_gray(input_dir,output_dir,dcmaxis_dir,dcmdecimal_val,actl_center):

    
        XV=dcmaxis_dir
        XV=str(XV)
        XV=XV[2]
    
    
    
    

       
        out_videoname='output'
        video_outputname=output_dir+"/"+out_videoname+'.mp4'
        video_out = os.path.join(output_dir, video_outputname)
    ################################################################################################
        
        data_path = os.path.join(input_dir, '*png')
        files = glob.glob(data_path)
        
        RGB=[]
        img=[]
        dr=dcmaxis_dir
    
        
        files =  glob.glob(data_path)
        file_count = len(files)

    
        
        if XV=='x':
            framx='x-axis='
            framy='y-axis=NA'
            framz='z-axis=NA'
            Unit='unit=mm'
        elif XV=='y':
                framx='x-axis=NA'
                framy='y-axis='
                framz='z-axis=NA'
                Unit='unit=mm'
        else:
            framx='x-axis=NA'
                    
            framy='y-axis=NA'
            framz='z-axis='
            Unit='unit=mm'
            
        img_array = []

        for mf1 in files:
            im = cv2.imread(mf1)

        
        
            height, width, layers = im.shape
            size = (width,height)
            videowidth=width
            videoheight=height
        
    
    
        
        out = cv2.VideoWriter(video_out,cv2.VideoWriter_fourcc(*'DIVX'), float(FPS), (videowidth,videoheight))

        mn=float(dcmdecimal_val)
    
        ########### SHORT CUT FOR 0.6 CODE

        tot=file_count-1


     
        ## By Changes '0' Center variation 0.6 from left and right  May 21
        LN=actl_center
        ### Changes now agst 1 int(LN) from LN also actl_center
        LNend=int(LN)*mn
        actl_center=int(actl_center)
        RP=file_count-actl_center
        RPend=RP*mn
        lxr=[]
        LNend=round(LNend,1)
    
        for l in np.arange(-LNend,0,mn):
            # rx=round(r,1)
            lx=round(l,2)
            lxr.append(lx)
    
    

        RPend=round(RPend,1)
        for r in np.arange(0,RPend,mn):
            rx=round(r,1)
            lxr.append(rx)


        
    
        for f1,xx in zip(sorted(files),lxr):

    
            
            
            xr=round(xx,1)
            xr=np.array(xr)
         

        
   
            img = cv2.imread(f1)
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            gray=gray
            RGB=cv2.merge((gray,gray,gray))
            height, width, layers = img.shape
            size = (width,height)
    


 
            
        
        
        
            
        
            
            
            
        
           

            if XV=='x':
                cv2.putText(RGB, framx+str(xr), (width-650, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
                cv2.putText(RGB, framy, (width-650, 103), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255),3)
                cv2.putText(RGB, framz, (width-650, 158), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
                cv2.putText(RGB, Unit, (width-650, 220), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)

               
     
            elif XV=='y':
                cv2.putText(RGB, framx, (width-650, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
                cv2.putText(RGB, framy+str(xr), (width-650, 103), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255),3)
                cv2.putText(RGB, framz, (width-650, 158), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
                cv2.putText(RGB, Unit, (width-650, 220), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
            else:
                
                cv2.putText(RGB, framx, (width-650, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
                cv2.putText(RGB, framy, (width-650, 103), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255),3)
                cv2.putText(RGB, framz+str(xr), (width-650, 158), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)
                cv2.putText(RGB, Unit, (width-650, 220), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3)

            
            




            out.write(RGB)
            del gray ,xx,f1
       

        del RGB ,img,framx,width,size,data_path,files,file_count ##indir,oudir,data,
        out.release()
        
            
    color_gray(input_dir,output_dir,dcmaxis_dir,dcmdecimal_val,actl_center)  

    
    

        
    

        



