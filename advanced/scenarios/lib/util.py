import socket, struct
from collections import namedtuple
ROUTE = "/proc/net/route"

DefaultRouting = namedtuple('DefaultRouting', ['iface', 'gateway', 'mask'])

def get_default_routing_information():
    with open(ROUTE) as route_file:
        for line in route_file:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue

            return DefaultRouting(
                iface=fields[0],
                gateway=socket.inet_ntoa(struct.pack("<L", int(fields[2], 16))),
                mask=socket.inet_ntoa(struct.pack("<L", int(fields[7], 16)))
            )

# def get_default_iface_name_linux():
#     with open(ROUTE) as f:
#         for line in f.readlines():
#             try:
#                 iface, dest, _, flags, _, _, _, _, _, _, _, =  line.strip().split()
#                 if dest != '00000000' or not int(flags, 16) & 2:
#                     continue
#                 return iface
#             except:
#                 continue
#
# def get_default_gateway_linux():
#     with open(ROUTE) as f:
#         for line in f:
#             fields = line.strip().split()
#             if fields[1] != '00000000' or not int(fields[3], 16) & 2:
#                 continue
#
#             return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
