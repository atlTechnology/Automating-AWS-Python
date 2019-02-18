import boto3
import click

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_bucket():
    "List all s3 bucket"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-buckets-object')
@click.argument('bucket')
def list_bucket_objects(bucket):
    "List objects in a s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)

if __name__ == '__main__':
    cli()