import random
import socket
from threading import Thread
import time


class Gossip_Main:
    # Array holds infected nodes
    nodes_infected = []

    """Init method passes the port of the node and the ports of the nodes 
    which has a connection to it
    """
    def __init__(self, port, connected_nodes):

        # Creates a socket instance and utilizes SOCK_DGRAM to transmit data 
        self.node = socket.socket(type=socket.SOCK_DGRAM)

        # Sets the address with hostname and port
        self.hostname = socket.gethostname()
        self.port = port

        # Binds the address to the socket which was just created
        self.node.bind((self.hostname, self.port))

        # Sets the ports of the nodes connected as susceptible nodes
        self.nodes_susceptible = connected_nodes

        print("Node started on port {0}".format(self.port))
        print("Susceptible nodes are", self.nodes_susceptible)

        self.start_threads()

    def input_message(self):
        while True:
            # Desired message that is going to sent to all nodes
            desired_message = input("Enter a message so it can sent to all nodes:\n")

            # Calls send message method and passes the input message with encoding message into ascii.
            self.submit_message(desired_message.encode('ascii'))

    def get_messages(self):
        while True:
            # Uses 'recvfrom' to receive UDP messages
            forward_message, address = self.node.recvfrom(1024)

            # removes the node/port of the sent node
            # from the list of susceptible nodes and
            # appends it to the list of infected nodes
            self.nodes_susceptible.remove(address[1])
            Gossip_Main.nodes_infected.append(address[1])

            # Sleeps for 3 seconds so time difference can be shown
            time.sleep(3)

            # Prints current time and decodes message
            print("\nMessage: '{0}'.\nReceived [{1}] from [{2}]\n"
                  .format(forward_message.decode('ascii'), time.ctime(time.time()), address[1]))

            # Calls send message to forward the message to other connected/suspectiable nodes
            self.submit_message(forward_message)

    def submit_message(self, message):
        while self.nodes_susceptible:
            # Utilizes random gossip distribution methodology
            port_selected = random.choice(self.nodes_susceptible)

            print("\n")
            print("-"*50)
            print("Susceptible nodes =>", self.nodes_susceptible)
            print("Infected nodes =>", Gossip_Main.nodes_infected)
            print("Port [{0}]".format(port_selected))

            # Uses 'sendto' inorder transmit the UDP message by connectionless protocol 
            self.node.sendto(message, (self.hostname, port_selected))

            # Removes destination node from the list of susceptible nodes then appends it to list of infected nodes
            self.nodes_susceptible.remove(port_selected)
            Gossip_Main.nodes_infected.append(port_selected)

            print("Message: '{0}' sent to [{1}].".format(message.decode('ascii'), port_selected))
            print("Susceptible nodes =>", self.nodes_susceptible)
            print("Infected nodes =>", Gossip_Main.infected_nodes)
            print("-"*50)
            time.sleep(2)
            print("\n")

    def threads(self):
        # Sets two threads for entering and getting a message. 
        # Enables node to send message and recieve message
    
        Thread(target=self.input_message).start()
        Thread(target=self.get_messages).start()