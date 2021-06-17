# import the Gossip_Main class
from Gossip import Gossip_Main

# Node Port
port = 8010
# Nodes Connected/Port
# connected_nodes = [8000, 8020]
nodes_connected = [7090]
node = Gossip_Main(port, nodes_connected)