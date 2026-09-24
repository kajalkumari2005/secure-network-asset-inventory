import socket
import platform
import uuid
import os
from datetime import datetime

hostname = socket.gethostname()

try:
    local_ip = socket.gethostbyname(hostname)
except:
    local_ip = "Unable to detect"

mac_address = ":".join(
    f"{(uuid.getnode() >> i) & 0xff:02x}"
    for i in range(40, -1, -8)
)

os_info = platform.platform()

try:
    interfaces = os.listdir("/sys/class/net/")
except:
    interfaces = ["Unable to detect"]

print("===== Secure Network Asset Inventory =====")
print("Hostname:", hostname)
print("Local IP:", local_ip)
print("MAC Address:", mac_address)
print("Operating System:", os_info)
print("Network Interfaces:", ", ".join(interfaces))

report = f"""Secure Network Asset Inventory Report
Generated: {datetime.now()}

Hostname: {hostname}
Local IP: {local_ip}
MAC Address: {mac_address}
Operating System: {os_info}
Network Interfaces: {", ".join(interfaces)}
"""

with open("system_report.txt", "w") as file:
    file.write(report)

print("\nReport saved as system_report.txt")
