import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('ssm')
    parameter = client.get_parameter(Name='parameter-example-Lambda', WithDecryption=True)
    print(parameter)
    return parameter ['Parameter']['Value']
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
