# Nebulae Generator

Project consisting in creating a generative model able to generate images of nebulae (planetary, dark, diffuse, protoplanetary or as supernova remnant).

You can access the the streamlit app at [this URL](https://share.streamlit.io/guigui14460/nebulae-generator/main/src/app.py).

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
```

## Commands
You can launch script :
- for training :
```sh
$ python3 src/train.py
```
- for testing :
```sh
$ python3 src/test.py
```


## Authors
- [LETELLIER Guillaume](https://github.com/Guigui14460)

## License
Project under the "GNU General Public License v3.0" license.
