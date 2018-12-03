

camera_server_url = 'http://localhost:5000'
camera_server_image_url = '{}/image.jpg'.format(camera_server_url)

# Specifies the darkflow model
model_options = {"model": "cfg/yolo.cfg", "load": "weights/yolo.weights", "threshold": 0.4}

# Specifies what objects to detect
# See cfg/coco.names for other labels
labels = [
    'bird',
    'cat'
]

base_image_path = './detected_images'
base_labeled_image_path = './labeled_images'

# If true detected objects will be labelled with a box drawn on the image
draw_box = True

# Change this to use local images
local_image_path = './test_images'
# local_image_path = ''