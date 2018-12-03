# Inference Computer

## Setup

1. Create a python virtual environment and activate.

```sh
virtualenv venv;
source venv/bin/activate
```

2. Install dependencies:

```sh
python -m pip install tensorflow numpy opencv-python cython image requests
```

3. Clone darkflow repo:

```sh
git clone https://github.com/thtrieu/darkflow.git
```

4. Install darkflow:

```sh
cd darkflow;
pip install .;
cd ..
```

5. [Download](https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU) some pre-trained yolo weights as specified in the darkflow repo readme. I chose to download yolo.weights. Put the downloaded weights in the `weights` directory.

6. Copy the configs from the darkflow repo:

```sh
cp -r darkflow/cfg .
```

7. Update any necessary values in the config.py file for your case.

8. Run the app:

```sh
python3 app.py
```

## Configuration

See the config.py file to see program options.