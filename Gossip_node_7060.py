# import the Gossip_Main class
from Gossip import Gossip_Main

# Node's port
port = 7060
# Connected ports/nodes
# connected_nodes = [7050, 7070]
nodes_connected = [7040]

node = Gossip_Main(port, nodes_connected)