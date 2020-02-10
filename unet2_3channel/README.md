# Implementation of deep learning framework -- Unet, using Keras

The architecture was inspired by [U-Net: Convolutional Networks for Biomedical Image Segmentation](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/).

---



## Overview

### Data

We use a TIFF stack that is obtained from 4 different lasers.

1. run reshaping.ipynb to seperate images obtained from different lasers(1 channel), also to make images with 3 channel or 4 channel

### Preparing Images and Masks(This part is not automated)

We pick 10 frames and segment the intestine using GIMP and obtain masks. The save frames under data/train/frames and save masks under data/train/masks renaming them 0.png, 1.png ... , giving same numbers to corresponding masks and frames.

### Data augmentation 3 channel

run dataAugmentation3Channel.ipynb
to obtained augmented data under data/aug in the shape (256,256,3)

#Obtaining data from all (augmented and normal), combining them and making train, test splits

will be automated!

### Model

![img/u-net-architecture.png](img/u-net-architecture.png)

This deep neural network is implemented with Keras functional API, which makes it extremely easy to experiment with different interesting architectures.

Output from the network is a 512*512 which represents mask that should be learned. Sigmoid activation function
makes sure that mask pixels are in \[0, 1\] range.

### Training

The model is trained for 5 epochs.

After 5 epochs, calculated accuracy is about 0.97.

Loss function for the training is basically just a binary crossentropy.


---

## How to use

### Dependencies

This tutorial depends on the following libraries:

* Tensorflow
* Keras >= 1.0

Also, this code should be compatible with Python versions 2.7-3.5.

### Run main.py

You will see the predicted results of test image in data/membrane/test

### Or follow notebook trainUnet



### Results

Use the trained model to do segmentation on test images, the result is statisfactory.

![img/0test.png](img/0test.png)

![img/0label.png](img/0label.png)


## About Keras

Keras is a minimalist, highly modular neural networks library, written in Python and capable of running on top of either TensorFlow or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

Use Keras if you need a deep learning library that:

allows for easy and fast prototyping (through total modularity, minimalism, and extensibility).
supports both convolutional networks and recurrent networks, as well as combinations of the two.
supports arbitrary connectivity schemes (including multi-input and multi-output training).
runs seamlessly on CPU and GPU.
Read the documentation [Keras.io](http://keras.io/)

Keras is compatible with: Python 2.7-3.5.
