# Camera Server

## Setup

1. Create a python virtual environment and activate:

```sh
virtualenv venv;
source venv/bin/activate
```

2. Install dependencies:

```sh
python3 -m pip install opencv-python flask
```

## Example Usage

Run the camera server:

```sh
python3 app.py
```

Visit the url `localhost:5000/image.jpg` to see an image the camera captures.