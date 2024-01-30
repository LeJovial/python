import socket
import platform
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
version_systeme = platform.system() + " " + platform.version()

print(f"Architecture: {platform.architecture()}")
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"   Version du système d'exploitation: {version_systeme}")