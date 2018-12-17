# Camera Server

## Setup

1. Create a python virtual environment and activate:

```sh
virtualenv venv;
source venv/bin/activate
```

2. Install dependencies:

```sh
python3 -m pip install -r requirements.txt
```

3. If running using webcam:

```sh
python3 -m pip install opencv-python==3.4.4.19
```

or if using picamera on raspberry pi:

```sh
python3 -m pip install picamera==1.13
```

## Example Usage

Run the camera server:

```sh
sh run.sh
```

Visit the url `localhost:8000/image` to see an image the camera captures.

Go to `localhost:8000` to see a video streaming demo. 