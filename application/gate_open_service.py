import time
import threading
from application.ports.inbound.gate_oppener import GateOppener
from common.singleton import SingletonMeta


class GateOpenService(metaclass=SingletonMeta):
    
    def __init__(self, system_idle_time: int, gate_oppener: GateOppener) -> None:
        self.is_gate_opening = False
        self.last_open = 0
        self.system_idle_time = system_idle_time
        self.gate_oppener = gate_oppener
        self.lock = threading.Lock()

    def open_gate(self):
        with self.lock:
            self.last_open = time.time()
            self.gate_oppener.open_gate()


    def is_idle_time(self) -> bool:
        return time.time() - self.last_open <= self.system_idle_time