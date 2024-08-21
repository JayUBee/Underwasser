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


def plot_prediction(path, range_limit=None):
    file = open(path, "r")
    lines = file.readlines()
    data = []

    # Store data in a list of tuples (convert x to int for sorting)
    for line in lines:
        x, y = line.split(":")
        data.append((int(x), float(y.strip())))  # Assuming x is always an integer and y is float

    # Sort the data based on x values
    data.sort(key=lambda pair: pair[0])

    # Plot the data
    for x, y in data:
        if range_limit is None or x < range_limit:
            plt.bar(x, y)

    plt.show()
    file.close()