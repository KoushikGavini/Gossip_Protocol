# import the Gossip_Main class
from Gossip import Gossip_Main

# Node port
port = 8000
# Connected node/port
# connected_nodes = [7090, 8010]
nodes_connected = [7080]
node = Gossip_Main(port, nodes_connected)