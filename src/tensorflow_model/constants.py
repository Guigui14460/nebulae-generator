import os


# all directories and files things
ROOT_DIR = "."
OUTPUT_DIR = os.path.join(ROOT_DIR, "out")
TRAINING_DATA_DIR = os.path.join(ROOT_DIR, "data")
GENERATED_IMAGES_DIR = os.path.join(OUTPUT_DIR, "generated", "tensorflow")
GENERATED_IMAGES_TRAINING_DIR = os.path.join(GENERATED_IMAGES_DIR, "training")
GENERATED_IMAGES_TESTING_DIR = os.path.join(GENERATED_IMAGES_DIR, "testing")
MODEL_DIR = os.path.join(OUTPUT_DIR, "models", "tensorflow")
MODEL_PATH = os.path.join(MODEL_DIR, "model.h5")
os.makedirs(GENERATED_IMAGES_TRAINING_DIR, exist_ok=True)
os.makedirs(GENERATED_IMAGES_TESTING_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)

# image things
IMAGE_SIZE = 128
NUMBER_CHANNELS = 3
IMAGE_SHAPE = (IMAGE_SIZE, IMAGE_SIZE)

# all train things
BATCH_SIZE = 8
LATENT_DIM = 100
EPOCHS = 200
LEARNING_RATE = 0.0002
BETA1 = 0.8
BETA2 = 0.999
