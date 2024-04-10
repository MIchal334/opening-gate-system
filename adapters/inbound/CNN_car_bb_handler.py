import numpy
from application.ports.inbound.car_bb_handler import CarBBHandler
from keras.models import load_model
import logging
import threading
import cv2
import numpy as np

logger = logging.getLogger()

class CNNCarBBnHandler(CarBBHandler):
    def __init__(self,cnn_path,frame_x_size,frame_y_size):
        self.cnn_path = cnn_path
        self.model = None
        self.frame_x_size = frame_x_size
        self.frame_y_size = frame_y_size
        self.start_cnn()


    def start_cnn(self):
        self.model = load_model(self.cnn_path)
        logger.info(f'START CNN CAR BB HANDLER {threading.current_thread().getName()}')

    def get_car_bb(self, image: 'numpy.ndarray') -> list:
        image_prepared = self.__preapre_image_for_proccesing(image)
        result = self.model.predict(image_prepared)
        car_boxes =  [result[0][0]*self.frame_x_size,result[0][1]*self.frame_y_size,
                      result[0][2]*self.frame_x_size,result[0][3]*self.frame_y_size]
        return car_boxes

    def __preapre_image_for_proccesing(self,img):
        image = cv2.resize(img, (self.frame_x_size, self.frame_y_size))
        image = image[np.newaxis, ...]
        return image.astype('float32')/255