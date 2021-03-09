
import sys
import os

DATASET_ROOT="/media/malong/7665cf70-1886-4554-b39d-f6a0e600d53e/workspace/Data_Storage/Datasets/DAVIS/480P/DAVIS-2017-Unsupervised-trainval-480p/DAVIS/"
RESULT_FOLDER = "/media/malong/7665cf70-1886-4554-b39d-f6a0e600d53e/workspace/2021/Video_Inpainting/Results/FGVC/DAVIS/"

vid_list = os.listdir(DATASET_ROOT + 'JPEGImages/480p/')

#os.system("cd tool")
for i in range(len(vid_list)):
    vid_name = vid_list[i]
    frame_folder_name = DATASET_ROOT + 'JPEGImages/480p/' + vid_name
    mask_folder_name = DATASET_ROOT +  'Annotations/480p/' + vid_name
    output_folder_name = RESULT_FOLDER + vid_name
    command_str = "cd tool \n CUDA_VISIBLE_DEVICES=1 python video_completion_MTL.py \
       --mode object_removal \
       --path " + frame_folder_name + " \
       --path_mask " + mask_folder_name + " \
       --outroot " + output_folder_name
    os.system(command_str)

