from application.ports.outbound.plate_data_repo import PlateNumberRepository
from typing import List

class MemoryPlateNumberRepository(PlateNumberRepository):
    
    def __init__(self):
        self.plate_list = []
    
    def get_all_plate_number(self) -> List[str]:
        return self.plate_list

    def update_plate_number(self,plate_number_list: List[str]) -> None:
        self.clear_all()
        self.plate_list.extend(plate_number_list)

    def clear_all(self) -> None:
        self.plate_list.clear()