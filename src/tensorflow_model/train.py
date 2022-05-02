import tensorflow as tf
from tensorflow.python import keras
from tensorflow.python.keras import layers

from constants import *
from .gan import GAN, GANMonitor


# data preprocessing
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    TRAINING_DATA_DIR, label_mode=None, shuffle=False,
    image_size=IMAGE_SHAPE, batch_size=BATCH_SIZE,
)
dataset = dataset.map(lambda x: x / 255.0)

# discriminator model
discriminator = keras.Sequential(
    [
        layers.InputLayer(input_shape=(IMAGE_SIZE, IMAGE_SIZE, NUMBER_CHANNELS)),
        layers.Conv2D(IMAGE_SIZE, kernel_size=4, strides=2, padding="same"),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2D(IMAGE_SIZE*2, kernel_size=4, strides=2, padding="same"),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2D(IMAGE_SIZE*2, kernel_size=4, strides=2, padding="same"),
        layers.LeakyReLU(alpha=0.2),
        layers.Flatten(),
        layers.Dropout(0.2),
        layers.Dense(1, activation="sigmoid"),
    ],
    name="discriminator",
)

# generator model
generator = keras.Sequential(
    [
        layers.InputLayer(input_shape=(LATENT_DIM,)),
        layers.Dense(16 * 16 * 128),
        layers.Reshape((16, 16, 128)),
        layers.Conv2DTranspose(128, kernel_size=4, strides=2, padding="same"),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2DTranspose(256, kernel_size=4, strides=2, padding="same"),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2DTranspose(512, kernel_size=4, strides=2, padding="same"),
        layers.LeakyReLU(alpha=0.2),
        layers.Conv2D(3, kernel_size=5, padding="same", activation="sigmoid"),
    ],
    name="generator",
)

# create the adversarial model
gan = GAN(discriminator=discriminator, generator=generator, latent_dim=LATENT_DIM)
gan.compile(
    d_optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE, beta_1=BETA1, beta_2=BETA2),
    g_optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE, beta_1=BETA1, beta_2=BETA2),
    loss_fn=tf.keras.losses.BinaryCrossentropy(),
)

# train the adversarial networks
gan.fit(
    dataset, epochs=EPOCHS, callbacks=[GANMonitor(GENERATED_IMAGES_TRAINING_DIR, num_img=10, latent_dim=LATENT_DIM)]
)

# save the trained generator
generator.save(MODEL_PATH)
