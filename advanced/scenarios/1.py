from shlex import split
import lib.util as util
import subprocess

command = "ip link set dev {iface} {status}"
iface = util.get_default_iface_name_linux()

args = split(command.format(iface=iface, status="down"))

print(args)

