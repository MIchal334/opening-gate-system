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
        self.capturer = cv2.VideoCapture(p_camera_link)
        self.frames = []
        self.DELAY_SECONDS = 250
        self.last_time = int(1000*time.time())

    def get_frame(self) -> 'numpy.ndarray'|None:
        ret, frame = self.capturer.read()

        if frame is not None:
            logger.info(f'Frame is not None from: {self.camera_link}')
            self.frames.append(frame)
            # return self.frames[-1]
            print(f'DIFFEENCE {int(1000*time.time()) - self.last_time }')
            if int(1000*time.time()) - self.last_time > self.DELAY_SECONDS :
                logger.info('GET FRAME FORM INDOOR FAKE')
                self.last_time = int(1000*time.time())
                return self.frames[-1]
        
        logger.debug(f'Frame is None from: {self.camera_link}')
        return None
        
            
