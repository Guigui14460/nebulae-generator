import gdown


def get_model(model_path):
    print("Downloading 'nebulae-generator' model from Google Drive...")
    gdown.download("https://drive.google.com/uc?id=1xQ7K6eQ0cu_yOQCC9WtF2_cE5XYN5KHf", model_path, quiet=False)
