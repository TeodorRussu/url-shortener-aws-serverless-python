import json
import random
import string

import boto3

from functions.validators.input_validator import validate_url

ddb = boto3.resource('dynamodb')
table = ddb.Table('UrlShortenerTable')

def create_short_url(event, context):
    print(event)
    url = json.loads(event['body'])['url']
    if not validate_url(url):
        return generate_error_response(400, 'Invalid URL')
    id = generate_short_url_id()
    table.put_item(Item={'id': id, 'url': url})

    return generate_success_response(id)


def generate_error_response(code, message):
    return {
        'statusCode': code,
        'body': message
    }


def generate_success_response(id):
    return {
        'statusCode': 201,
        'body': json.dumps({'id': id})
    }


def generate_short_url_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

