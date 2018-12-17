#!/usr/bin/env python
import os
import time

from flask import Flask, render_template, Response, jsonify

from .configs import config
if config.USE_PICAMERA:
    from .pi_camera import Camera
else:
    from .opencv_camera import Camera

app = Flask(__name__)
stop = False


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/stop_video', methods=['POST'])
def stop_video():
    global stop
    stop = True
    return jsonify({'message': 'Set stop var'})


@app.route('/start_video', methods=['POST'])
def start_video():
    global stop
    stop = False
    return jsonify({'message': 'Unset stop var'})


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        if not stop:
            time.sleep(config.FRAME_SLEEP)
        else:
            break


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen_image(camera):
    frame = camera.get_frame()
    yield frame


@app.route('/image')
def image():
    return Response(gen_image(Camera()),
                    mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
