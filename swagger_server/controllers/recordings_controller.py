import connexion
import six

from swagger_server.models.recording import Recording  # noqa: E501
from swagger_server import util


def add_recording(body):  # noqa: E501
    """Add a new recording to a experiment exercise

     # noqa: E501

    :param body: Recording object that needs to be added to a experiment exercise.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Recording.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
