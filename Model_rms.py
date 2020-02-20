import os
import tensorflow

from keras import layers
from keras.models import Model

from keras.applications.inception_v3 import InceptionV3
print('299*299, mixed5 (all trained), no weights, 512 nodes,  0.2 dropout, Batch size 20/5, 50 epochs 100 steps, rmsprop(.0003), without weights ')
local_weights_file = '/project/DRDLM/model_weights/weights'
pre_trained_model = InceptionV3(input_shape = (299, 299, 3),
                                include_top = False,
                                weights = None)



for layer in pre_trained_model.layers:
  layer.trainable = False
  
for layer in pre_trained_model.layers:
        layer.trainable = True
        if layer == 'mixed7':
         break   


last_layer = pre_trained_model.get_layer('mixed7')
print('last layer output shape: ', last_layer.output_shape)
last_output = last_layer.output

from keras import optimizers
from keras import metrics
x = layers.Flatten()(last_output)
x = layers.Dense(1024, activation = 'relu')(x)
x = layers.Dropout(0.2)(x)
x = layers.Dense(512, activation = 'relu')(x)
x = layers.Dropout(0.2)(x)
x = layers.Dense(5, activation = 'softmax')(x)

model = Model(pre_trained_model.input, x)

rms = optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=1e-6)
model.compile(optimizer = rms,
             loss = 'categorical_crossentropy',
             metrics = ['acc', 'categorical_accuracy'])

import os


from keras.preprocessing.image import ImageDataGenerator

base_dir = '/project/DRDLM/data/mika'
train_dir = os.path.join( base_dir, 'four_train')


validation_dir = os.path.join( base_dir, 'four_test')


train_0_dir = os.path.join(train_dir, 'sub_0')
train_1_dir = os.path.join(train_dir, 'sub_1')
train_2_dir = os.path.join(train_dir, 'sub_2')
train_3_dir = os.path.join(train_dir, 'sub_3')
train_4_dir = os.path.join(train_dir, 'sub_4')

validation_0_dir = os.path.join(validation_dir, 'sub_0')
validation_1_dir = os.path.join(validation_dir, 'sub_1')
validation_2_dir = os.path.join(validation_dir, 'sub_2')
validation_3_dir = os.path.join(validation_dir, 'sub_3')
validation_4_dir = os.path.join(validation_dir, 'sub_4')

train_0_fnames = os.listdir(train_0_dir)
train_1_fnames = os.listdir(train_1_dir)
train_2_fnames = os.listdir(train_2_dir)
train_3_fnames = os.listdir(train_3_dir)
train_4_fnames = os.listdir(train_4_dir)

# Add our data-augmentation parameters to ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255.,
                                  rotation_range = 40,
                                  horizontal_flip = True,
                                  vertical_flip = True)

# Note that the validation data should not be augmented!
test_datagen = ImageDataGenerator( rescale = 1.0/255. )

# Flow training images in batches of 20 using train_datagen generator
train_generator = train_datagen.flow_from_directory(train_dir,
                                                   batch_size = 20,
                                                   class_mode = 'categorical',
                                                   target_size = (299, 299))
# Flow validation images in batches of 20 using test_datagen generator
validation_generator = test_datagen.flow_from_directory(validation_dir,
                                                   batch_size = 5,
                                                   class_mode = 'categorical',
                                                   target_size = (299, 299))
history = model.fit_generator(train_generator, validation_data = validation_generator, steps_per_epoch = 100, epochs = 50, validation_steps = 50, verbose = 1)



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend(loc=0)
fig1 = plt.gcf()
plt.show()
plt.draw()
fig1.savefig('Model_rms.png', dpi=100)
