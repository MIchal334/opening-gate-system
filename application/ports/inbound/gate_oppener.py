from abc import ABC, abstractmethod

class GateOppener(ABC):

    @abstractmethod
    def open_gate(self) -> None:
        pass