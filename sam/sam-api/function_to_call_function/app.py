import json
import boto3
import botocore


# Set "running_locally" flag if you are running the integration test locally
running_locally = True


def lambda_handler(event, context):
    print ('Hello3')
    try:
        if running_locally:
            lambda_client = boto3.client('lambda',
                                    region_name="eu-west-1",
                                    endpoint_url="http://host.docker.internal:3001",
                                    use_ssl=False,
                                    verify=False,
                                    config=botocore.client.Config(signature_version=botocore.UNSIGNED,
                                                    read_timeout=10,
                                                    retries={'max_attempts': 0}))
        else:
            lambda_client = boto3.client('lambda')

        response = lambda_client.invoke(FunctionName="CallByFunction")
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
