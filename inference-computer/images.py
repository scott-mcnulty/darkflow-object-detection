import datetime
import os
from io import BytesIO
from os import listdir
from os.path import isfile, join
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

import numpy as np
import requests
from PIL import Image, ImageDraw
import cv2

import config


class Imager():
    """
    Handles image fetching/storing/other prep for interacting with the
    predict.Predictor class
    """
    
    @staticmethod
    def get_image_camera_server(url=''):
        """
        Get an image from a camera server.
        
        :param url: url to the get an image from the camera server
        :type url: str
        :returns: tuple of the detection image and the cv2 detection image
        :rtype: (PIL.Image, np.array)
        """

        if not url:
            url = config.camera_server_image_url

        r = requests.get(url)
        detection_image = Image.open(BytesIO(r.content))
        detection_image_cv2 = cv2.cvtColor(np.array(detection_image), cv2.COLOR_RGB2BGR)

        return detection_image, detection_image_cv2

    @staticmethod
    def get_file_strings_from_local(local_path=''):
        """
        Gets a list of files names from a local path

        :param local_path: (Optional) local path to look for image files
        :type local_path: str
        :returns: List of file name strings
        :rtype: list
        """
        if not local_path:
            local_path = config.local_image_path
        
        files = [f for f in listdir(local_path) if isfile(join(local_path, f))]
        logging.debug('local files: {}'.format(files))
    
        return files

    @staticmethod
    def get_image_local(local_image_path):
        """
        Get an image from a local directory.
        
        :param local_image_path: string path to get an image from the local file system
        :type local_image_path: str
        :returns: tuple of the detection image and the cv2 detection image
        :rtype: (PIL.Image, np.array)
        """

        detection_image = Image.open(local_image_path).convert('RGB')
        detection_image_cv2 = cv2.cvtColor(np.array(detection_image), cv2.COLOR_RGB2BGR)

        return detection_image, detection_image_cv2

    @staticmethod
    def draw_boxes(detections, detection_image):
        """
        Draws boxes on the image that was predicted on.
        The different detections will have labeled boxes around them.

        Uses all labels if config.labels is unspecified.
        
        :param detections: Detection predictions from the model.
        :type detections: dict
        :param detection_image: Image to draw boxes on
        :type detection_image: PIL.Image
        :returns: None
        :rtype: None
        """

        logging.debug('draw_boxes')
        draw = ImageDraw.Draw(detection_image)
        for detection in detections:

            if detection['label'] in config.labels or not config.labels:
                draw.rectangle([detection['topleft']['x'], detection['topleft']['y'], 
                                detection['bottomright']['x'], detection['bottomright']['y']],
                            outline=(255, 0, 0))
                draw.text([detection['topleft']['x'], detection['topleft']['y'] - 13], detection['label'], fill=(255, 0, 0))

        return

    @staticmethod
    def save_image(base_path, label, detection_image, use_date=False):
        """
        Saves an image based on some supplied filepath options.
        
        :param base_path: Base path to use.
        :type detections: str
        :param label: A label for the image. Typically given by the model from a
        prediction.
        :type label: str
        :param detection_image: Image to save
        :type detection_image: PIL.Image
        :param use_date: Specify if todays date should be used to store as yyyy/mm/dd
        :type use_date: bool
        :returns: None
        :rtype: None
        """

        logging.debug('save_image')
        if use_date:
            now = datetime.datetime.now()
            save_path = '{}/{}/{}/{}/{}'.format(base_path, label, now.year, now.month, now.day)

        else:
            save_path = '{}/{}'.format(base_path, label)

        try:
            path, dirs, files = next(os.walk(save_path))

        # Path not created yet so make it
        except StopIteration:
            os.makedirs(save_path)
    
        path, dirs, files = next(os.walk(save_path))
        file_count = len(files)
        detection_image.save('{}/{}.jpg'.format(save_path, file_count))