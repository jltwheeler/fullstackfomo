from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, AutoScaling
from diagrams.aws.network import Route53, ElbApplicationLoadBalancer

from .utils import create_kwargs


def api(graph_attr: dict = None, path: str = None) -> None:
    name = "NodeJS GraphQL API"
    kwargs = create_kwargs(name, graph_attr, path)

    with Diagram(**kwargs):
        with Cluster("VPC"):
            route53 = Route53("DNS")
            elb = ElbApplicationLoadBalancer("ALB")
            asg = AutoScaling("ASG")

            with Cluster("ECS Tasks"):
                ecs = [ECS("API 1"), ECS("API 2")]

            route53 >> elb >> asg >> ecs