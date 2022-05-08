from typing import List
from flask import current_app
"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_api_key(api_key, required_scopes):
    return {current_app.config["API_KEY"]: current_app.config["API_VALUE"]}
