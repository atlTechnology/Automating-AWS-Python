#!/usr/bin/pythonAutomation
# -*- coding: utf-8 -*-

"""Webotron: Deploy websites with AWS.

Webotron automates the process of deploying static websites
- Configure AWS s3 buckets
    - Create them
    - Set them up
    - Deploy local files  to them
- Configure DNS with AWS Route 53
- Configure a Content delivery Network and SSL with AWS
"""


import boto3
import click

from bucket import BucketManager


session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)
#s3 = session.resource('s3')


@click.group()
def cli():
    """Webotron deploys websites to AWS."""
    pass


@cli.command('list-buckets')
def list_bucket():
    """List all s3 bucket."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-buckets-object')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in a s3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to BUCKET."""
    bucket_manager.sync(pathname, bucket)


if __name__ == '__main__':
    cli()
