import torch
import cv2

model = torch.hub.load('lpdr/detection/yolov5', 'custom', path='lpdr/detection/weigths/best_yolo_cbam.pt', source='local')

def get_plates_image(image):

    df_results = model(image).pandas().xyxy[0]
    df_detections = df_results[df_results["confidence"] > 0.3]

    if len(df_detections) is not 0 :
        plate_crop = cv2.imencode('.jpg', image[int(df_detections["ymin"]):int(df_detections["ymax"]), int(df_detections["xmin"]):int(df_detections["xmax"]), :])[1].tobytes()

        df_detections["image"] = plate_crop 

    return df_detections
