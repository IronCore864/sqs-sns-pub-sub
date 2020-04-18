import boto3
from botocore.exceptions import ClientError


def retrieve_sqs_messages(sqs_queue_url):
    sqs_client = boto3.client('sqs')
    try:
        msgs = sqs_client.receive_message(QueueUrl=sqs_queue_url,
                                          MaxNumberOfMessages=1,
                                          WaitTimeSeconds=0,
                                          VisibilityTimeout=5)
    except ClientError as e:
        print(e)
        return None
    return msgs['Messages']


def main():
    sqs_queue_url = 'https://sqs.eu-central-1.amazonaws.com/297122103751/test'

    msgs = retrieve_sqs_messages(sqs_queue_url)
    if msgs is not None:
        for msg in msgs:
            print(f'SQS: Message ID: {msg["MessageId"]}, 'f'Contents: {msg["Body"]}')


if __name__ == '__main__':
    main()
