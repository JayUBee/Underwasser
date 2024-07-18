import matplotlib.pyplot as plt 

def plot_training(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    epochs = range(len(acc))
    
    plt.plot(epochs, acc, 'r', label='Training accuracy')
    plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.legend(loc=0)
    plt.figure()
    
    plt.show()


def plot_prediction(path, range):
    #open txt file
    file = open(path, "r")
    #read the file
    lines = file.readlines()
    for line in lines:
        x, y = line.split(":")
        if int(x) < range:
            plt.bar(x, y)
    plt.show()
    file.close()
