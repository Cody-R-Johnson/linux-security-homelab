# Phase 4 – Isolated Attacker/Defender Network

## Objective

Expand the lab into a multi-system environment to simulate real attacker and defender interaction.

---

## Network Configuration

VirtualBox Internal Network: `isolated-lab`

### Defender (Ubuntu Server)
- IP: 192.168.56.10
- Static configuration via netplan
- SSH hardened
- UFW enabled
- Fail2Ban active

### Attacker (Kali Linux)
- IP: 192.168.56.20
- Static configuration via NetworkManager
- Internal-only network access
- Prepared for reconnaissance and brute-force testing

---

## Security Design

The environment is fully isolated:

- No external internet exposure
- No access to host LAN
- No DHCP server
- Static addressing for controlled traffic analysis

This architecture enables safe simulation of:

- Port scanning
- Service enumeration
- Brute-force authentication attempts
- Log monitoring during live attacks
- Automated defensive response validation

---

## Validation

Connectivity confirmed via:

```bash
ping 192.168.56.10  # From Kali to Ubuntu
ping 192.168.56.20  # From Ubuntu to Kali
```

Both systems can communicate within the isolated network while remaining completely disconnected from external networks.
