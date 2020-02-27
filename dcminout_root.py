import numpy as np
import os
import glob





def inout_root(var):
    cwd = os.path.dirname(os.path.abspath(__file__))
   
    path=cwd+"/"+var+'.txt'
    f = open(path,'r')
    message = f.readline()
  
    txp=message.split("#") 
    dcm_dir=txp
    input_dir=dcm_dir[1]
    output_dir=dcm_dir[3]
    dcm_height=dcm_dir[5]
    dcm_width=dcm_dir[7]
    dcmaxis_dir=dcm_dir[9]
    dcmdecimal_val=dcm_dir[11]
    actaul_center=dcm_dir[13]
    end_value=dcm_dir[15]
    out_videoname=dcm_dir[17]
    fframe=dcm_dir[21]
  
   


    data_path = os.path.join(str(input_dir), '*tif')

    files = glob.glob(data_path)
    
    files =  glob.glob(data_path)
    file_count = len(files)
 
   
    return [input_dir,output_dir,dcm_height,dcm_width,file_count,dcmaxis_dir,dcmdecimal_val,actaul_center,end_value,out_videoname,fframe]


