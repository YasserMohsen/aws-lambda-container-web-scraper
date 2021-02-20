from aws_cdk import (
    aws_events as events,
    aws_lambda as lambdas,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_ecr as ecr,
    core
)


class LambdaScraperCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, repo_name: str, repo_tag: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. Roles & Policies

        role = iam.Role(
            self, 'myappRole',
            assumed_by= iam.ServicePrincipal('lambda.amazonaws.com'))

        role.add_to_policy(iam.PolicyStatement(
            effect = iam.Effect.ALLOW,
            resources = ["*"],
            actions= ['events:*']))

        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["arn:aws:iam::*:role/AWS_Events_Invoke_Targets"],
            actions=['iam:PassRole']))

        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"]))

        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=["s3:*"]))

        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=["lambda:*"]))

        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=["sns:*"]))

        # 2. Lambda functions

        repo = ecr.Repository.from_repository_name(self, "Repository", repository_name=f"{repo_name}")
        lambdaFn1 = lambdas.DockerImageFunction(
            self, "lambda_scraper_cdk_func_1",
            code=lambdas.DockerImageCode.from_ecr(
                repository=repo,
                tag=repo_tag
            ),
            timeout=core.Duration.seconds(600),
            memory_size=2048,
            environment=dict(PATH="/opt"),
            role = role
        )

        # rule1 = events.Rule(
        #     self, "Rule",
        #     schedule=events.Schedule.cron(
        #         minute='*',
        #         hour='*/4',
        #         month='*',
        #         week_day='*',
        #         year='*'),
        # )
        # rule1.add_target(targets.LambdaFunction(lambdaFn1))
