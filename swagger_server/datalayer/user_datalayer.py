from swagger_server.models.user import User
from swagger_server.datalayer.db import execute


def store_user(user: User):
    """
    Handle all logic to store a user into the data storage.
    """
    sql = "INSERT INTO User (ID, UniParkID, GenderRecordingFK, AgeRecordingFK) VALUES (%s, %s, %s, %s)"

    inserted_user = execute(sql, (user.id, user.id, user.gender.id, user.age.id), "INSERT")
    
    return inserted_user