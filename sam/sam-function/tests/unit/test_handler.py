import json
import unittest

from call_by_sns import app

def sns_event():
    """ Generates SNS Event"""

    return {
    "Records": [
      {
        "EventSource": "aws:sns",
        "EventVersion": "1.0",
        "EventSubscriptionArn": "arn:aws:sns:us-east-1::SNSTopic",
        "Sns": {
          "Type": "Notification",
          "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
          "TopicArn": "arn:aws:sns:us-east-1:123456789012:SNSTopic",
          "Subject": "example subject",
          "Message": "Hello from SNS",
          "Timestamp": "1970-01-01T00:00:00.000Z",
          "SignatureVersion": "1",
          "Signature": "EXAMPLE",
          "SigningCertUrl": "EXAMPLE",
          "UnsubscribeUrl": "EXAMPLE",
          "MessageAttributes": {
            "Test": {
              "Type": "String",
              "Value": "TestString"
            },
            "TestBinary": {
              "Type": "Binary",
              "Value": "TestBinary"
            }
          }
        }
      }
    ]
  }

class HelloSNS(unittest.TestCase):

    def test_lambda_handler_valid_sns_returns_200(self):
        event = sns_event()
        ret = app.lambda_handler(event, "")

        assert ret["statusCode"] == 200

    def test_lambda_handler_valid_sns_has_message(self):
        event = sns_event()
        ret = app.lambda_handler(event, "")

        assert "message" in ret["body"]

    def test_lambda_handler_valid_sns_has_message_from_event(self):
        event = sns_event()
        ret = app.lambda_handler(event, "")
        data = json.loads(ret["body"])

        assert "message" in ret["body"]
        assert data["message"] == "Hello from SNS"
