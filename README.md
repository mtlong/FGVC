# [ECCV 2020] Flow-edge Guided Video Completion

### [[Paper](https://arxiv.org/abs/2009.01835)] [[Project Website](http://chengao.vision/FGVC/)] [[Google Colab](https://colab.research.google.com/drive/1pb6FjWdwq_q445rG2NP0dubw7LKNUkqc?usp=sharing)]



**[ECCV 2020] Flow-edge Guided Video Completion**
<br/>
[Chen Gao](http://chengao.vision), [Ayush Saraf](#), [Jia-Bin Huang](https://filebox.ece.vt.edu/~jbhuang/), and [Johannes Kopf](https://johanneskopf.de/)
<br/>
In European Conference on Computer Vision (ECCV), 2020

## Prerequisites

- Linux (tested on CentOS Linux release 7.4.1708)
- Anaconda
- Python 3.8 (tested on 3.8.5)
- PyTorch 1.6.0

and the Python dependencies listed in requirements.txt

- To get started, please run the following commands:
  ```
  conda create -n FGVC
  conda activate FGVC
  conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch
  conda install matplotlib scipy
  pip install -r requirements.txt
  ```

- Next, please download the model weight and demo data using the following command:
  ```
  chmod +x download_data_weights.sh
  ./download_data_weights.sh
  ```

## Quick start

- Object removal:
```bash
cd tool
python video_completion.py \
       --mode object_removal \
       --path ../data/tennis \
       --path_mask ../data/tennis_mask \
       --outroot ../result/tennis_removal \
       --seamless
```

- FOV extrapolation:
```bash
cd tool
python video_completion.py \
       --mode video_extrapolation \
       --path ../data/tennis \
       --outroot ../result/tennis_extrapolation \
       --H_scale 2 \
       --W_scale 2 \
       --seamless
```

You can remove the `--seamless` flag for a faster processing time.
