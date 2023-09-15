import cv2
import pandas as pd
import os

import lpdr.recognition.darknet.darknet as darknet


cwd = os.path.dirname(__file__)

CFG_FILE        = cwd + "/config-files/cfg/custom-yolov4-tiny-detector.cfg"
WEIGTHS_FILE    = cwd + "/config-files/weigths/custom-yolov4-tiny-detector_best.weights"
DATA_FILE       = cwd + "/config-files/data/obj.data"

network, class_names, class_colors = darknet.load_network(CFG_FILE, DATA_FILE, WEIGTHS_FILE)
width = darknet.network_width(network)
height = darknet.network_height(network)

# darknet helper function to run detection on image
def darknet_helper(img, width, height):
    darknet_image = darknet.make_image(width, height, 3)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height),
                                interpolation=cv2.INTER_LINEAR)

    # get image ratios to convert bounding boxes to proper size
    img_height, img_width, _ = img.shape
    width_ratio = img_width/width
    height_ratio = img_height/height

    # run model on darknet style image to get detections
    darknet.copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = darknet.detect_image(network, class_names, darknet_image)
    darknet.free_image(darknet_image)
    return detections, width_ratio, height_ratio


def get_plate_text(image):
    detections, width_ratio, height_ratio = darknet_helper(image, width, height)

    detections_ = []
    for detection in detections:
        class_name, score, cord = detection
        x1, y1, x2, y2 = cord

        detections_.append([class_name, score, x1, y1, x2, y2])

    df_detections = pd.DataFrame(detections_, columns=["Class Name", "Score", "X1", "Y1", "X2", "Y2"])
    df_detections.sort_values(by=["X1"], inplace=True)

    char_list = df_detections["Class Name"]
    plate_text = ''.join(map(str, char_list))
    return plate_text


