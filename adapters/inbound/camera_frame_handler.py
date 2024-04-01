from __future__ import annotations
import numpy
import cv2 
import logging
from application.ports.inbound.frame_handler import FrameHandler

logger = logging.getLogger()

class CameraFrameHandler(FrameHandler):
    def __init__(self, p_camera_link) -> None:
        self.camera_link = p_camera_link
        self.capturer = cv2.VideoCapture(p_camera_link)

    def get_frame(self) -> 'numpy.ndarray'|None:
        ret, frame = self.capturer.read()

        if frame is not None:
            logger.info(f'Frame is not None from: {self.camera_link}')
            return frame
        
        logger.info(f'Frame is None from: {self.camera_link}')
        return None
        
            
