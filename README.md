# Implementation of deep learning framework -- Unet, using Keras for mice organ segmentation

The architecture was inspired by [U-Net: Convolutional Networks for Biomedical Image Segmentation](http://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/).

---

## Overview

###Getting Started

To download the required packages, it is recommended to make a new virtual environment using the following commands:

conda create enc --name myenv
conda activate myenv

And then to add the virtual environment as jupyter notebook kernel to your environment:

pip install --user ipykernel
python -m ipykernel install --user --name=myenv

So now we have a virtual environment specific for this project. And the environment can be used as Kernel in jupyter notebook while using ipynb files.

To install required packages run:
pip install -r requirements.txt

### Data

Currently I used tiff stack that was obtained from Goldeye camera 4 different lasers (write details).

U-Net models are giving good results even with a few data samples. Using reshaping.ipynb , we can extract frames corresponding to different lasers and save these frames in folders laser1, laser2, laser3, laser4. Now we seperated frames from different lasers.

We can also combine 3 lasers in an image, and make it 3 channel, 4channel... using reshaping.ipynb and save the results under channels3 and channels4

Then we need to pick approximtely 15 frames(preferablly from distant frames) and name them from 0,1,2...



##Data Annotation

This part is manual.

Using GIMP we can draw masks and save them:

Free -> Select
Scissors
Select -> Invert
Colors -> Levels -> Output levels bring to 0
Select - > Invert
Colors -> Levels -> OUtput Levels 1
Export

Name obtained masks with corresponding numbers of their input image.


### Data augmentation

This part can be done if number of data is not enough.

Using dataAugmentation.ipynb we can increase the number of dataset so that we will have more data to be used in training. techniques like rotation, shift, shear, flip, zoom are used to obtain new frames .

The data for training contains 30 512*512 images, which are far not enough to feed a deep learning neural network. I use a module called ImageDataGenerator in keras.preprocessing.image to do data augmentation.

See dataPrepare.ipynb and data.py for detail.

Use data augmentation both for masks and frames


### Model

![img/u-net-architecture.png](img/u-net-architecture.png)

This deep neural network is implemented with Keras functional API, which makes it extremely easy to experiment with different interesting architectures.

Output from the network is a 512*512 which represents mask that should be learned. Sigmoid activation function
makes sure that mask pixels are in \[0, 1\] range.

### Training

The model is trained for 5 epochs.

Loss function for the training is basically just a binary crossentropy.


---

## How to use

### Dependencies

Requirements are listed in requirements.txt
Also, this code should be compatible with Python versions 2.7-3.5.

### How to use
For gray scale images:

After having data under data1d/train/frames (having approximately 45 images) and corresponding masks under data1d/train/masks named from 0,1,2...., and having test images(the ones that you want to segment) THAT ARE NOT USED BEFORE under data1d/test 

run unet_1channel/trainUnet.ipynb to train gray scale images

You will see the predicted results of test image in data1d/results

For 3 color (or rgb) images:

After having data under data3d/train/frames (having approximately 45 images) and corresponding masks under data3d/train/masks named from 0,1,2...., and having test images(the ones that you want to segment) THAT ARE NOT USED BEFORE under data3d/test 

run unet_3channel/trainUnet3.ipynb to train 3 color images

You will see the predicted results of test image in data3d/results



## About Keras

Keras is a minimalist, highly modular neural networks library, written in Python and capable of running on top of either TensorFlow or Theano. It was developed with a focus on enabling fast experimentation. Being able to go from idea to result with the least possible delay is key to doing good research.

Use Keras if you need a deep learning library that:

allows for easy and fast prototyping (through total modularity, minimalism, and extensibility).
supports both convolutional networks and recurrent networks, as well as combinations of the two.
supports arbitrary connectivity schemes (including multi-input and multi-output training).
runs seamlessly on CPU and GPU.
Read the documentation [Keras.io](http://keras.io/)

Keras is compatible with: Python 2.7-3.5.
