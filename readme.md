This repository contains the files that are necessary to run the pipeline of out hybrid CNNs on different datasets using different architectures.
Each folder corresponds to a different (architecture,dataset) pair.
In order to run the pipeline in the ideal case (ignoring the effects of cross-talk between channels), run the hybrid_onn_pipeline_ideal.py file of the corresponding folder on a terminal.
In order to run the pipeline in the non-ideal case (incorporating the effects of cross-talk between channels), run the hybrid_onn_pipeline_nonideal.py file of the corresponding folder on a terminal.

Before running the code, download:

- HybridCNN_CodeRepo/VGG_CIFAR100/weights/ needs to have a file called cifar100vgg_pretrained.h5, which can be downloaded [here](https://drive.google.com/file/d/1OcZhedp_fHo-UtBd3b2WYSlssq_Orct7/view?usp=sharing).
- HybridCNN_CodeRepo/ResNet50_CIFAR100/weights/Final/ needs to have a file called model_finetuned_2020-09-01-07-46.h5, which can be downloaded [here](https://drive.google.com/file/d/1OcZhedp_fHo-UtBd3b2WYSlssq_Orct7/view?usp=sharing).
- The python version of the CIFAR-10 data needs to be downloada from [here](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) and added to HybridCNN_CodeRepo/AlexNet_CIFAR10/cifar-10-batches-py/
 
After having added these files to the indicated directories, install Anaconda (if it is not installed already) following the instructions [here](https://docs.anaconda.com/anaconda/install/).

After that, move to the repository's directory and run this command to install the required packages:

  ```shell
 conda create --name tensorflowenv --file spec-file.txt
  ```
  
 Then move to the folder that corresponds to the (architecture,dataset) pair you wish to run, and run these commands if you want to run the ideal case (no cross-talk):
   ```shell
 conda activate tensorflowenv
 python hybrid_onn_pipeline_ideal.py
  ```
  
  If instead you want to run the non-ideal case (with cross-talk), run these commands from the folder that corresponds to the the (architecture,dataset) pair you wish to run:
  ```shell
 conda activate tensorflowenv
 python hybrid_onn_pipeline_nonideal.py
  ```

