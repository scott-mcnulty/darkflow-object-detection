from images import Imager
from predict import Predictor
import config


def start(p):

    # Get the files to predict
    files = Imager.get_file_strings_from_local(config.local_image_path)
    for f in files:

        detection_image, detection_image_cv2 = Imager.get_image_local('{}/{}'.format(config.local_image_path, f))
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


if __name__ == '__main__':

    p = Predictor()
    start(p)
    