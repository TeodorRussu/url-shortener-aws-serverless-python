import json
import boto3

ddb = boto3.resource('dynamodb')
table = ddb.Table('UrlShortenerTable')

def get_short_url(event, context):
    id = event['pathParameters']['id']
    response = table.get_item(Key={'id': id})
    if 'Item' not in response:
        return {'statusCode': 404}
    print(f'response from db: {response}')
    url = response['Item']['url']
    return {
        'statusCode': 301,
        'headers': {
            'Location': url
        }
    }