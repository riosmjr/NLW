from .check_ins_repository import CheckInsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

def test_inser_check_in():
    attendee_id = 'uuid-attendees'
    check_ins_repository = CheckInsRepository()
    response = check_ins_repository.inser_check_in(attendee_id)
    print(response)