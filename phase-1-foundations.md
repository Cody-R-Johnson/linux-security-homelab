# Phase 1 – Linux Foundations

## Objective

Establish a clean Ubuntu Server environment and develop familiarity with core Linux administrative concepts before applying security hardening techniques.

---

## Environment Setup

### Host System
- Windows 11

### Hypervisor
- Oracle VM VirtualBox

### Guest OS
- Ubuntu Server 22.04 LTS

### VM Configuration
- RAM: 4GB
- CPU: 2 cores
- Storage: 25GB (dynamically allocated)
- Network Mode: NAT

---

## System Initialization

After installation, the system was updated to ensure all packages and security patches were current.

### Commands Used

```bash
sudo apt update
sudo apt upgrade -y
```

### Purpose

- Apply latest security patches
- Update system packages
- Establish secure baseline before configuration changes
