from shlex import split
import lib.util as util
import subprocess

"""
Scenario Overview:
Poison the user's arp cache redirecting traffic intended for the default gateway to instead go to an invalid MAC.

Triage:
The student should identify the issue by inspecting the machine's arp table via a tool like "arp".  They should note that the MAC that corresponds to their default gateway is set to an invalid MAC.

Solution:
Delete the malicious entry and re add a proper entry to the gateway's MAC address.  
They should have taken note of proper configuration info prior to tanking their system.
The entry should be added using a command like "sudo arp -s <ip_address <MAC_address>" 
Conflicts with existing entries may exist, in that case, the student should remove conflicting entries with "sudo arp -d <ip_address>"
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
