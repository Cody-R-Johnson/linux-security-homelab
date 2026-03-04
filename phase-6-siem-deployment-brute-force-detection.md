# Phase 6 – SIEM Deployment and Brute Force Detection

## Overview

In this phase I expanded the lab by deploying the Wazuh SIEM platform on the Ubuntu server to monitor security events and detect suspicious activity.

After installation, the Wazuh dashboard was accessed through the web interface and configured to monitor system logs generated on the Ubuntu machine. Once the SIEM was running, I launched another SSH brute force attack from the Kali attacker machine using Hydra.

During the attack, the Ubuntu server generated repeated authentication failures in `/var/log/auth.log`. Wazuh ingested these logs and created security alerts that appeared in the dashboard.

The dashboard shows multiple authentication failures mapped to the MITRE ATT&CK framework under credential access techniques. The alerts correspond directly to the brute force activity generated from the Kali machine.

This confirms that the SIEM is successfully collecting logs, analyzing authentication activity, and generating alerts when suspicious login attempts occur.

This phase demonstrates how a SOC analyst would monitor authentication logs and investigate brute force activity using a SIEM.

---

## Key Observations

- Multiple SSH authentication failures detected
- Alerts generated from `/var/log/auth.log`
- Source activity correlated with the Kali attacker machine
- Events mapped to MITRE ATT&CK credential access techniques
- Security events visible in the Wazuh dashboard

---

## Lab Architecture

```
Kali Linux (Attacker)
    ↓
SSH brute force using Hydra
    ↓
Ubuntu Server (Target)
    ↓
Authentication logs generated (/var/log/auth.log)
    ↓
Wazuh SIEM ingestion
    ↓
Security alerts displayed in the dashboard
```

---

## Visual Evidence

![Wazuh Dashboard showing SSH brute force alerts](screenshots/wazuh-bruteforce-alert-dashboard.png)

*Screenshot : Wazuh SIEM dashboard displaying multiple SSH authentication failure alerts generated during the Hydra brute force attack from the Kali machine. Events are correlated with MITRE ATT&CK credential access techniques.*

---

## What This Demonstrates

**SIEM Deployment**
- Successfully installed and configured Wazuh SIEM on Ubuntu Server
- Web-based dashboard accessible and operational
- Log ingestion pipeline functioning correctly

**Security Monitoring**
- Real-time detection of authentication failures
- Correlation of security events with attacker activity
- MITRE ATT&CK framework mapping for threat intelligence

**SOC Analyst Skills**
- Log monitoring and analysis
- Alert triage and investigation
- Understanding SIEM capabilities and limitations
- Incident detection and documentation

---

## Next Steps

With a functional SIEM in place, future phases could include:
- Configuring custom detection rules
- Setting up email alerting for critical events
- Expanding monitoring to additional log sources
- Creating dashboards for specific threat scenarios
- Implementing automated response playbooks
