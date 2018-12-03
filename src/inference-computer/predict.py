import datetime
import os
from io import BytesIO
from os import listdir
from os.path import isfile, join
import time
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from PIL import Image, ImageDraw
import cv2
import numpy as np
import requests

from darkflow.net.build import TFNet

import config



class Predictor():
    """Used to get predictions for detected objects in images."""

    def __init__(self):

        # Loads the darkflow model according the the model_optionss
        self.tfnet = TFNet(config.model_options)
        logging.debug('tfnet initiated')

    def start(self):
        """Starts the prediction script. If config.local_image_path is
        specified images in that directory are used for detection
        """

        if config.local_image_path:
            logging.debug('local image start')
            self.predict_images_local(draw_box=config.draw_box)
        else:
            logging.debug('camera server start')
            self.predict_images_camera_server(draw_box=config.draw_box)

    def save_image(self, base_path, label, detection_image, use_date=False):
        """Saves an image based on some supplied filepath options."""

        logging.debug('save_image')
        if use_date:
            now = datetime.datetime.now()
            save_path = '{}/{}/{}/{}/{}'.format(base_path, label, now.year, now.month, now.day)

        else:
            save_path = '{}/{}'.format(base_path, label)

        try:
            path, dirs, files = next(os.walk(save_path))
        except StopIteration:
            os.makedirs(save_path)
    
        path, dirs, files = next(os.walk(save_path))
        file_count = len(files)
        detection_image.save('{}/{}.jpg'.format(save_path, file_count))

    def draw_boxes(self, detections, detection_image):
        """Draws boxes on the image that was predicted on.
        The different detections will have labelled boxes around them"""

        logging.debug('draw_boxes')
        draw = ImageDraw.Draw(detection_image)
        for detection in detections:

            if detection['label'] in config.labels:
                draw.rectangle([detection['topleft']['x'], detection['topleft']['y'], 
                                detection['bottomright']['x'], detection['bottomright']['y']],
                            outline=(255, 0, 0))
                draw.text([detection['topleft']['x'], detection['topleft']['y'] - 13], detection['label'], fill=(255, 0, 0))

        return draw

    def predict(self, detection_image):
        """Use the tfnet to predict on an image"""

        logging.debug('predict')
        prediction = self.tfnet.return_predict(detection_image)
        return prediction

    def get_image_local(self, local_image_path):
        """Get an image from a local directory"""
        detection_image = Image.open(local_image_path).convert('RGB')
        detection_image_cv2 = cv2.cvtColor(np.array(detection_image), cv2.COLOR_RGB2BGR)

        return detection_image, detection_image_cv2

    def get_image_camera_server(self):
        """Get an image from a camera server"""

        # Set camera server url in config.py
        r = requests.get(config.camera_server_image_url)
        detection_image = Image.open(BytesIO(r.content))
        detection_image_cv2 = cv2.cvtColor(np.array(detection_image), cv2.COLOR_RGB2BGR)

        return detection_image_cv2

    def predict_images_local(self, draw_box=False):
        """Gets images from a local directory and saves them."""

        files = [f for f in listdir(config.local_image_path) if isfile(join(config.local_image_path, f))]
        logging.debug('local files: {}'.format(files))
        for f in files:

            logging.info('Getting image from local file: {}'.format(f))
            detection_image, detection_image_cv2 = self.get_image_local('{}/{}'.format(config.local_image_path, f))
            prediction = self.tfnet.return_predict(detection_image_cv2)
            
            # Look through the things that were detected
            for detection in prediction:

                # Save any images where an object we're looking for exists
                if detection['label'] in config.labels:
                    self.save_image(config.base_image_path, detection['label'], detection_image)

                    # Draw the detection box if specified
                    if draw_box:
                        drawn_on_image = self.draw_boxes(prediction, detection_image)
                        self.save_image(config.base_labeled_image_path, '', detection_image)

                    break

    def predict_images_camera_server(self, draw_box=False):
        """Gets images and saves them."""

        while True:

            logging.info('Getting image from camera server')
            detection_image_cv2 = self.get_image_camera_server(config.local_image_path)
            prediction = self.tfnet.return_predict(detection_image_cv2)
            
            for detection in prediction:
                if detection['lable'] in config.labels:
                    self.save_image(config.base_image_path, detection['label'], detection_image_cv2, True)

            if draw_box:
                drawn_on_image = self.draw_boxes(prediction, detection_image)
                self.save_image(config.base_labeled_image_path, '', detection_image)

            time.sleep(4)
