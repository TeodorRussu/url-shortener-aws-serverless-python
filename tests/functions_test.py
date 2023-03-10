import json
import os
import pytest
import boto3
from botocore.stub import Stubber




@pytest.fixture
def dynamodb_mock(mocker):
    dynamodb_mock = mocker.MagicMock()
    boto3_mock = mocker.patch("boto3.resource", return_value=dynamodb_mock)
    yield dynamodb_mock
    boto3_mock.stop()


def test_create_short_url(mocker, dynamodb_mock):
    mocker.patch("functions.create.generate_short_url_id", return_value="abcd1234")
    # Set up the test event and context
    event = {"body": "{\"url\": \"https://www.example.com/\"}"}
    context = {}

    # Call the create_short_url function with the test event and context
    from functions.create import create_short_url
    result = create_short_url(event, context)

    # Check the result
    assert result == {"statusCode": 201, "body": '{"id": "abcd1234"}'}
