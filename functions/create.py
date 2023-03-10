import json
import boto3
import string
import random

ddb = boto3.resource('dynamodb')
table = ddb.Table('UrlShortenerTable')

def create_short_url(event, context):
    url = json.loads(event['body'])['url']
    id = generate_short_url_id()
    table.put_item(Item={'id': id, 'url': url})
    response = {
        'statusCode': 201,
        'body': json.dumps({'id': id})
    }
    return response


def generate_short_url_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))