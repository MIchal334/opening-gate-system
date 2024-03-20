from abc import ABC, abstractmethod
from typing import List


class PlateNumberRepository(ABC):
    
    @abstractmethod
    def get_all_plate_number(self) -> List[str]:
        pass

    @abstractmethod
    def update_plate_number(self,plate_number_list: List[str]) -> None:
        pass    
    