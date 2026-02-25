# Linux Security Homelab

## Overview

This repository documents the development of a Linux-based security homelab focused on system hardening, log analysis, and automated intrusion prevention.

The lab is designed to simulate real-world defensive security practices in a controlled virtual environment. Each phase builds progressively from foundational Linux administration to layered defensive controls.

---

## Environment

- **Host System:** Windows 11  
- **Hypervisor:** Oracle VM VirtualBox  
- **Guest OS:** Ubuntu Server 22.04 LTS  
- **RAM Allocation:** 4GB  
- **CPU Allocation:** 2 cores  
- **Network Mode:** NAT with SSH port forwarding  

---

## Project Goals

- Develop practical Linux administration skills  
- Implement secure baseline configurations  
- Apply host-based firewall policies  
- Monitor authentication logs for anomalies  
- Automate brute-force detection and response  
- Understand how defensive tools interact with the firewall layer  

---

## Phase Breakdown

### Phase 1 – Foundations
- Ubuntu Server installation
- System updates and patching
- User privilege awareness
- Service management with `systemctl`
- Log familiarity (`/var/log/auth.log`)

### Phase 2 – System Hardening
- UFW default-deny inbound firewall configuration
- Explicit SSH security configuration
- Root login disabled
- Firewall logging enabled

### Phase 3 – Automated Intrusion Prevention
- Fail2Ban deployment
- SSH brute-force detection
- Threshold-based IP banning
- Dynamic firewall rule injection via nftables
- Validation of automated blocking behavior

### Phase 4 – Isolated Attacker/Defender Lab

- Added Kali Linux attacker VM
- Configured VirtualBox Internal Network (`isolated-lab`)
- Assigned static IP addresses:
  - Ubuntu (Defender): 192.168.56.10
  - Kali (Attacker): 192.168.56.20
- Verified bidirectional connectivity
- Created fully isolated environment (no internet exposure)
- Prepared lab for controlled reconnaissance and brute-force simulation

This phase transitions the lab from a single hardened host to a multi-system attacker/defender architecture.

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

Fail2Ban dynamically injects firewall rules to reject malicious SSH traffic once configured thresholds are exceeded.

---

## Current Capabilities

- Hardened Ubuntu Server baseline
- Controlled network exposure
- Automated brute-force mitigation
- Firewall rule auditing
- Log-based detection awareness

---

## Planned Enhancements

- Centralized log aggregation
- Dedicated attacker VM (Kali Linux)
- Brute-force simulation using Hydra
- File integrity monitoring
- Expanded intrusion detection coverage

---

## Purpose

This homelab is a hands-on learning project focused on developing practical Linux security skills aligned with SOC and security analyst roles.

All testing is conducted in an isolated virtual environment.