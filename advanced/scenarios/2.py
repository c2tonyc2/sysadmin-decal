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
routing_entries = util.get_default_routing_information()
default_entry = next((e for e in routing_entries if util.is_default_gateway(e)), None)
default_iface_entry = next(
    (e for e in routing_entries if not util.is_default_gateway(e) and e.iface == default_entry.iface), 
    None
)

# Kill their default gateway routing rule
command = "ip route delete default"
subprocess.run(split(command))

# Add a dummy entry
command = "ip route add default via {gateway}".format(
    gateway=util.get_iface_ip_address(default_iface_entry.iface)
)

subprocess.run(split(command))
