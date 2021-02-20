## Execution Steps:
1. Update your code in `code/`
2. Build a docker image
```
docker build -t lambda-chrome-scraper:latest .
```
3. Test the image by running
```
docker run -p 9000:8080 lambda-chrome-scraper:latest
```
4. Invoke a test function using
```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

## Push to AWS ECR:
1. Authenticate to AWS ECR
```
aws ecr get-login-password --region ${YOUR_REGION} | docker login --username AWS --password-stdin ${YOUR_ACCOUNT_ID}.dkr.ecr.${YOUR_REGION}.amazonaws.com
```
2. Create an AWS ECR repo
```
aws ecr create-repository --repository-name aws-lambda-chrome-scraper-test --region ${YOUR_REGION}
```
3. Tag your local image
```
docker tag lambda-chrome-scraper:latest ${YOUR_ACCOUNT_ID}.dkr.ecr.${YOUR_REGION}.amazonaws.com/lambda-chrome-scraper:v1.0
```
4. Push your image to the remote repo
```
docker push ${YOUR_ACCOUNT_ID}.dkr.ecr.${YOUR_REGION}.amazonaws.com/lambda-chrome-scraper:latest
```