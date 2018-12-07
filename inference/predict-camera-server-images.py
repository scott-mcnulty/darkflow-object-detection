import time
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
from collections import OrderedDict

from images import Imager
from predict import Predictor
import config


def start(p):

    while True:

        logging.info('Getting image from camera server')
        detection_image_cv2 = Imager.get_image_camera_server(config.camera_server_image_url)
        detections = p.predict(detection_image_cv2)
        original_detected_image = detection_image_cv2.copy()
        logging.debug('Got detections: {}'.format(detections))

        # Nothing detected. Continue to next iteration
        if not detections:
            logging.info('No objects detected')
            sleep_time = 4
            logging.info('Sleeping for {} seconds.'.format(sleep_time))
            time.sleep(sleep_time)
            continue
        
        labels = [detection['label'] for detection in detections]
        logging.info('Found objects with labels: {}'.format(labels))

        # Look through the things that were detected
        for detection in detections:

            # Save any images where an object we're looking for exists
            if detection['label'] in config.labels or not config.labels:

                # Draw the detection box if specified
                if config.draw_box:
                    labelled_image_cv2 = Imager.draw_box(detection, detection_image_cv2)
                    labelled_image_cv2 = Imager.draw_label(detection, labelled_image_cv2)

            else:
                del labels[labels.index(detection['label'])]


        non_duplicated_labels = list(OrderedDict.fromkeys(labels))
        logging.debug('non duplicated labels: {}'.format(non_duplicated_labels))
        if len(non_duplicated_labels) == 1:
            Imager.save_image(config.base_image_path, non_duplicated_labels[0], original_detected_image)
            Imager.save_image(config.base_labeled_image_path, non_duplicated_labels[0], labelled_image_cv2)

        else:
            label = 'combo'
            Imager.save_image(config.base_image_path, label, original_detected_image)
            Imager.save_image(config.base_labeled_image_path, label, labelled_image_cv2)

        sleep_time = 4
        logging.info('Sleeping for {} seconds.'.format(sleep_time))
        time.sleep(sleep_time)


if __name__ == '__main__':

    p = Predictor()
    start(p)
    