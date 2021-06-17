# import the Gossip_Main class
from Gossip import Gossip_Main

# Node port
port = 8050
# Connected nodes/ports
# connected_nodes = [8040]
nodes_connected = [8030]
node = Gossip_Main(port, nodes_connected)