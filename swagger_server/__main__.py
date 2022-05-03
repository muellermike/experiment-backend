#!/usr/bin/env python3

import connexion
from flask_cors import CORS
from swagger_server import encoder
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join("swagger_server/.ini")))


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.app.config['DB_URI'] = config['PROD']['DB_URI']
    app.app.config['DB_USER'] = config['PROD']['DB_USER']
    app.app.config['DB_PW'] = config['PROD']['DB_PW']
    app.app.config['DB_NAME'] = config['PROD']['DB_NAME']
    app.app.config['API_KEY'] = config['PROD']['API_KEY']
    app.app.config['API_VALUE'] = config['PROD']['API_VALUE']
    app.add_api('swagger.yaml', arguments={'title': 'NLP Experiment API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
