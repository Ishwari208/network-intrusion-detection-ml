from scapy.layers.inet import IP, TCP, UDP

def extract_features(packet):

    features = {}

    # packet length
    features["packet_length"] = len(packet)

    # protocol
    if packet.haslayer(TCP):
        features["protocol"] = 1
    elif packet.haslayer(UDP):
        features["protocol"] = 2
    else:
        features["protocol"] = 0

    # source bytes
    features["src_bytes"] = len(packet)

    # destination bytes (placeholder)
    features["dst_bytes"] = len(packet)

    # duration placeholder
    features["duration"] = 0

    # source port
    if packet.haslayer(TCP):
        features["src_port"] = packet[TCP].sport
    elif packet.haslayer(UDP):
        features["src_port"] = packet[UDP].sport
    else:
        features["src_port"] = 0

    # destination port
    if packet.haslayer(TCP):
        features["dst_port"] = packet[TCP].dport
    elif packet.haslayer(UDP):
        features["dst_port"] = packet[UDP].dport
    else:
        features["dst_port"] = 0

    return features