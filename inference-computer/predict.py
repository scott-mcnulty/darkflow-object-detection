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
