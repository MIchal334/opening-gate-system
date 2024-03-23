from abc import ABC, abstractmethod
import numpy


class FrameHandler(ABC):

    @abstractmethod
    def get_frame(self) -> 'numpy.ndarray'|None:
        pass