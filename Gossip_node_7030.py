# import the Gossip_Main class
from Gossip import Gossip_Main

# Node's port
port = 7030
# Connected ports/nodes
nodes_connected = [7010]

node = Gossip_Main(port, nodes_connected)