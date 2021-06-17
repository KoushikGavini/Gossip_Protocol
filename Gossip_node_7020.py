# import the Gossip_Main class
from Gossip import Gossip_Main

# Node's port
port = 7020
# Connected ports/nodes
nodes_connected = [7000]

node = Gossip_Main(port, nodes_connected)