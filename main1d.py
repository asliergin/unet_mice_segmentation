from unet_1channel.model import *
from unet_1channel.data import *
import os
import matplotlib.pyplot as plt

#os.environ["CUDA_VISIBLE_DEVICES"] = "0"


data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.05,
                    height_shift_range=0.05,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')


myGene = trainGenerator(2,'unet_1channel/data1d/train','frames','masks',data_gen_args,save_to_dir = None)

model = unet()
model_checkpoint = ModelCheckpoint('unet1d.hdf5', monitor='loss',verbose=1, save_best_only=True)
model.fit_generator(myGene,steps_per_epoch=300,epochs=1,callbacks=[model_checkpoint])
# try tensorboard instead

testGene = testGenerator("unet_1channel/data1d/test")
results = model.predict_generator(testGene,30,verbose=1)

if not os.path.exists("unet_1channel/data1d/results"):
    os.makedirs("unet_1channel/data1d/results")
saveResult("data1d/test",results)



