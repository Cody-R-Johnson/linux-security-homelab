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

This repository documents the development of a Linux-based security homelab focused on system hardening, log analysis, and automated intrusion prevention.

The lab is designed to simulate real-world defensive security practices in a controlled virtual environment. Each phase builds progressively from foundational Linux administration to layered defensive controls, culminating in an isolated attacker/defender network for controlled security testing.

---

## Environment

- **Host System:** Windows 11  
- **Hypervisor:** Oracle VM VirtualBox  
- **Guest OS:** Ubuntu Server 22.04 LTS  
- **RAM Allocation:** 4GB  
- **CPU Allocation:** 2 cores  
- **Network Mode:** NAT with SSH port forwarding (initial setup) / Internal Network (isolated lab)  

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

This project is organized into four progressive phases, each building upon the previous:

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
- Threshold-based IP banning (5 failures in 10 minutes)
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

-  Hardened Ubuntu Server baseline
-  Controlled network exposure via UFW firewall
-  Automated brute-force mitigation with Fail2Ban
-  Firewall rule auditing and verification
-  Log-based detection and monitoring
-  Isolated attacker/defender lab environment
-  Multi-VM architecture for security testing

---

## Documentation

Detailed documentation is organized into the following files:

### Phase Guides
- **[Phase 1: Foundations](phase-1-foundations.md)** - Initial setup and Linux administration basics
- **[Phase 2: Hardening](phase-2-hardening.md)** - System and SSH security hardening
- **[Phase 3: Automated Defense](phase-3-automated-defense.md)** - Fail2Ban implementation and testing
- **[Phase 4: Isolated Lab](phase-4-isolated-lab.md)** - Multi-VM attacker/defender environment

### Technical Documentation
- **[Architecture Overview](architecture-overview.md)** - System architecture and component interactions
- **[Logs Analysis](logs-analysis.md)** - Log monitoring, detection patterns, and analysis techniques

### Visual Documentation
- **[Screenshots](screenshots/)** - Visual evidence of configurations and testing

---

## Planned Lab Expansions

- [ ] SSH brute-force simulation using Hydra (Kali VM → Ubuntu target)
- [ ] Internal network reconnaissance and port scanning (Nmap)
- [ ] File integrity monitoring deployment (AIDE)
- [ ] Centralized log aggregation using rsyslog
- [ ] Host-based intrusion detection (Wazuh)
- [ ] Network-based IDS deployment (Suricata)
- [ ] Documented incident response playbooks for simulated attacks

---

## Purpose

This homelab is a hands-on learning project focused on developing practical Linux security skills aligned with SOC and security analyst roles.

**Key Learning Outcomes:**
- Linux system administration and hardening
- Firewall configuration and management
- Log analysis and pattern recognition
- Automated security response mechanisms
- Attacker/defender mindset development
- Virtual network design and isolation

All testing is conducted in an isolated virtual environment with no exposure to production systems or the internet during security testing phases.

---

## Getting Started

1. Review the [Phase 1: Foundations](phase-1-foundations.md) guide to set up your environment
2. Follow each phase sequentially to build skills progressively
3. Review the [Architecture Overview](architecture-overview.md) to understand system components
4. Use the [Logs Analysis](logs-analysis.md) guide to understand detection patterns

---

## About

**Author:** Security Homelab Project  
**Last Updated:** February 2026  
**Status:** Active Development

This project demonstrates a methodical approach to building security infrastructure and developing defensive security skills through hands-on practice.