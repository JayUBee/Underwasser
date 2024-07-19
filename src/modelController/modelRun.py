from modelController.modelCompiler import  model
from modelController.dataGenerator import train_generator, validation_generator
from utils import plot

history = model.fit(
train_generator,
epochs=15,
steps_per_epoch=10,
validation_data=validation_generator,
validation_steps=3,
verbose=1
)

model.save("rps2.h5")

plot.plot_training(history)
