# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.exercise import Exercise  # noqa: E501
from swagger_server.models.experiment import Experiment  # noqa: E501
from swagger_server.test import BaseTestCase


class TestExperimentsController(BaseTestCase):
    """ExperimentsController integration test stubs"""

    def test_add_experiment(self):
        """Test case for add_experiment

        Add a new experiment to a user
        """
        body = Experiment()
        response = self.client.open(
            '/v1/experiments',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_exercise(self):
        """Test case for get_exercise

        Get next exercise for this specific experiment of this user
        """
        response = self.client.open(
            '/v1/experiments/{experimentId}/exercises/next'.format(experimentId=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
