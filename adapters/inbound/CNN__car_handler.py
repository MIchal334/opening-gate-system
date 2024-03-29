from application.ports.inbound.car_handler import CarHandler
import numpy
from keras.models import load_model

class CNNCarHandler(CarHandler):

    def __init__(self, cnn_path: str) -> None:
        self.cnn_path = cnn_path
        self.model = None

    def start_cnn(self):
        self.model = load_model(self.cnn_path)

    def chek_if_car_on_image(self, image: 'numpy.ndarray') -> bool:
        pass
