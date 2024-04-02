import logging
from application.ports.inbound.car_handler import CarHandler
import numpy
from keras.models import load_model
import cv2
import numpy as np

logger = logging.getLogger()

class CNNCarHandler(CarHandler):

    def __init__(self, cnn_path: str) -> None:
        self.cnn_path = cnn_path
        self.model = None
        self.start_cnn()

    def start_cnn(self):
        self.model = load_model(self.cnn_path)
        logger.info('START CNN CAR HANDLER')


    def chek_if_car_on_image(self, image: 'numpy.ndarray') -> bool:
        image_prepared = self.__preapre_image_for_proccesing(image)
        result = self.model.predict(image_prepared)
        class_max = np.argmax(result)
        if class_max == 1:
            return True
        return False


    def __preapre_image_for_proccesing(self,img):
        x_size = 64
        y_size = 64
        image = cv2.resize(img, (x_size, y_size))
        image = image[np.newaxis, ...]
        image = np.expand_dims(image, axis=-1)
        return image.astype('float32')/255
