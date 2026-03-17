import re
from collections import defaultdict

log_file = "/var/log/ssh_alerts.log"

alert_count = 0
info_count = 0
ip_failures = defaultdict(int)
ip_alert_events = defaultdict(int)

alert_pattern = re.compile(r"top_sources=([\d\.]+) \((\d+)\)")

print("\n===== SSH ALERT LOG ANALYSIS =====\n")

with open(log_file, "r") as file:
    for line in file:
        if "[ALERT]" in line:
            alert_count += 1

            ip_match = alert_pattern.search(line)

            if ip_match:
                ip = ip_match.group(1)
                failures = int(ip_match.group(2))

                ip_failures[ip] += failures
                ip_alert_events[ip] += 1

                print(f"Alert detected from {ip} with {failures} failures")

        elif "[INFO]" in line:
            info_count += 1


def classify_attack(total_failures, total_alerts):
    if total_failures >= 100 or total_alerts >= 4:
        return "BRUTE FORCE ATTACK"
    elif total_failures >= 50 or total_alerts >= 3:
        return "HIGH"
    elif total_failures >= 20 or total_alerts >= 2:
        return "MEDIUM"
    else:
        return "LOW"


print("\n===== SUMMARY =====\n")

print(f"Total alert events: {alert_count}")
print(f"Informational events: {info_count}\n")

print("Top Attacking IPs:")
for ip, failures in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True):
    print(f"{ip} -> {failures} failed attempts across {ip_alert_events[ip]} alert events")

print("\nAttack Classification:")
for ip, failures in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True):
    classification = classify_attack(failures, ip_alert_events[ip])
    print(f"{ip} -> {classification}")

print("\nSuspicious IPs:")
found_suspicious = False
for ip, failures in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True):
    classification = classify_attack(failures, ip_alert_events[ip])
    if classification in ["HIGH", "BRUTE FORCE ATTACK"]:
        print(f"ALERT: {ip} classified as {classification} with {failures} failures")
        found_suspicious = True

if not found_suspicious:
    print("No high-confidence suspicious IPs detected.")

print("\n===== END REPORT =====\n")

with open("analysis_report.txt", "w") as report:
    report.write("SSH ALERT ANALYSIS REPORT\n\n")
    report.write(f"Total alert events: {alert_count}\n")
    report.write(f"Informational events: {info_count}\n\n")

    report.write("Top Attacking IPs:\n")
    for ip, failures in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True):
        report.write(f"{ip} -> {failures} failed attempts across {ip_alert_events[ip]} alert events\n")

    report.write("\nAttack Classification:\n")
    for ip, failures in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True):
        classification = classify_attack(failures, ip_alert_events[ip])
        report.write(f"{ip} -> {classification}\n")

    report.write("\nSuspicious IPs:\n")
    found_suspicious = False
    for ip, failures in sorted(ip_failures.items(), key=lambda x: x[1], reverse=True):
        classification = classify_attack(failures, ip_alert_events[ip])
        if classification in ["HIGH", "BRUTE FORCE ATTACK"]:
            report.write(f"{ip} classified as {classification} with {failures} failures\n")
            found_suspicious = True

    if not found_suspicious:
        report.write("No high-confidence suspicious IPs detected.\n")
