# Linux Security Homelab

> A hands-on learning project focused on developing practical Linux security skills aligned with SOC and security analyst roles.

## Table of Contents

- [Overview](#overview)
- [Environment](#environment)
- [Project Goals](#project-goals)
- [Implementation Phases](#implementation-phases)
- [Key Security Concepts](#key-security-concepts-demonstrated)
- [Architecture](#architecture-summary)
- [Current Capabilities](#current-capabilities)
- [Documentation](#documentation)
- [Purpose](#purpose)

---

## Overview

This repository documents the development of a Linux-based security homelab focused on system hardening, log analysis, automated intrusion prevention, and network-based intrusion detection.

The lab is designed to simulate real-world defensive security practices in a controlled virtual environment. Each phase builds progressively from foundational Linux administration to layered defensive controls, culminating in SIEM-based monitoring, Python-driven log analysis, and Suricata IDS detection in an isolated attacker/defender network.

---

## Environment

- **Host System:** Windows 11  
- **Hypervisor:** Oracle VM VirtualBox  
- **Guest OS:** Ubuntu Server 22.04 LTS (defender) / Kali Linux (attacker)  
- **RAM Allocation:** 4GB per server
- **CPU Allocation:** 2 cores per server
- **Network Mode:** NAT with SSH port forwarding (initial setup) / Host-Only Adapter + Internal Network (`isolated-lab`)  

---

## Project Goals

- Develop practical Linux administration skills  
- Implement secure baseline configurations  
- Apply host-based firewall policies  
- Monitor authentication logs for anomalies  
- Automate brute-force detection and response  
- Understand how defensive tools interact with the firewall layer  
- Build an isolated attacker/defender environment for controlled security testing

---

## Implementation Phases

This project is organized into seven progressive phases, each building upon the previous:

### [Phase 1 – Foundations](phase-1-foundations.md)
Establishing the baseline Ubuntu Server environment and core Linux administration skills.
- Ubuntu Server installation and initial setup
- System updates and patching procedures
- User privilege management and awareness
- Service management with `systemctl`
- Log file familiarity (`/var/log/auth.log`)

### [Phase 2 – System Hardening](phase-2-hardening.md)
Implementing security controls to reduce attack surface and harden SSH access.
- UFW default-deny inbound firewall configuration
- Explicit SSH security configuration
- Root login disabled
- Password authentication controls
- Firewall logging enabled for monitoring

### [Phase 3 – Automated Intrusion Prevention](phase-3-automated-defense.md)
Deploying automated detection and response for SSH brute-force attacks.
- Fail2Ban installation and configuration
- SSH brute-force detection rules
- Threshold-based IP banning (3 failures in 10 minutes)
- Dynamic firewall rule injection via nftables
- Validation of automated blocking behavior
- Ban/unban testing and verification

### [Phase 4 – Isolated Attacker/Defender Lab](phase-4-isolated-lab.md)
Creating a multi-VM environment for realistic security testing without internet exposure.
- Kali Linux attacker VM deployment
- VirtualBox Internal Network configuration (`isolated-lab`)
- Static IP addressing:
  - Ubuntu (Defender): 192.168.56.10
  - Kali (Attacker): 192.168.56.20
- Network isolation verification
- Bidirectional connectivity testing
- Preparation for controlled reconnaissance and attack simulation

This phase transitions the lab from a single hardened host to a multi-system attacker/defender architecture.

### [Phase 5 – Brute-Force Simulation & Log Validation](phase-5-brute-force-simulation-log-validation.md)
Simulating an SSH brute-force attack from Kali to Ubuntu and validating log visibility and correlation.
- Hydra-based SSH brute-force simulation (port 22)
- Live monitoring of `/var/log/auth.log` during attack execution
- Source IP correlation between attacker and authentication failures
- Troubleshooting of initial network/IP misalignment

### [Phase 6 – SIEM Deployment and Brute Force Detection](phase-6-siem-deployment-brute-force-detection.md)
Deploying Wazuh SIEM platform to monitor security events and detect authentication attacks.
- Wazuh SIEM installation and configuration on Ubuntu Server
- Web dashboard access over HTTPS with UFW firewall adjustment (`ufw allow 443/tcp`)
- SSH brute-force attack simulation from Kali using Hydra
- Real-time log ingestion from `/var/log/auth.log`
- Custom local rule tuning in `/var/ossec/etc/rules/local_rules.xml`
- High-severity custom alert detection (Rule ID `100100`, Level `12`) with MITRE ATT&CK mapping
- SOC analyst workflow demonstration for authentication monitoring

### [Phase 7 – Python Log Analysis and Suricata IDS](phase-7-python-log-analysis-suricata-ids.md)
Expanding host and network monitoring through Python-driven SSH log analysis and Suricata IDS deployment.
- Python parsing of `/var/log/ssh_alerts.log` to identify attacking IPs and failed login patterns
- Threshold-based SSH attack severity classification (Low, Medium, High, Brute Force Attack)
- Suricata IDS installation, interface monitoring configuration, and rule set integration
- Validation of JSON-based alert generation in `/var/log/suricata/eve.json`
- Attack simulation from Kali with detection confirmation in host and network telemetry
- SOC-style layered workflow combining endpoint and network visibility

---

## Key Security Concepts Demonstrated

- Defense-in-depth
- Default-deny firewall posture
- SSH hardening best practices
- Log-based detection
- Automated response mechanisms
- Firewall rule inspection and verification

---

## Architecture Summary

The system implements layered host-based defense:

1. Operating system hardening  
2. Restricted SSH access  
3. UFW firewall enforcement  
4. Authentication log monitoring  
5. Fail2Ban automated IP blocking  
6. Wazuh SIEM alerting and event correlation  
7. Python SSH log analysis and threat classification  
8. Suricata IDS network alerting and packet-level detection  

Fail2Ban dynamically injects firewall rules to reject malicious SSH traffic once configured thresholds are exceeded, Wazuh ingests authentication logs and surfaces correlated alerts for SOC-style investigation, and Suricata provides packet-level network detection to complement host telemetry.

---

## Current Capabilities

-  Hardened Ubuntu Server baseline
-  Controlled network exposure via UFW firewall
-  Automated brute-force mitigation with Fail2Ban
-  Firewall rule auditing and verification
-  Log-based detection and monitoring
-  Isolated attacker/defender lab environment
-  Multi-VM architecture for security testing
-  Brute-force simulation and authentication log validation in an isolated lab
-  Wazuh SIEM deployment with real-time security event monitoring
-  Custom Wazuh SSH threat-intel rule for attacker-IP alert prioritization
-  Python-based SSH alert log analysis with attack severity classification
-  Suricata IDS deployment with real-time network alerting via `eve.json`

---

## Documentation

Detailed documentation is organized into the following files:

### Phase Guides
- **[Phase 1: Foundations](phase-1-foundations.md)** - Initial setup and Linux administration basics
- **[Phase 2: Hardening](phase-2-hardening.md)** - System and SSH security hardening
- **[Phase 3: Automated Defense](phase-3-automated-defense.md)** - Fail2Ban implementation and testing
- **[Phase 4: Isolated Lab](phase-4-isolated-lab.md)** - Multi-VM attacker/defender environment
- **[Phase 5: Brute-Force Simulation & Log Validation](phase-5-brute-force-simulation-log-validation.md)** - Simulated SSH brute-force and auth log validation
- **[Phase 6: SIEM Deployment and Brute Force Detection](phase-6-siem-deployment-brute-force-detection.md)** - Wazuh SIEM deployment and authentication monitoring
- **[Phase 7: Python Log Analysis and Suricata IDS](phase-7-python-log-analysis-suricata-ids.md)** - Python SSH log analytics and Suricata network intrusion detection

### Technical Documentation
- **[Architecture Overview](architecture-overview.md)** - System architecture and component interactions
- **[Logs Analysis](logs-analysis.md)** - Log monitoring, detection patterns, and analysis techniques

### Phase Scripts
- **[Phase 7 log_analysis.py](scripts/phase-7/log_analysis.py)** - Python parser and classifier for `/var/log/ssh_alerts.log`

### Visual Documentation
- **[Screenshots](screenshots/)** - Visual evidence of configurations and testing

---

## Planned Lab Expansions

- [ ] Internal network reconnaissance and port scanning (Nmap)
- [ ] File integrity monitoring deployment (AIDE)
- [ ] Centralized log aggregation using rsyslog
- [x] Host-based intrusion detection (Wazuh)
- [x] Network-based IDS deployment (Suricata)
- [ ] Documented incident response playbooks for simulated attacks

---

## Purpose

This homelab is a hands-on learning project focused on developing practical Linux security skills aligned with SOC and security analyst roles.

**Key Learning Outcomes:**
- Linux system administration and hardening
- Firewall configuration and management
- Log analysis and pattern recognition
- Python-based security log parsing and classification
- Automated security response mechanisms
- Network intrusion detection with Suricata
- Attacker/defender mindset development
- Virtual network design and isolation

All testing is conducted in an isolated virtual environment with no exposure to production systems or the internet during security testing phases.

---

## About

**Author:** Cody Johnson  
**Last Updated:** March 2026  
**Status:** Active Development

This project demonstrates a methodical approach to building security infrastructure and developing defensive security skills through hands-on practice.
