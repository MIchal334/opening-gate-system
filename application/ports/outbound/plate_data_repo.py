from abc import ABC, abstractmethod

class PlateNumberRepository(ABC):
    
    @abstractmethod
    def get_all_plate_number(self) -> list[str]:
        pass

    @abstractmethod
    def update_plate_number(self,plate_number_list: list[str]) -> None:
        pass    
    