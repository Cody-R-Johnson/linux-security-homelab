# Phase 2: Hardening

## Overview

This phase focuses on foundational hardening techniques and security improvements for the Linux systems in the homelab.

# System Hardening (UFW Firewall)

## Goal
Enable a host-based firewall to reduce attack surface and enforce a default-deny inbound policy while keeping required administrative access.

## Actions Taken
- Installed UFW (Uncomplicated Firewall)
- Set default firewall policy:
  - Deny all inbound traffic by default
  - Allow all outbound traffic by default
- Allowed SSH to keep remote administration available
- Enabled firewall logging for visibility
- Enabled the firewall and verified active rules

## Commands Used
```bash
sudo apt install -y ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow OpenSSH
sudo ufw logging on
sudo ufw enable
sudo ufw status verbose
```

## SSH Configuration Hardening

### Goal
Reduce remote attack surface by explicitly defining secure SSH settings.

### Configuration Changes
Edited `/etc/ssh/sshd_config` to explicitly define:
```
PermitRootLogin no
PasswordAuthentication yes
```

### Actions Taken
- Disabled root login to prevent direct root access via SSH.
- Explicitly defined password authentication policy.
- Restarted SSH service to apply changes:
  - `sudo systemctl restart ssh`
- Verified SSH service status:
  - `sudo systemctl status ssh`

### Security Rationale
Disabling root login reduces the risk of brute-force attacks targeting privileged accounts. Explicitly defining SSH configuration settings ensures consistent behavior and prevents reliance on default configurations.