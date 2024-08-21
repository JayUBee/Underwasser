#from modelCompiler import  model
#from dataGenerator import train_generator, validation_generator
import matplotlib.pyplot as plt
import sys
sys.path.append('../')
import plot

#history = model.fit(
#train_generator,
#epochs=15,
#steps_per_epoch=10,
#validation_data=validation_generator,
#validation_steps=3,
#verbose=1
#)
#
#model.save("rps2.h5")



# Mock data for history
history = {
    'loss': [0.5, 0.4, 0.3, 0.2, 0.1],
    'accuracy': [0.8, 0.85, 0.9, 0.92, 0.95],
    'val_loss': [0.6, 0.5, 0.4, 0.3, 0.2],
    'val_accuracy': [0.75, 0.8, 0.85, 0.88, 0.9]
}

# Plot training history
plot.plot_training(history)
plt.show()
