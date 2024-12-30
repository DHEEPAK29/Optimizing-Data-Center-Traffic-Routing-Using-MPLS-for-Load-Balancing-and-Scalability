from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import Controller
from mininet.link import TCLink

class MPLSDataCenterTopo(Topo):
    def build(self):
        # three data center switches (routers)
        dc1 = self.addSwitch('dc1')
        dc2 = self.addSwitch('dc2')
        dc3 = self.addSwitch('dc3')

        # servers (hosts) connected to each switch
        host1 = self.addHost('h1')
        host2 = self.addHost('h2')
        host3 = self.addHost('h3')

        # Connecting switches and hosts
        self.addLink(dc1, dc2, bw=10)  # Link between switches
        self.addLink(dc2, dc3, bw=10)  # Link between switches
        self.addLink(dc1, host1, bw=10)  # Link to server 1
        self.addLink(dc2, host2, bw=10)  # Link to server 2
        self.addLink(dc3, host3, bw=10)  # Link to server 3

if __name__ == '__main__':
    topo = MPLSDataCenterTopo()
    net = Mininet(topo=topo, controller=Controller, link=TCLink)
    net.start()
    CLI(net)
    net.stop()
