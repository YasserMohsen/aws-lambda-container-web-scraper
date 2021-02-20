# aws-lambda-container-web-scraper
This is a blank repository as a template to create an AWS lambda function using a container image I aim to build the needed container image first, then use it to create my lambda function through AWS CDK.
## Components
This project consists of two separated components:
1. `container_image`: used to build a container image using Docker that has the web driver (chrome) installed, and the scraping code. After building the image, push it on an AWS ECR repository. 
2. `lambda_scraper_cdk`: An AWS CDK project that is used to create a stack of connected components on an AWS project:
  - IAM Roles
  - Lambda function from a container image (on an AWS ECR repository)
  - Event role to trigger the function