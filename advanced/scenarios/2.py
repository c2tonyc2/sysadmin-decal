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

default_gateway = util.get_default_gateway_linux()
print(default_gateway)

# Kill their default gateway routing rule
# command = "ip route delete default"
# subprocess.run(split(command))
#
# # Add a dummy entry
# command = "ip route add default via "
# iface = util.get_default_iface_name_linux()
