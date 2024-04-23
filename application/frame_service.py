from __future__ import annotations
from application.ports.inbound.frame_handler import FrameHandler
from common.singleton import SingletonMeta
import numpy
import threading


class FrameService(metaclass=SingletonMeta):
    def __init__(self, outdor_frame_handler: FrameHandler,indoor_frame_handler: FrameHandler) -> None:
        self.outdor_frame_handler = outdor_frame_handler
        self.indoor_frame_handler = indoor_frame_handler
        outdoor_frame_handler_thread = threading.Thread(target=self.outdor_frame_handler.start_handler, daemon=True, name=f"cam-outdoor")
        indoor_frame_handler_thread= threading.Thread(target=self.indoor_frame_handler.start_handler, daemon=True, name=f"cam-indoor")
        indoor_frame_handler_thread.start()
        outdoor_frame_handler_thread.start()
        
    def get_indoor_frame(self) -> 'numpy.ndarray' | None :
        frame = self.indoor_frame_handler.get_frame()
        if frame is not None:
            return frame
        return None
    
    def get_outdoor_frame(self) -> 'numpy.ndarray' | None :
        frame = self.outdor_frame_handler.get_frame()
        if frame is not None:
            return frame
        return None
