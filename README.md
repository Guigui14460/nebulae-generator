# Nebulae Generator

Project consisting in creating a generative model able to generate images of nebulae (planetary, dark, diffuse, protoplanetary or as supernova remnant).

## Table of contents

  - [Table of contents](#table-of-contents)
  - [Setup](#setup)
  - [Commands](#commands)
  - [Authors](#authors)
  - [License](#license)

## Setup
To get the project and all dependencies, you need to get the associated submodule with the project. There is the data available on the [Guigui14460/nebulae-generator-data repository](https://github.com/Guigui14460/nebulae-generator-data). You can juste launch the following command to get all :
```bash
$ git clone --recursive https://github.com/Guigui14460/nebulae-generator.git
```

You need to have Python 3 installed in your machine and you can run the following commands to setup packages of the project :
```bash
$ pipenv install
$ pipenv shell
# you can install pytorch package to train/test pytorch model
$ pip3 install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html
```

## Commands
You can choose which library to use between TensorFlow and PyTorch :
- TensorFlow
  - for training :
```sh
$ python3 src/tensorflow/train.py
```
  - for testing :
```sh
$ python3 src/tensorflow/test.py
```
- PyTorch
  - for training :
```sh
$ python3 src/pytorch/train.py
```
  - for testing :
```sh
$ python3 src/pytorch/test.py
```


## Authors
- [LETELLIER Guillaume](https://github.com/Guigui14460)

## License
Project under the "GNU General Public License v3.0" license.
