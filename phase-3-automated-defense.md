# Phase 3 – Automated Intrusion Prevention (Fail2Ban)

## Objective

Implement automated detection and response for repeated SSH authentication failures using Fail2Ban to reduce exposure to brute-force attacks.

---

## Overview

After configuring a hardened SSH service and enabling UFW, the next step was to automate detection and response.

Fail2Ban was installed to:

- Monitor authentication logs
- Detect repeated failed SSH login attempts
- Automatically insert firewall rules to block offending IP addresses

This transforms the system from passive logging to active intrusion prevention.

---

## Installation

Fail2Ban was installed using:

```bash
sudo apt install -y fail2ban
```

The service was verified as running:

```bash
sudo systemctl status fail2ban
```

---

## Jail Configuration

A custom configuration file was created at:

```
/etc/fail2ban/jail.local
```

The SSH jail was configured as follows:

```
[DEFAULT]
ignoreip = 127.0.0.1/8 ::1

bantime  = 600
findtime = 600
maxretry = 3

backend = auto

[sshd]
enabled  = true
port     = ssh
filter   = sshd
logpath  = /var/log/auth.log
```

### Configuration Summary

- **maxretry = 3** → Ban after 3 failed attempts
- **findtime = 600** → Failures counted within 10 minutes
- **bantime = 600** → 10 minute ban duration
- **ignoreip** excludes localhost to prevent accidental self-ban

---

## Testing Procedure

To simulate a brute-force attempt:

Port forwarding was configured in VirtualBox:

```
Host port 2222 → Guest port 22
```

From Windows (host system):

```bash
ssh fake@127.0.0.1 -p 2222
```

Multiple incorrect password attempts were made.

---

## Detection Results

Authentication failures were confirmed in:

```
/var/log/auth.log
```

Fail2Ban status showed:

```bash
sudo fail2ban-client status sshd
```

Result:

- Total failed: 3
- Currently banned: 1
- Banned IP list: 10.0.2.2

This confirmed the SSH jail was detecting failures and enforcing bans.

---

## Firewall Enforcement Verification

The firewall ruleset was inspected:

```bash
sudo nft list table inet f2b-table
```

Fail2Ban created:

- A dynamic IP set containing the banned IP
- A firewall chain hooked into INPUT
- A rule rejecting TCP port 22 traffic from banned IP addresses

Example rule behavior:

```
If source IP is in addr-set-sshd
And destination port is 22
Reject connection
```

This confirms that Fail2Ban dynamically modifies firewall rules to block malicious activity.
