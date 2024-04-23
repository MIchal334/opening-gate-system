import time
import threading
from common.singleton import SingletonMeta


class GateOpenService(metaclass=SingletonMeta):
    
    def __init__(self,syste_idle_time) -> None:
        self.is_gate_opening = False
        self.last_open = 0
        self.syste_idle_time = syste_idle_time
        self.lock = threading.Lock()

    def open_gate(self):
        with self.lock:
            pass

    def is_idle_time(self) -> bool:
        return time.time() - self.last_open <= self.syste_idle_time