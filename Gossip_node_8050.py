# import the Gossip_Main class
from Gossip import GossipNode

# Node port
port = 8050
# Connected nodes/ports
# connected_nodes = [8040]
nodes_connected = [8040]
node = GossipNode(port, nodes_connected)