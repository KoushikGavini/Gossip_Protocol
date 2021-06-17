# import the Gossip_Main class
from Gossip import GossipNode

# Node port
port = 8000
# Connected node/port
# connected_nodes = [7090, 8010]
nodes_connected = [7080]
node = GossipNode(port, nodes_connected)