import json
import boto3
import botocore

def lambda_handler(event, context):
    print ('Hello3')
    try:
        lambda_client = boto3.client('lambda',
                                  endpoint_url="http://z2:3001",
                                  use_ssl=False,
                                  verify=False,
                                  config=botocore.client.Config(signature_version=botocore.UNSIGNED,
                                                read_timeout=3,
                                                retries={'max_attempts': 0}))
        response = lambda_client.invoke(FunctionName="HelloWorldFunction")
        lambda_response_body = response['Payload'].read()
        data = json.loads(lambda_response_body)['body']
    except Exception as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": data
    }
