from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# function which checks whether it's a new client or not
try:
    # auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    cluster = Cluster(["10.240.0.70"], port="9042")
    session = cluster.connect("test")
    print(session)
except:
    print("failerd")
