from unittest import result
import connexion
import six

from flask import abort
from swagger_server.models.recording import Recording
from swagger_server.models.user import User  # noqa: E501
from swagger_server.service import user_service
from swagger_server import util


def add_user(body):  # noqa: E501
    """Add a new user as experiment participant

     # noqa: E501

    :param body: User object that needs to be added as experiment participant.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

    if is_valid(body):
        print("all good")
        result = user_service.add_user(body)
    else:
        abort(400, "Please provide all required attributes.")
    
    return result

def is_valid(user: User):
    """
    Checks all the params whether they are all available or not
    """
    isValid = False
    if user.id and user.gender.recording and user.gender.time_to_recording and user.age.recording and user.age.time_to_recording:
        isValid = True

    return isValid