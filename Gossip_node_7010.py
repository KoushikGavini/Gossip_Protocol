# Imports the Gossip_Main class
from Gossip import Gossip_Main

# Node's port
port = 7010
# Connected ports/nodes
nodes_connected = [7000, 7030, 7040]

node = Gossip_Main(port, nodes_connected)