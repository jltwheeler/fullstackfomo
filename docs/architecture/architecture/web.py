from diagrams import Diagram
from diagrams.aws.network import Route53, CloudFront
from diagrams.aws.storage import SimpleStorageServiceS3
from diagrams.onprem.client import Users

from .utils import create_kwargs


def web(graph_attr=None, path=None) -> None:
    name = "Static Hosted React Web Application"
    kwargs = create_kwargs(name, graph_attr, path)

    with Diagram(**kwargs):
        users = Users("Users")
        route53 = Route53("Route 53")
        cloudfront = CloudFront("CloudFront")
        s3 = SimpleStorageServiceS3("S3 - index.html \n with React.js app")

        users >> route53 >> cloudfront >> s3
