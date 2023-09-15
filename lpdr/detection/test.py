import cv2
import numpy as np

im = cv2.imread('prueba.jpg')



bytes_str = cv2.imencode('.jpg', im)[1].tobytes()

#print(np.array(bytes_str).tostring())
with open("text.txt","w") as file:
    file.write("{}".format(bytes_str))