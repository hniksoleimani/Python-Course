import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split



#Dataset
(images_train, labels_train), (images_test, labels_test) = datasets.cifar10.load_data()

images_train, X_val, labels_train, Y_val = train_test_split(images_train, labels_train, test_size=0.1, random_state=24, shuffle=False)


# Printing out train, test and validation sets
print('images_train : ')
print(images_train.shape)
print('')
print('images_test : ')
print(images_test.shape)
print('')
print('X_val : ')
print(X_val.shape)
print('')
print('labels_train : ')
print(labels_train.shape)
print('')
print('labels_test : ')
print(labels_test.shape)
print('Y_val : ')
print(Y_val.shape)


#Verify the data
class_names = ['airplane', 'automibile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(images_train[i])
    # The CIFAR labels happen to be arrays, 
    # which is why you need the extra index
    plt.xlabel(class_names[labels_train[i][0]])
plt.savefig('sample_data.jpg')


#Applying Normalization
images_train, images_test = images_train / 255.0, images_test / 255.0


#Feature Extraction using CNN
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3,3), activation='relu'))


#FCN
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))

model.summary()

#Compile and train the model
model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])

history = model.fit(images_train, labels_train, epochs=5, validation_data=(X_val, Y_val))


#Test data
model.evaluate(X_val, Y_val)

model.save("CIFAR10.h5")


plt.figure(figsize=(10,10))
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
# plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.savefig('statistics.jpg')

test_loss, test_acc = model.evaluate(images_test,  labels_test, verbose=2)
print(test_loss)
print(test_acc)
