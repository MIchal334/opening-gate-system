from __future__ import annotations
import numpy
import cv2 
import logging
from application.ports.inbound.frame_handler import FrameHandler
import time

logger = logging.getLogger()

class CameraFrameHandler(FrameHandler):
    def __init__(self, p_camera_link) -> None:
        self.camera_link = p_camera_link
        self.capturer = cv2.VideoCapture(self.camera_link)

    def get_frame(self) -> 'numpy.ndarray'|None:
        ret, frame = self.capturer.read()
        
        if not ret:
            logger.info(f"End of stream camera {self.camera_link}")
            self.capturer = cv2.VideoCapture(self.camera_link)

        if frame is not None:
            logger.info(f'Frame is not None from: {self.camera_link}')
            return frame
        
        logger.debug(f'Frame is None from: {self.camera_link}')
        return None