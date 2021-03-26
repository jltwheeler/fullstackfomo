# FullStackFOMO API

## About the Project

GraphQL API written with `Node.js TypeScript`, bootstrapped using the
[NestJS][nest] backend framework.

Data layer is provided by `DynamoDB`.

### Built With

- [NestJS][nest]
- [GraphQL][graphql]
- [Dynamoose][dynamoose] with the [NestJS Dynamoose][nestjs-dynamoose] plugin.

## Getting Started

To get a local copy up and running, follow these example steps.

### Prerequisites

- `Node.js v14.X` The recommended way to install specific node versions is via
  `Node Version Manager` (`nvm`). Follow the instructions in the [link][nvm]
  to get `nvm` installed on your machine.

  ```sh
  # Check nvm is installed and running
  nvm -v

  # Check node version
  node -v

  # If you need version 14, install v14 and specify as your default node
  nvm install 14
  nvm use 14

  # Check you are running 14
  node -v
  ```

- `npm`

  ```sh
  npm install npm@latest -g
  ```

### Installation

```bash
$ npm install
```

### Running the app

```bash
# development
$ npm run start

# watch mode
$ npm run start:dev

# production mode
$ npm run start:prod
```

> Ensure you run `docker-compose up` from the `./workers` directory to spin up
> the local dynamodb server for development.

### Test

```bash
# unit tests
$ npm run test

# e2e tests
$ npm run test:e2e

# test coverage
$ npm run test:cov
```

<!-- MARKDOWN LINKS -->

[nest]: https://github.com/nestjs/nest
[nvm]: https://github.com/nvm-sh/nvm
[graphql]: https://graphql.org/
[nestjs-dynamoose]: https://github.com/hardyscc/nestjs-dynamoose
[dynamoose]: https://github.com/dynamoose/dynamoose
