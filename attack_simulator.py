import socket
import time

target_ip = "10.83.82.36"
target_port = 80

print("Starting attack simulation...")

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.send(b"attack_test")
        s.close()

        print("Simulated packet sent")

        time.sleep(0.01)

    except Exception:
        pass