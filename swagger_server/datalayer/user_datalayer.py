from swagger_server.models.user import User
from swagger_server.datalayer.db import execute
import base64

def store_user(user: User):
    """
    Handle all logic to store a user into the data storage.
    """

    # write base64 string to mp3 file
    """mp3_gender_data = base64.b64decode(user.gender.recording)
    newFileGender = open("gender.mp3", "wb")
    newFileGender.write(mp3_gender_data)
    mp3_age_data = base64.b64decode(user.age.recording)
    newFileAge = open("age.mp3", "wb")
    newFileAge.write(mp3_age_data)"""

    # INSERT Statement for the insertion of a User.
    sql = "INSERT INTO User (ID, UniParkID, GenderRecordingFK, AgeRecordingFK) VALUES (%s, %s, %s, %s)"

    inserted_user = execute(sql, (user.id, user.id, user.gender.id, user.age.id), "INSERT")
    
    return inserted_user