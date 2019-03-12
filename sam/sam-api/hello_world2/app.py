import json
import requests

def lambda_handler(event, context):
    print("Hello2")
    content = {}
    content['body'] = -1
    try:
        sam_get = requests.get("http://z2:3000/hello1")
        content = sam_get.json()
        print(content['body'])
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world 2",
            "body": content['body']
        }),
    }
