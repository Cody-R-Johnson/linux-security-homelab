# Phase 5 – Brute-Force Simulation & Log Validation

## Objective

Simulate a real-world SSH brute-force attack from Kali Linux against an Ubuntu Server target and validate logging and monitoring behavior inside a controlled lab environment.

---

## Lab Network Configuration

- Configured **Kali Linux (attacker)** and **Ubuntu Server (target)** to operate on:
  - Host-Only Adapter
  - Internal Network (`isolated-lab`)
- Verified connectivity between machines using `ping`.
- Confirmed the lab environment is isolated and not exposed to the public internet.
- Identified and corrected an incorrect target IP during initial testing.

---

## SSH Attack Simulation (Hydra)

- Executed a brute-force attack against the Ubuntu SSH service using `hydra` from Kali.
- Targeted SSH on port 22.
- Generated repeated failed login attempts.
- Resolved initial script formatting issue (`<<'EOF'` confusion) and successfully executed the attack.
- Confirmed Hydra was actively sending authentication attempts.

---

## Log Monitoring & Validation

- Monitored `/var/log/auth.log` on Ubuntu during the attack.
- Observed:
  - Repeated failed password attempts
  - Authentication failure entries
  - Source IP correlation with the Kali machine
- Confirmed logs updated in real time during the brute-force attempt.

---

## Troubleshooting & Adjustments

- Diagnosed SSH monitor not updating during initial test.
- Verified correct IP addressing.
- Confirmed network adapters were properly aligned on the same internal network.
- Validated successful packet flow once configuration was corrected.

---

## Security Concepts Demonstrated

- SSH brute-force attack mechanics
- Internal network segmentation using VirtualBox
- Log-based detection of authentication abuse
- Correlating attack activity with system logs
- Controlled offensive testing inside an isolated lab

---

## Outcome

Successfully simulated a brute-force attack in a controlled environment and validated that:

- Attack traffic reached the target
- Authentication failures were logged properly
- Logs reflected attack timing and source IP accurately

This phase demonstrates practical understanding of attack simulation, log analysis, and lab-based security validation.
