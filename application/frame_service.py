from __future__ import annotations
from adapters.inbound import get_frame_handler_indoor_camera, get_frame_handler_outdoor_camera
from application.ports.inbound.frame_handler import FrameHandler
from common.singleton import SingletonMeta
import numpy

def get_frame_service():
    return FrameService(get_frame_handler_outdoor_camera(),get_frame_handler_indoor_camera())

class FrameService(metaclass=SingletonMeta):
    def __init__(self, outdor_frame_handler: FrameHandler,indor_frame_handler: FrameHandler) -> None:
        self.outdor_frame_handler = outdor_frame_handler
        self.indor_frame_handler = indor_frame_handler
        
    def get_indor_frame(self) -> 'numpy.ndarray' | None :
        frame = self.indor_frame_handler.get_frame()
        if frame is not None:
            return frame
        return None
    
    def get_outdor_frame(self) -> 'numpy.ndarray' | None :
        frame = self.outdor_frame_handler.get_frame()
        if frame is not None:
            return frame
        return None