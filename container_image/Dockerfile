FROM public.ecr.aws/lambda/python:3.6

# OS libraries
RUN yum update -y
RUN yum install -y \
    gcc \
    gtk3 \
    wget \
    unzip
RUN yum -y clean all

# Install chrome driver and browser
WORKDIR /bin
# RUN wget https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip
RUN wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
# RUN curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-57/stable-headless-chromium-amazonlinux-2.zip > headless-chromium.zip
RUN wget https://github.com/adieuadieu/serverless-chrome/releases/\
download/v1.0.0-53/stable-headless-chromium-amazonlinux-2017-03.zip
RUN unzip stable-headless-chromium-amazonlinux-2017-03.zip
RUN rm *.zip

RUN chmod 755 /bin/chromedriver

WORKDIR ${LAMBDA_TASK_ROOT}

# Install requirements
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install awslambdaric
RUN pip install -r requirements.txt

# Handler function
COPY code/ .

CMD [ "index.lambda_handler" ]