import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

from darkflow.net.build import TFNet

import config


class Predictor():
    """
    Used to get predictions for detected objects in images.
    """

    def __init__(self, model_options={}):

        if not model_options:
            model_options = config.model_options

        self.tfnet = TFNet(model_options)
        logging.debug('tfnet initiated')

    def predict(self, detection_image_cv2):
        """
        Use the tfnet to predict on an image.
        
        :param detection_image_cv2: cv2 image to get an object detection prediction on
        :type detection_image_cv2: np.array
        """

        logging.debug('predict')
        prediction = self.tfnet.return_predict(detection_image_cv2)
        return prediction

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
