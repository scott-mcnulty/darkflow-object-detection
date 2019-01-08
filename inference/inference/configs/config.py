

camera_server_url = 'http://localhost:5000'
camera_server_image_url = '{}/image'.format(camera_server_url)
camera_server_video_feed_url = '{}/video_feed'.format(camera_server_url)

# Specifies the darkflow model
model_options = {"model": "cfg/yolo.cfg", "load": "weights/yolo.weights", "threshold": 0.4}

# Specifies what objects to detect
# See cfg/coco.names for other labels
labels = [
    'bird',
    'cat'
]

# Uncomment to see all labels drawn (specified in the example usage scripts)
# labels = []

# Try other labels
# labels = [
#     'person',
#     'tvmonitor'
# ]

base_image_path = './images/detected-images'
base_labeled_image_path = './images/labeled-images'

# If true detected objects will be labeled with a box drawn on the image
draw_box = True
# draw_box = False

# Change this to use local images
local_image_path = './test-images'
# local_image_path = ''