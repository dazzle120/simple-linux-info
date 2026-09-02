import platform
import socket

print("=== System Info ===")
print(f"Hostname: {socket.gethostname()}")
print(f"OS: {platform.system()}")
print(f"OS Version: {platform.release()}")
print(f"Architecture: {platform.machine()}")
