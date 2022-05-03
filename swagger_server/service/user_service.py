from flask import current_app
from swagger_server.datalayer.recording_datalayer import store_recording
from swagger_server.models.user import User
from swagger_server.datalayer.user_datalayer import store_user

def add_user(user: User):
    """
    checks all parameters and adds user to the storage
    """
    # before storing the user both recordings (age and gender) have to be saved
    age_id = store_recording(user.age)
    gender_id = store_recording(user.gender)
    user.age.id = age_id
    user.gender.id = gender_id

    # after both recordings have been stored, the user itself can be stored with the corresponding foreign keys.
    result = store_user(user)
    return result