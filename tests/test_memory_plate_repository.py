import pytest
from adapters.outbound.memory_plate_number_repository import MemoryPlateNumberRepository

@pytest.fixture
def plate_repo():
    return MemoryPlateNumberRepository()

@pytest.fixture
def clear_all(plate_repo):
    plate_repo.clear_all()



def test_update_plate_number(plate_repo):
    plate_numbers = ['ABC123', 'XYZ789', 'DEF456']
    plate_repo.update_plate_number(plate_numbers)
    assert plate_repo.get_all_plate_number() == plate_numbers
