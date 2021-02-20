## Execution Steps:
1. Create `.env` file like `.env-template` and update it with your values
2. Update `lambda_scraper_cdk/lambda_scraper_cdk_stack` with your needed values (like updating the event role)
3. Create a python environment and install the requirements
4. Run: `cdk deploy`

## Result:
You will find a lambda application created called `lambda_scraper_cdk` with a function created inside and an event trigger.

## Start from scratch:
You can start from scratch through:
1. Create a new directory and run: `cdk init --language` inside it
2. Update your created `app.py`
3. Update your stack class