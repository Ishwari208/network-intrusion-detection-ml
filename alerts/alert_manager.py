attack_count = 0
normal_count = 0

def send_alert(ip, prediction, confidence):

    global attack_count, normal_count

    if prediction == 1:
        attack_count += 1
        message = f"⚠ ATTACK DETECTED from {ip} (confidence {confidence:.2f})"
    else:
        normal_count += 1
        message = f"Normal traffic from {ip}"

    print(message)

    with open("alerts.log", "a") as f:
        f.write(message + "\n")

    print(f"Stats → Normal: {normal_count} | Attacks: {attack_count}")