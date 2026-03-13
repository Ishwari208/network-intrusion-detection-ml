from collections import defaultdict
import time

ip_packet_count = defaultdict(int)
start_time = time.time()

THRESHOLD = 20  # lower for easier demo


def track_ip(ip):

    global start_time

    ip_packet_count[ip] += 1

    # check every 5 seconds
    if time.time() - start_time > 5:

        for ip_addr, count in ip_packet_count.items():

            if count > THRESHOLD:
                print(f"⚠ Suspicious traffic detected from {ip_addr} ({count} packets)")

        ip_packet_count.clear()
        start_time = time.time()