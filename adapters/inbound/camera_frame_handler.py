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
        self.crashed_time = time.time()
        self.last_frame = None
        logger.info(f'START CAMERA : {self.camera_link}')
        
    def start_handler(self):
        while True:
            ret, frame = self.capturer.read()
            if not ret:
                now = time.time()
                logger.error(f"End of stream camera {self.camera_link} time = {now - self.crashed_time} ")
                self.capturer = cv2.VideoCapture(self.camera_link)
                self.crashed_time  = now
            if frame is not None:
                self.last_frame = frame
        

    def get_frame(self) -> 'numpy.ndarray'|None:
        if self.last_frame is not None:
            logger.info(f'GET FRAME  from: {self.camera_link}')
            return self.last_frame
            
        logger.info(f'Frame is None from: {self.camera_link}')
        return None
        
            
