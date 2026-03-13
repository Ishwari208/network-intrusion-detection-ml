from capture.packet_capture import start_capture
from features.feature_extractor import extract_features
from detection.predictor import predict
from alerts.alert_manager import send_alert
from monitor.traffic_monitor import track_ip


def process_packet(packet):

    try:
        # Track packet count from each IP
        track_ip(packet.src)

        # Extract packet features
        features = extract_features(packet)

        # Convert dictionary → list
        feature_list = list(features.values())

        # Pad features so the model receives 122 inputs
        while len(feature_list) < 122:
            feature_list.append(0)

        # Run ML prediction
        prediction, confidence = predict(feature_list)

        # Send alert / print result
        send_alert(packet.src, prediction, confidence)

    except Exception as e:
        print("Packet skipped:", e)


def start_system():
    print("Starting Real-Time Intrusion Detection System")
    start_capture(process_packet)


if __name__ == "__main__":
    start_system()