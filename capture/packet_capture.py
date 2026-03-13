from scapy.all import sniff


def start_capture(callback):
    print("Starting packet capture...")
    sniff(prn=callback, store=False)