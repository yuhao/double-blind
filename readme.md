This repository contains the files that are necessary to run the pipeline of out hybrid CNNs on different datasets using different architectures.
Each folder corresponds to a different (architecture,dataset) pair.
In order to run the pipeline in the ideal case (ignoring the effects of cross-talk between channels), run the hybrid_onn_pipeline_ideal.py file of the corresponding folder on a terminal.
In order to run the pipeline in the non-ideal case (incorporating the effects of cross-talk between channels), run the hybrid_onn_pipeline_nonideal.py file of the corresponding folder on a terminal.

Before running the code, download:

- HybridCNN_CodeRepo/VGG_CIFAR100/weights/ needs to have a file called cifar100vgg_pretrained.h5, which can be downloaded [here](https://drive.google.com/file/d/1OcZhedp_fHo-UtBd3b2WYSlssq_Orct7/view?usp=sharing).
- HybridCNN_CodeRepo/ResNet50_CIFAR100/weights/Final/ needs to have a file called model_finetuned_2020-09-01-07-46.h5, which can be downloaded [here](https://drive.google.com/file/d/1OcZhedp_fHo-UtBd3b2WYSlssq_Orct7/view?usp=sharing).
- The python version of the CIFAR-10 data needs to be downloada from [here](https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz) and added to HybridCNN_CodeRepo/AlexNet_CIFAR10/cifar-10-batches-py/
- 
