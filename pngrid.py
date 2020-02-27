


def gridpng(input_dir):
    import numpy as np
    import os
    import glob
    import cv2
    from pprint import pprint
    import sys,os
    from datetime import datetime
    import dcminout_root
    import datetime

    strt_time = datetime.datetime.now()




    os.mkdir("data")

    def color_gray(input_dir):

        data_path = os.path.join(input_dir, '*tif')
        files = glob.glob(data_path)
        RGB=[]
        files =  glob.glob(data_path)
        cwd = os.getcwd()
        png_dir = os.path.join(cwd,'data')
        d=0
        for f1 in sorted(files):
        ###################
            import matplotlib.pyplot as plt     
            import matplotlib.axis as maxis
            
            
        
    

            
            img = plt.imread(f1)
            fig = plt.figure(figsize=(40.00,20.00))
            # fig = plt.figure()

            X = [1, 2, 3, 4, 5, 6, 7]
            Y = [1, 3, 4, 2, 5, 8, 6]

            # axes1 = fig.add_axes([0.1, 0.1, 0.9, 0.9]) # main axes
            axes1 = fig.add_axes([0.1, 0.1, 0.9, 0.9]) # main axes
            plt.imshow(~img)
            # axes2 = fig.add_axes([0.2, 0.2, 0.2, 0.3]) # inset axes
            # axes2 = fig.add_axes([0.16, 0.21, 0.78, 0.7]) # inset axes
            # axes2 = fig.add_axes([0.16, 0.25, 0.78, 0.4]) # inset axes  etron=0262
            #################################left###top2bottom
            # axes2 = fig.add_axes([0.21, 0.33, 0.78, 0.4])  # etron 2052
            # axes2 = fig.add_axes([0.10, 0.34, 0.98, 0.5])  # etron 2052
            axes2 = fig.add_axes([0.10, 0.3299, 0.898, 0.54])  # etron 2052 axes2 = fig.add_axes([0.10, 0.33, 0.897, 0.52])  # etron 2052



       
            axes1.imshow(~img)

          


            xl=np.arange(0,1,1)


           
            axes1.set_yticklabels([])
            axes1.set_xticklabels([])
           
            axes2.patch.set_alpha(2005)
            xl=np.arange(0,2052,100)

            yl=range(0,1703,100)    
            yl=sorted(yl,reverse=True)
            plt.grid(color='c',which='major',linestyle=':',linewidth=0.8)
            plt.ylim(0,1500)        
            plt.xticks(xl)
            plt.xlim(0,2052)
            plt.ylim(0,1703)
            plt.yticks(yl) 


            axes2.set_xlabel('y')
            axes2.set_ylabel('x')
            
            image_out = os.path.join(png_dir, "%d.png"%d)
            plt.savefig(image_out)
            plt.close()
            






            d=d+1
        



    
    

    
    

        
    




    

    ## Main Function 

    color_gray(input_dir)

  


























