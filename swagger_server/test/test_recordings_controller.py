# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.recording import Recording  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRecordingsController(BaseTestCase):
    """RecordingsController integration test stubs"""

    def test_add_recording(self):
        """Test case for add_recording

        Add a new recording to a experiment exercise
        """
        body = Recording()
        response = self.client.open(
            '/v1/recordings',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
