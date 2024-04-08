from application.ports.outbound.plate_data_repo import PlateNumberRepository
from adapters.outbound.memory_plate_number_repository import MemoryPlateNumberRepository


def get_plate_repository() -> PlateNumberRepository:
    return MemoryPlateNumberRepository()