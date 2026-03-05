# Log Analysis – Authentication Awareness

## Objective
Develop familiarity with Linux authentication logs and identify indicators of failed login attempts.

---

## Log Location

### Primary Log File

```
/var/log/auth.log
```

### Viewed Recent Log Entries

```bash
sudo tail -n 30 /var/log/auth.log
```

---

## Detecting Failed Login Attempts

### Searched for Failed Password Attempts

```bash
sudo grep "Failed password" /var/log/auth.log
```

### Counted Failed Attempts

```bash
sudo grep "Failed password" /var/log/auth.log | wc -l
```

---

## Controlled Test

### Simulated Failed Login

Simulated a failed login attempt using:

```bash
su fakeuser
```

### Verification

Verified the failed authentication event appeared in `/var/log/auth.log`.

---

## Key Findings

- Authentication logs provide critical visibility into login attempts
- Failed password attempts are logged and can be grepped for analysis
- Testing confirms log entries are generated for both successful and failed authentication events

---

## Phase 5 – Brute-Force Simulation Validation (Hydra)

In the isolated lab environment, repeated SSH login failures were generated from the Kali attacker VM and validated in real time on the Ubuntu defender.

Examples of useful validation commands:

```bash
sudo tail -f /var/log/auth.log
sudo grep "Failed password" /var/log/auth.log | tail -n 25
sudo grep "192.168.56.20" /var/log/auth.log | tail -n 25
```

---

## Phase 6 – SIEM Alert Validation (Wazuh)

After deploying Wazuh on Ubuntu, authentication log events from `/var/log/auth.log` were ingested into the SIEM and surfaced in the dashboard as security alerts.

Dashboard access required opening HTTPS through UFW:

```bash
sudo ufw allow 443/tcp
```

A custom rule was added in `/var/ossec/etc/rules/local_rules.xml` to elevate SSH authentication activity from the known lab attacker IP.

Rule metadata validated in dashboard alerts:

- Rule ID: `100100`
- Severity level: `12`

### Validation Outcomes

- Multiple SSH authentication failures appeared as Wazuh alerts
- Alert activity correlated with brute-force traffic generated from Kali attacker source configured in the local rule
- Events were mapped to MITRE ATT&CK credential access techniques
- Dashboard visibility confirmed end-to-end detection from log generation to analyst view

