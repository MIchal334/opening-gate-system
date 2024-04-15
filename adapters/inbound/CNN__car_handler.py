import logging
import threading
from application.ports.inbound.car_detenction_handler import CarHandler
import numpy
from keras.models import load_model
import cv2
import numpy as np

logger = logging.getLogger()

class CNNCarHandler(CarHandler):

    def __init__(self, cnn_path: str, frame_x_size: int, frame_y_size: int) -> None:
        self.cnn_path = cnn_path
        self.model = None
        self.frame_x_size = frame_x_size
        self.frame_y_size = frame_y_size
        self.start_cnn()

    def start_cnn(self):
        self.model = load_model(self.cnn_path)
        logger.info(f'START CNN CAR HANDLER {threading.current_thread().getName()}')


    def check_if_car_on_image(self, image: 'numpy.ndarray') -> bool:
        image_prepared = self.__preapre_image_for_proccesing(image)
        result = self.model.predict(image_prepared)
        class_max = np.argmax(result)
        if class_max == 1:
            return True
        return False


    def __preapre_image_for_proccesing(self,img):
        image = cv2.resize(img,(self.frame_x_size,self.frame_y_size))
        image = image[np.newaxis, ...]
        image = np.expand_dims(image, axis=-1)
        return image.astype('float32')/255
