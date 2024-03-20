from application.ports.outbound import PlateNumberRepository

class MemoryPlateNumberRepository(PlateNumberRepository):
    
    def __init__(self):
        self.plate_list = []
    
    def get_all_plate_number(self) -> list[str]:
        return self.plate_list

    def update_plate_number(self,plate_number_list: list[str]) -> None:
        self.plate_list.clear()
        self.plate_list.extend(plate_number_list)