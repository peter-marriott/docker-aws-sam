import json
import requests

def lambda_handler(event, context):
    try:
        docker_get = requests.get("http://host.docker.internal:5000/3")
        content = docker_get.json()
        print(content['body'])
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "thank you docker",
            "body": content['body']
        }),
    }
