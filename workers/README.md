# FullStackFOMO Workers

## About the Project

This sub repo contains the async `Python3` lambda functions that are invoked as
serverless cron jobs in AWS. These `'worker'` functions are responsible for
building the platform database and `AWS ElasticSearch` cluster index data.

Initially `Node.js Typescript` was used, however there is currently [no support][sls-offline-bug]
for using `Node 14.X` runtimes with the `serverless-offline` plugin. This made
it difficult to test the workers locally, therefore I changed to `Python3`.

> Although I can still use the `sls invoke local` command, I found this a bit
> slow and annoying compared to making a local dev server you can hit with REST
> calls using `postman`

### Built With

This project has been generated using the `aws-python3` template from
the [Serverless framework][sls-framework]. For detailed instructions, please
refer to the [documentation][sls-aws-docs].

## Getting Started

The local dev environment is a bit odd. In order to easily invoke and test the
cron functions, `Docker` is used to serve the functions via a local **REST API**
using [serverless-offline][sls-offline] and a local **DynamoDB** instance.

To get a local copy up and running, follow these example steps

### Prerequisites

- `Docker` and `docker-compose` follow [this link][get-docker]

### Local Dev Environment

- Run `docker-compose up` to start the local dev environment. Code is volume
  mounted into the container, and `nodemon` allows for hot reloading of local
  server code. This also starts the local `DynamoDB` instance.
- Test functions by hitting the `GET` endpoints using `curl` or `postman`.
- If you want to run Python tests, linting etc. locally,
  it is recommended to setup a `venv`:

  ```sh
  # Create venv
  python3 -m venv venv
  source venv/bin/activate

  # Install dependencies
  pip install -r requirements.txt
  pip install -r requirements-dev.txt

  # Run tests and lint
  pytest tests/
  find . -path ./venv -prune -false -o -type f -name "*.py" | xargs pylint
  ```

  However all this is done in the `GitHub CI/CD workflow` anyyway.

<!-- MARKDOWN LINKS -->

[sls-framework]: https://www.serverless.com/
[sls-aws-docs]: https://www.serverless.com/framework/docs/providers/aws/
[sls-offline]: https://github.com/dherault/serverless-offline
[sls-offline-bug]: https://github.com/dherault/serverless-offline/issues/1187
[get-docker]: https://docs.docker.com/get-docker/
