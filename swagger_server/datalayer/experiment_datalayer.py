import random
from swagger_server.datalayer.db import execute
from swagger_server.models.experiment import Experiment

def store_experiment(experiment: Experiment):
    """
    Store experiment with the information into the database
    """
    sql = "INSERT INTO Experiment (UserFK, Start) VALUES (%s, %s)"

    experiment_id = execute(sql, (experiment.user, experiment.start), "INSERT")
    
    return experiment_id

def store_experiment_exercises(exercises, experiment: Experiment):
    """
    Stores all experiment exercises into the database
    """
    # sql statement to insert multi rows
    sql = "INSERT INTO ExperimentExercise (ExperimentFK, ExerciseFK) VALUES (%s, %s)"

    # create list with the experiment id and the exercise id to insert into the database
    experiment_exercises = list([(experiment.id, e["PK"]) for e in exercises])
    random.shuffle(experiment_exercises)
    
    # execute the INSERT MANY statement
    execute(sql, (experiment_exercises), "INSERT MANY")

    return True

def load_user_experiment(experiment_id: int, user_id: int):
    """
    Loads a specific experiment for a specific user
    """
    # sql statement for the experiment load
    sql = "SELECT * FROM Experiment WHERE PK = %s AND UserFK = %s"

    # execute sql statement
    result = execute(sql, (experiment_id, user_id), "SELECT")

    if not result:
        return None

    return result