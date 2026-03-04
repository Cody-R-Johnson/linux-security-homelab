# Architecture Overview – Ubuntu Security Lab

## Environment Summary

This homelab environment is designed to simulate a hardened Linux server with layered defensive controls.

The lab is hosted on:

- Host OS: Windows 11
- Hypervisor: Oracle VirtualBox
- Guest OS: Ubuntu Server 22.04 LTS (defender) / Kali Linux (attacker)

---

## Network Architecture

This lab uses two networking modes depending on the phase:

- Initial setup: VirtualBox NAT + SSH port forwarding
        - Host Port 2222 → Guest Port 22 (SSH)
- Isolated lab: VirtualBox Internal Network (`isolated-lab`) (and Host-Only Adapter as needed)

This supports both safe host-to-VM administration during setup and fully isolated attacker/defender testing in later phases.

---

## Lab Topology (Current)

VirtualBox Internal Network: isolated-lab

Kali Linux (Attacker)
IP: 192.168.56.20
        ↓
Ubuntu Server (Defender)
IP: 192.168.56.10
        ↓
UFW + Fail2Ban + nftables + Wazuh SIEM

Both systems are isolated from the host network and internet.
All attack simulation is contained within the virtual environment.

---

## System Components

### 1. Operating System Layer
Ubuntu Server 22.04 LTS
- Updated packages
- Non-root administrative model
- systemd service management

---

### 2. Access Control Layer

SSH Service:
- Root login disabled
- Password authentication explicitly defined
- Service monitored via logs

---

### 3. Firewall Layer

UFW (Uncomplicated Firewall):
- Default deny inbound policy
- Default allow outbound policy
- Explicit SSH allowance
- Logging enabled

Underlying firewall system:
- iptables-nft compatibility mode
- nftables rule engine

---

### 4. Detection Layer

Log Monitoring:
- Authentication logs located at `/var/log/auth.log`
- SSH failure events parsed by Fail2Ban

Fail2Ban:
- Monitors SSH login failures
- Threshold: 3 failed attempts within 10 minutes
- Ban duration: 10 minutes
- Automatically injects firewall rules

Wazuh SIEM:
- Ingests authentication logs from Ubuntu
- Detects and alerts on suspicious authentication activity
- Correlates events for dashboard-based investigation

---

### 5. Prevention Layer

Fail2Ban dynamically creates:

- nftables table: `f2b-table`
- IP set: `addr-set-sshd`
- Firewall chain hooked into INPUT
- Rule rejecting SSH connections from banned IPs

This creates automated host-level intrusion prevention.

---

### 6. SIEM Visibility Layer

Wazuh dashboard provides centralized visibility into authentication events, including repeated SSH failures generated during brute-force simulation from Kali.

- Alerts are visible in the web interface
- Authentication activity is mapped to MITRE ATT&CK credential access techniques
- Supports SOC-style monitoring and triage workflows

---

## Defense-in-Depth Model

The system now implements layered defense:

1. OS Hardening
2. SSH Configuration Restrictions
3. Default-Deny Firewall Policy
4. Log-Based Detection
5. Automated Firewall Enforcement
6. SIEM Alerting and Correlation

Each layer reduces risk independently and collectively strengthens security posture.

---

## Current Capabilities

- Hardened SSH service
- Controlled network exposure
- Automated brute-force detection
- Dynamic IP blocking
- Firewall rule inspection and verification
- Isolated Kali → Ubuntu attack simulation with real-time auth log validation
- SIEM-based authentication alerting and event correlation in Wazuh

---

## Next Planned Enhancements

- Centralized log aggregation
- File integrity monitoring
- SIEM detection coverage expansion beyond SSH authentication events