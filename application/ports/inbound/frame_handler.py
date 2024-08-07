from __future__ import annotations
from abc import ABC, abstractmethod
import numpy



class FrameHandler(ABC):

    @abstractmethod
    def get_frame(self) -> 'numpy.ndarray'|None:
        pass
        
    @abstractmethod
    def start_handler(self):
        pass
