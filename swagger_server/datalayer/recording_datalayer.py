from swagger_server.models.recording import Recording
from swagger_server.datalayer.db import execute


def store_recording(recording: Recording):
    """
    Handle all logic to store a recoring into the data storage.
    """
    sql = "INSERT INTO Recording (TimeToRecording, Recording) VALUES (%s, %s)"

    inserted_user = execute(sql, (recording.time_to_recording, recording.recording), "INSERT")
    
    return inserted_user