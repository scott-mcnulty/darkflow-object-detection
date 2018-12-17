import time
import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
from collections import OrderedDict
import argparse

from images import Imager
from predict import Predictor
import config


def predict_camera_server(p):

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
                    labeled_image_cv2 = Imager.draw_box(detection, detection_image_cv2)
                    labeled_image_cv2 = Imager.draw_label(detection, labeled_image_cv2)

            else:
                logging.info('Deleting label `{}` for detection we\'re not looking for'.format(detection['label']))
                del labels[labels.index(detection['label'])]


        non_duplicated_labels = list(OrderedDict.fromkeys(labels))
        logging.debug('Non duplicated labels: {}'.format(non_duplicated_labels))
        if len(non_duplicated_labels) == 1:
            Imager.save_image(config.base_image_path, non_duplicated_labels[0], original_detected_image)

            try:
                Imager.save_image(config.base_labeled_image_path, non_duplicated_labels[0], labeled_image_cv2)
            except NameError:
                logging.error('No labeled image to save.')

        else:
            label = 'combo'
            Imager.save_image(config.base_image_path, label, original_detected_image)
            
            try:
                Imager.save_image(config.base_labeled_image_path, label, labeled_image_cv2)
            except NameError:
                logging.error('No labeled image to save.')

        sleep_time = 4
        logging.info('Sleeping for {} seconds.'.format(sleep_time))
        time.sleep(sleep_time)


def predict_local(p):

    # Get the files to predict
    files = Imager.get_file_strings_from_local(config.local_image_path)
    for f in files:

        detection_image_cv2 = Imager.get_image_from_local('{}/{}'.format(config.local_image_path, f))

        start = time.time()
        detections = p.predict(detection_image_cv2)
        logging.info('Predicted in {} seconds.'.format(time.time() - start))
        original_detected_image = detection_image_cv2.copy()
        logging.debug('Got detections: {}'.format(detections))


        # Nothing detected. Continue to next iteration
        if not detections:
            logging.info('No objects detected')
            continue
        
        labels = [detection['label'] for detection in detections]
        logging.info('Found objects with labels: {}'.format(labels))
        
        # Look through the things that were detected
        for detection in detections:

            if detection['label'] in config.labels or not config.labels: 

                # Draw the detection box if specified
                if config.draw_box:
                    labeled_image_cv2 = Imager.draw_box(detection, detection_image_cv2)
                    labeled_image_cv2 = Imager.draw_label(detection, labeled_image_cv2)

            else:
                del labels[labels.index(detection['label'])]


        non_duplicated_labels = list(OrderedDict.fromkeys(labels))
        if len(non_duplicated_labels) == 1:
            Imager.save_image(config.base_image_path, non_duplicated_labels[0], original_detected_image)
            Imager.save_image(config.base_labeled_image_path, non_duplicated_labels[0], labeled_image_cv2)

        else:
            label = 'combo'
            Imager.save_image(config.base_image_path, label, original_detected_image)
            Imager.save_image(config.base_labeled_image_path, label, labeled_image_cv2)


if __name__ == '__main__':

    # Make the predictor object
    p = Predictor()

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--camera_server", type=int, default=0,
        help="Whether to predict from camera server images.")
    args = vars(parser.parse_args())


    if args['camera_server']:
        predict_camera_server(p)
    else:
        predict_local(p)
    