This repository contains the files that are necessary to run the pipeline of out hybrid CNNs on different datasets using different architectures.
Each folder corresponds to a different (architecture,dataset) pair.
In order to run the pipeline in the ideal case (ignoring the effects of cross-talk between channels), run the hybrid_onn_pipeline_ideal.py file of the corresponding folder on a terminal.
In order to run the pipeline in the non-ideal case (incorporating the effects of cross-talk between channels), run the hybrid_onn_pipeline_nonideal.py file of the corresponding folder on a terminal.

For these pipelines to work, some files (which could not be uploaded to Github because of their size) need to be added:
- The CIFAR-10 python files downloaded from https://www.cs.toronto.edu/~kriz/cifar.html need to be added to HybridCNN_CodeRepo/AlexNet_CIFAR10/cifar-10-batches-py/
- HybridCNN_CodeRepo/VGG_CIFAR100/weights/ needs to have a file called cifar100vgg_pretrained.h5, which can be downloaded from
- HybridCNN_CodeRepo/ResNet50_CIFAR100/weights/Final/ needs to have a file called model_finetuned_2020-09-01-07-46.h5, which can be downloaded from
