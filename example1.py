from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Envoy
from diagrams.onprem.queue import Kafka
from diagrams.onprem.client import User

with Diagram(name="Example", show=False):
    with Cluster("Back End"):
        services = [Server("service1"), Server("service2"), Server("service3")]

    with Cluster("Front End"):
        gateway = Envoy("HTTP/2 SSE\n/events?userId=...")
        user = User("frontend")
        frontend = [gateway, user]
        gateway << Edge(style="dotted") >> user
    services >> Kafka() >> gateway
