import connexion
import six
from swagger_server.datalayer.db import execute

from swagger_server.models.exercise import Exercise  # noqa: E501
from swagger_server.models.experiment import Experiment  # noqa: E501
from swagger_server import util


def add_experiment(body):  # noqa: E501
    """Add a new experiment to a user

     # noqa: E501

    :param body: Experiment object that needs to be added to a user.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Experiment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_exercise(experiment_id):  # noqa: E501
    """Get next exercise for this specific experiment of this user

     # noqa: E501

    :param experimentId: Experiment ID to retrieve
    :type experimentId: int

    :rtype: Exercise
    """

    sql = "SELECT * FROM Exercise WHERE Number = %s"

    print (str(experiment_id))
    exercises = execute(sql, (experiment_id), "SELECT")
    #return "Hello world " + str(experiment_id) + "!" 
    return exercises
