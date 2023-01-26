import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import cv2


##dataset
mnist = tf.keras.datasets.mnist
(X_train, Y_train), (X_val, Y_val) = mnist.load_data()

print(X_train[0].shape)

#Normalization
X_train = X_train / 255.0
X_val = X_val / 255.0

model = tf.keras.models.Sequential([
    #Feature extraction
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(28,28,1)),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (5,5), activation="relu"),    
    layers.Flatten(),

    #FCN
    layers.Dense(48, activation="relu"),
    layers.Dense(10, activation="softmax")
])    



model.summary()


model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

model.fit(X_train, Y_train, epochs=5, validation_data=(X_val, Y_val))


#test data
model.evaluate(X_val, Y_val)

model.save("mnist.h5")

img = cv2.imread("mnist.png")
img = cv2.resize(img, (28,28))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = img / 255.0
img = img.reshape(1, 28, 28)
result = model.predict([img])
print(result)
print(np.argmax(result))

#CIFAR10  ----> 32x32 color images
#train, validation, test
#weights and biases