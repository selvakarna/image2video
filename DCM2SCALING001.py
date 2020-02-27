import PySimpleGUI as sg
import stg1
import time 

start=time.time()
def gui_mdl():

    layout = [[sg.Text('DCM2SCALING VIDEO TOOL')],
    [sg.Text('Input Image Root', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
    [sg.Text('Output Video Root ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
                 
    [sg.Text('Direction', size=(15, 1)),sg.Listbox(values=['x', 'y', 'z'], size=(15, 1))],

    [sg.Text('Frame Variation',size=(15, 1)),sg.InputText()],
    [sg.Text('Frame Centre',size=(15, 1)),sg.InputText()],
    [sg.Submit(), sg.Cancel()]]

    window = sg.Window('DICOM2SCALING VIDEO TOOL', layout)

    event, values = window.Read()
    
    input_dir=values[0]
    output_dir=values[1]
    dcmaxis_dir=values[2]
    dcmdecimal_val=values[3]
    actl_center=values[4]
    #####################################################
    ### STAGE 1  READ INPUT DICOM IMAGE'S WITH GRID OUT
    import pngrid
    import os
    import shutil
    cwd = os.getcwd()
    png_dir = os.path.join(cwd,'data')


    pngrid.gridpng(input_dir)
    
    stg1.stag_1(png_dir,output_dir,dcmaxis_dir,dcmdecimal_val,actl_center)

    ############################################
## ###########STAGE-2 [FIRST FRAMES IM2VIDEO]
    import IM2VIDO
    import numpy as np
    from cv2 import VideoWriter, VideoWriter_fourcc
  
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

    IM2VIDO.color_gray(input_dir)
    ##################################################
    ##STAGE ---3
    import moviepy.editor as mp

    
 
    
    cwd = os.getcwd()
    vidopath = os.path.join(cwd,'result','output.mp4')


    video = mp.VideoFileClip(vidopath)


    cwd = os.getcwd()
    input_dir = os.path.join(cwd,'nlog')

    data_path = os.path.join(input_dir, 'nlog.png')

    files=str(data_path)



    logo = (mp.ImageClip(files)

            .set_duration(video.duration)
            .resize(height=150) 
            .margin(right=1, top=100, opacity=0) 
            .set_pos(("center","bottom")))


    final = mp.CompositeVideoClip([video, logo])

    vidopath = os.path.join(input_dir,'logovideo.mp4')

    final.write_videofile(vidopath)
    ####################################################################################
    ####### STAGE--4


    from moviepy.editor import VideoFileClip, concatenate_videoclips
  
    cwd = os.getcwd()
    input_dir = os.path.join(cwd,'fstfrm')
    video_outputname=input_dir+"/"+'se.mp4'

    dirpath = os.getcwd()

    clip1 = VideoFileClip(video_outputname)

    input_dir = os.path.join(cwd,'nlog')
    second_outputname=input_dir+"/"+'logovideo.mp4'

    clip3 = VideoFileClip(second_outputname)
    final_clip = concatenate_videoclips([clip1,clip3])  
    input_dir = os.path.join(cwd,'final_video')
    final_video=input_dir+"/"+'result.mp4'
    final_clip.write_videofile(final_video)




    end_time = datetime.datetime.now()
    ########### REMOVE STAGE 1 GRID FOLDER
    
    shutil.rmtree('data')
    vidopath1 = os.path.join(cwd,'result','output.mp4')
    os.remove(vidopath1)
    vidopath2 = os.path.join(cwd,'fstfrm','se.mp4')
    os.remove(vidopath2)
    vidopath3 = os.path.join(cwd,'nlog','logovideo.mp4')
    os.remove(vidopath3)




# 

gui_mdl()
end=time.time()

dif=int(end-start)
tt=dif;
########################################################
import time
import datetime
from datetime import datetime

import socket
import pypyodbc


userName = os.environ.get('USERNAME')
print("Current UserName : " + userName)
Host = socket.gethostname()
print("HostName : " + Host)
ProjectName ="DCM-SCALING-VIDEO-TOOL"
Bulidate = " 13/05/2019"
Toolstarttime = datetime.now()

Toolendtime = datetime.now()
TimeSavings= "1"
AboutProject = " Dicom to Scaling "
Inputtext = " Dicom "
Team = " TCAE support "
Domainname = " TCAE support "
SubDomainname = " TCAE support "
connect =  pypyodbc.connect('Driver={SQL Server};Server=10.10.23.9;Database=LicenceManagement;uid=licenceusr;pwd=P@$$0R345R#@!')
cursor = connect.cursor()

SQLCommand =("Insert into EngineeringSoftwareTeamLog (ProjectName,BuildDate,UserName,SystemName,StartTime,EndTime,TimeSavedInMinutes,AboutProject,InputText,Team,Domain,SubDomain) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)")
Values=[ProjectName, Bulidate, userName, Host, Toolstarttime, Toolendtime, tt, AboutProject, Inputtext, Team,Domainname, SubDomainname]
cursor.execute(SQLCommand,Values) 
connect.commit()
connect.close()

