from shlex import split
import lib.util as util
import subprocess

"""
Scenario Overview:
Place a bad entry in their routing table for the default gateway and route
traffic to a black hole.

Triage:
They should be using "ip route" or a similar command to display their routing
table and from information they gathered before running the scenarios, they
should deduce that the entry for the default gateway is bad.

Solution:
Delete the malicious entry and re add a entry to the proper default gateway i.e.
"ip route add default via 10.0.2.2"
"""
# Memorize their current default gateway
routing_info = util.get_default_routing_information()

# Construct new bogus gateway
gateway_bytes = routing_info.gateway.split(".")

last_byte = int(gateway_bytes[-1])
if last_byte < 250:
    last_byte += 5
else:
    last_byte -= 5
gateway_bytes[-1] = str(last_byte)
 
new_gateway = ".".join(gateway_bytes)

# Kill their default gateway routing rule
command = "ip route delete default"
subprocess.run(split(command))

# Add a dummy entry
command = "ip route add default via {gateway}".format(gateway=new_gateway)
subprocess.run(split(command))
