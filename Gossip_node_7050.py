from Gossip import GossipNode

# port for this node
port = 7050
# ports for the nodes connected to this node
# connected_nodes = [7040, 7060]
connected_nodes = [7040, 7070, 7080]

node = GossipNode(port, connected_nodes)