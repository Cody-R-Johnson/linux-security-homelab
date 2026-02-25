# Architecture Overview – Ubuntu Security Lab

## Environment Summary

This homelab environment is designed to simulate a hardened Linux server with layered defensive controls.

The lab is hosted on:

- Host OS: Windows 11
- Hypervisor: Oracle VirtualBox
- Guest OS: Ubuntu Server 22.04 LTS

---

## Network Architecture

VirtualBox NAT networking is used.

Port forwarding is configured:

- Host Port 2222 → Guest Port 22 (SSH)

This allows external SSH testing from the Windows host to the Ubuntu VM while maintaining isolation from the broader network.

---

## Lab Topology (Current)

VirtualBox Internal Network: isolated-lab

Kali Linux (Attacker)
IP: 192.168.56.20
        ↓
Ubuntu Server (Defender)
IP: 192.168.56.10
        ↓
UFW + Fail2Ban + nftables

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

---

### 5. Prevention Layer

Fail2Ban dynamically creates:

- nftables table: `f2b-table`
- IP set: `addr-set-sshd`
- Firewall chain hooked into INPUT
- Rule rejecting SSH connections from banned IPs

This creates automated host-level intrusion prevention.

---

## Defense-in-Depth Model

The system now implements layered defense:

1. OS Hardening
2. SSH Configuration Restrictions
3. Default-Deny Firewall Policy
4. Log-Based Detection
5. Automated Firewall Enforcement

Each layer reduces risk independently and collectively strengthens security posture.

---

## Current Capabilities

- Hardened SSH service
- Controlled network exposure
- Automated brute-force detection
- Dynamic IP blocking
- Firewall rule inspection and verification

---

## Next Planned Enhancements

- Centralized log aggregation
- Separate attacker VM (Kali Linux)
- Brute-force simulation using Hydra
- File integrity monitoring
- Intrusion detection expansion beyond SSH