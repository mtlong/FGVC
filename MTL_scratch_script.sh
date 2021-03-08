cd tool

CUDA_VISIBLE_DEVICES=1 python video_completion.py \
       --mode object_removal \
       --path ../data/tennis \
       --path_mask ../data/tennis_mask \
       --outroot ../result/tennis_removal \
