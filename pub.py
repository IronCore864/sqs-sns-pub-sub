import boto3

sns = boto3.client('sns')

response = sns.publish(
    TopicArn='arn:aws:sns:eu-central-1:297122103751:test',
    Message='Hello World!',
)

print(response)
