import json
import requests
# import ptvsd

# # Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
# ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
# ptvsd.wait_for_attach()

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print("Hello1")
    content = {}
    content['body'] = -1
    try:
        ip = requests.get("http://checkip.amazonaws.com/")
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
            "message": "hello world",
            "location": ip.text.replace("\n", ""),
            "body": content['body']
        }),

    }
