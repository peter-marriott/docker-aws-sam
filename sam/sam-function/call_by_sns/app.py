import json


def lambda_handler(event, context):

    message = event['Records'][0]['Sns']['Message']

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": message
        }),
    }
