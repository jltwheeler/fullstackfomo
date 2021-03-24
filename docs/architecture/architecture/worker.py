from diagrams import Diagram, Cluster
from diagrams.aws.analytics import ElasticsearchService
from diagrams.aws.compute import Lambda
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SimpleQueueServiceSqs
from diagrams.aws.management import CloudwatchEventTimeBased
from diagrams.saas.social import Twitter

from .utils import create_kwargs


def worker(graph_attr=None, path=None) -> None:
    name = "Data retrieval worker"
    kwargs = create_kwargs(name, graph_attr, path)

    with Diagram(**kwargs):
        source = Twitter("Data source")
        event = CloudwatchEventTimeBased("CloudWatch (1 min)")
        _lambda = Lambda("Python lambdas")
        dynamodb = Dynamodb("DynamoDB")
        sqs = SimpleQueueServiceSqs("SQS")
        es = ElasticsearchService("ElasticSearch")

        source >> event >> sqs >> _lambda >> dynamodb >> es
