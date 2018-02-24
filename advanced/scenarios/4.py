from shlex import split
import lib.util as util
import subprocess

"""
Scenario Overview:
We will be simulating spoofed DNS responses using dnsmasq, a tool that will let us run a nameserver on our local machine.  Once the nameserver is up, we will configure certain hostnames to point to a blackhole server.  Additionally, we will edit /etc/resolv.conf to prioritize the local nameserver when it comes to resolving hostnames via lookup tools like dig.

Triage:
The student should use a lookup tool like dig to verify that they are receiving DNS responses for their queries.  However, since these entries are spoofed the bindings are bogus.
They should cross validate this result -- one good way to do this is to have the lookup tool use an alternative nameserver to issue the same query and notice that connections to this IP are valid.  Another option is to perform a reverse DNS lookup via another DNS server.  The key here is that you need to cross validate the IP in the DNS response in order to confirm that it's invalid.

Solution:
Since the current DNS server has a malicious record there are multiple ways to solve this issue.  One can place a static entry in /etc/hosts if the IP of the destination in question doesn't change.  Additionally, you can modify the default DNS server to be something more 'trustworthy', Google DNS at 8.8.8.8 for example.  This can be done by adding an entry in /etc/resolv.conf, mind the order of the entry since this affects its priority.
"""
HOSTS_FILE = "/etc/hosts"
ENTRY = "72.66.115.13 google.com\n"

# Edit their hosts file to contain a bad entry
with open(HOSTS_FILE, "a") as host_file:
    host_file.write(ENTRY)

