"""
Module 4: Brute-Force Attack Detector (by IP Address)
------------------------------------------------------
Analyzes login attempt logs to detect potential IP-based brute-force attacks.
Identifies IP addresses accumulating 3 or more failed login attempts.
"""

from collections import defaultdict
from typing import List, Dict, Any


def detect_brute_force_attacks(logs: List[Dict[str, Any]], threshold: int = 3) -> Dict[str, Any]:
    """Processes authentication log records and identifies IP addresses exceeding failed attempt threshold."""
    ip_failed_counts = defaultdict(int)
    ip_targeted_users = defaultdict(set)
    ip_attempt_timestamps = defaultdict(list)

    total_logs = len(logs)
    total_failures = 0

    for log in logs:
        ip = log.get("ip_address") or log.get("ip") or log.get("source_ip", "0.0.0.0")
        user = log.get("username") or log.get("user", "unknown")
        status = str(log.get("status") or log.get("result", "")).upper()
        timestamp = log.get("timestamp", "N/A")

        if status in ("FAILED", "FAILURE", "INVALID"):
            total_failures += 1
            ip_failed_counts[ip] += 1
            ip_targeted_users[ip].add(user)
            ip_attempt_timestamps[ip].append(timestamp)

    flagged_ips = []
    for ip, count in ip_failed_counts.items():
        if count >= threshold:
            flagged_ips.append({
                "ip_address": ip,
                "failed_attempts": count,
                "targeted_users": sorted(list(ip_targeted_users[ip])),
                "timestamps": ip_attempt_timestamps[ip],
                "risk_level": "HIGH" if count >= 5 else "MEDIUM"
            })

    flagged_ips.sort(key=lambda x: x["failed_attempts"], reverse=True)

    return {
        "total_logs_processed": total_logs,
        "total_failed_attempts": total_failures,
        "threshold_applied": threshold,
        "suspicious_ip_count": len(flagged_ips),
        "flagged_ips": flagged_ips,
        "all_ip_counts": dict(ip_failed_counts)
    }
