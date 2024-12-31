                    # Install Mininet and Ryu
                    sudo apt-get install mininet
                    pip install ryu




                sudo python mpls_dc_network.py




                                sudo python mpls_dc_network.py



                                                # Start iperf on Host 1
                h1 iperf -s

                # Start iperf on Host 2
                h2 iperf -c 10.0.0.1 -t 30  # Traffic from Host 2 to Host 1
