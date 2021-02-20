#!/usr/bin/env python3

from aws_cdk import core
from lambda_scraper_cdk.lambda_scraper_cdk_stack import LambdaScraperCdkStack

import os
from dotenv import load_dotenv

load_dotenv()

app = core.App()

account_id = os.getenv("ACCOUNT_ID")
region = os.getenv("REGION")
AWS_ENV = core.Environment(
    account=account_id, 
    region=region
)
ecr_repo_name = os.getenv("ECR_REPO_NAME")
ecr_repo_tag = os.getenv("ECR_REPO_TAG")
# repo = f'{account_id}.dkr.ecr.{region}.amazonaws.com/{ecr_repo_name}'
LambdaScraperCdkStack(
    app, 
    "lambda-scraper-cdk", 
    env=AWS_ENV, 
    repo_name=ecr_repo_name,
    repo_tag=ecr_repo_tag
)

app.synth()
