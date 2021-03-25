FROM node:14.15.4-alpine3.11

# Install Python3 in alpine linux image
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache --upgrade pip setuptools && \
    pip install -r requirements.txt

RUN npm i -g serverless serverless-offline nodemon

COPY . /app

EXPOSE 3000

CMD [ "nodemon", "-e", "py", "--exec", "sls", "offline", "-c", "serverless.dev.yml", "start", "--host", "0.0.0.0", "--httpPort", "3000" ]