import tensorflow as tf


def get_data(validation_data_size):
    mnist = tf.keras.datasets.mnist
    (X_train_full, y_train_full), (X_val,
                                   y_val), (x_test, y_test) = mnist.load_data()

    X_valid, X_train = X_train_full[:validation_data_size] / \
        255., y_train[validation_data_size:] / 255.
    y_valid, y_train = y_train_full[:validation_data_size], y_train_full[validation_data_size:]
    x_test = x_test/255.
    return (X_train, y_train), (X_valid, y_valid), (x_test, y_test)
