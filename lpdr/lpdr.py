import cv2
import numpy as np

import lpdr.detection.detection as detection
import lpdr.recognition.recognition as recognition

def get_license_plate(image):
    
    df_plates = detection.get_plates_image(image)

    if len(df_plates) is not 0 :
        plates_text = []
        for index, plates in df_plates.iterrows():
            plate_bytes = plates['image']
            plate_buffer = np.frombuffer(plate_bytes, dtype=np.uint8)
            plate_image = cv2.imdecode(plate_buffer, cv2.IMREAD_COLOR)
            plate_text = recognition.get_plate_text(plate_image)
            plates_text.append(plate_text)
        
        df_plates["text"] = plate_text

    return df_plates.values