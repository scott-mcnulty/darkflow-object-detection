import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from images import Imager
from predict import Predictor
import config


def start(p):

    while True:

        logging.info('Getting image from camera server')
        detection_image_cv2 = Imager.get_image_camera_server(config.local_image_path)
        predictions = p.predict(detection_image_cv2)
        
        # Look through the things that were detected
        for detection in predictions:

            # Save any images where an object we're looking for exists
            if detection['label'] in config.labels:
                Imager.save_image(config.base_image_path, detection['label'], detection_image)

                # Draw the detection box if specified
                if config.draw_box:
                    Imager.draw_boxes(predictions, detection_image)
                    Imager.save_image(config.base_labeled_image_path, detection['label'], detection_image)

                break
        
        sleep_time = 4
        logging.info('Sleeping for {} seconds.'.format(sleep_time))
        time.sleep(sleep_time)


if __name__ == '__main__':

    p = Predictor()
    start(p)
    