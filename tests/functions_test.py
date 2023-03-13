import json

import pytest


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


def test_generate_error_response(dynamodb_mock):
    from functions.create import generate_error_response
    # Test 1: Verify response for HTTP status code 404
    code = 400
    message = 'Invalid URL'
    expected_response = {
        'statusCode': 400,
        'body': 'Invalid URL'
    }
    assert generate_error_response(code, message) == expected_response

    # Test 2: Verify response for HTTP status code 500
    code = 500
    message = 'Internal Server Error'

    expected_response = {
        'statusCode': 500,
        'body': 'Internal Server Error'
    }
    assert generate_error_response(code, message) == expected_response


def test_generate_success_response(dynamodb_mock):
    id = 123
    expected_response = {
        'statusCode': 201,
        'body': json.dumps({'id': 123})
    }
    from functions.create import generate_success_response
    assert generate_success_response(id) == expected_response
