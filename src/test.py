import os

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python import keras

from constants import MODEL_PATH, LATENT_DIM, GENERATED_IMAGES_TESTING_DIR


# load trained generator
print("Loading the generator model...", end=" ")
generator = keras.models.load_model(MODEL_PATH)
print("DONE")

for i in range(10):
    print(f"Generate image {i}...", end=" ")
    z = tf.random.normal((1, LATENT_DIM))
    fake_image = generator(z)
    plt.axis("off")
    plt.imshow((fake_image.numpy() * 255).astype("int32")[0])
    plt.savefig(os.path.join(GENERATED_IMAGES_TESTING_DIR, f"{i}.jpg"), bbox_inches='tight', pad_inches=0)
    print("DONE")
