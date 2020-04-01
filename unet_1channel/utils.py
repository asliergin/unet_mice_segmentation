import matplotlib.pyplot as plt


#def plot_segm_history(history, metrics=["accuracy"], losses=["binary_crossentropy"]):
def plot_segm_history(history):
    """[summary]
    Args:
        history ([type]): [description]
        metrics (list, optional): [description]. Defaults to ["iou", "val_iou"].
        losses (list, optional): [description]. Defaults to ["loss", "val_loss"].
    """
    # summarize history for iou
    plt.plot(history.history['accuracy'])
#    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.xticks([1,2,3,4,5])
#    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(history.history['loss'])
#    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
#    plt.legend(['train', 'test'], loc='upper left')
    plt.show()