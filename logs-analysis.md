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

