from mypack.plotTB import plot1d, create_axes

def plot_result(history):
    axes = create_axes(1, 2)
    plot1d(history.epoch, history.history['loss'], label='train loss', ax=axes[0, 0])
    plot1d(history.epoch, history.history['val_loss'], label='val loss', legend=True, ax=axes[0, 0])
    plot1d(history.epoch, history.history['accuracy'], label='train acc', ax=axes[0, 1])
    plot1d(history.epoch, history.history['val_accuracy'], label='val acc', legend=True, ax=axes[0, 1])
    print('train accurary:', history.history['accuracy'][-1])
    print('val accurary:', history.history['val_accuracy'][-1])