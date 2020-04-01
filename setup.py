import setuptools

DESCRIPTION = "Implementation of U-Net: Convolutional Networks for Biomedical Image Segmentation. using Keras for 3 color and 1 color mice images to segment mice organs"
LONG_DESCRIPTION = open("README.md").read()
INSTALL_REQUIRES = open("requirements.txt").read()

setuptools.setup(
    name="unet_mice_segmentation",
    version="0.1",
    author="Asli Ergin",
    author_email="asli.ergin@helmholtz-muenchen.de",
    description=DESCRIPTION,
    url="https://ascgitlab.helmholtz-muenchen.de/asli.ergin/segmentation",
    packages=["unet_mice_segmentation"],
    long_description=LONG_DESCRIPTION,
    install_requires=INSTALL_REQUIRES
)
