import os

import streamlit as st
import tensorflow as tf
from tensorflow.python import keras

from constants import MODEL_PATH, LATENT_DIM, IMAGE_SIZE


# load trained generator
generator = keras.models.load_model(MODEL_PATH)


def generate():
    z = tf.random.normal(shape=(1, LATENT_DIM))
    fake_image = generator(z)
    return (fake_image * 255).numpy().astype("int32")[0]


st.header("Nebulae generator")
st.write(f"""
With this single page application, you can create a brand new nebula image (size {IMAGE_SIZE}x{IMAGE_SIZE} pixels).
The model has been trained with the **TensorFlow** library.
Created by [Guillaume Letellier](https://guillaumeletellier-portfolio.netlify.app/)
""")
if st.button("Generate new nebula"):
    image = generate()
    tf.keras.preprocessing.image.array_to_img(image).save(os.path.join(".", "nebula.png"))
    
    st.image(image)
    with open("nebula.png", "rb") as file:
        st.download_button("Download image", file, file_name="nebula.png", mime="image/png")
