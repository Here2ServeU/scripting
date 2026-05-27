"""
Python for AI & ML Engineers
Project 1: Real-World Log Parser
github.com/Here2ServeU/scripting

This project ties together all 5 patterns in a real-world scenario:
you have a stream of log lines and need to generate a full analysis report.

Patterns used:
  Pattern 1 (Counter)       — count errors per service
  Pattern 2 (defaultdict)   — group log lines by level
  Pattern 3 (sorted/lambda) — rank services by error count
  Pattern 5 (set)           — find new error types vs baseline
"""

from collections import Counter, defaultdict


# ── STEP 1: PARSE ─────────────────────────────────────────────────────────────

def parse_line(line):
    """
    Parse a structured log line into a dict.

    Format: TIMESTAMP LEVEL SERVICE MESSAGE...

    Returns:
        {'timestamp': str, 'level': str, 'service': str, 'message': str}
        or {} if the line is malformed.
    """
    if not line:
        return {}
    parts = line.strip().split()
    if len(parts) < 3:
        return {}
    return {
        'timestamp': parts[0],
        'level':     parts[1].upper(),
        'service':   parts[2],
        'message':   ' '.join(parts[3:]) if len(parts) > 3 else '',
        'raw':       line.strip(),
    }


def parse_logs(lines):
    """Parse a list of raw log lines. Skip malformed lines."""
    return [p for line in lines if (p := parse_line(line))]


# ── STEP 2: ANALYSE ───────────────────────────────────────────────────────────

def error_count_per_service(parsed_logs):
    """Pattern 1 — Count ERROR lines per service."""
    if not parsed_logs:
        return {}
    errors = [log['service'] for log in parsed_logs if log['level'] == 'ERROR']
    return dict(Counter(errors))


def group_by_level(parsed_logs):
    """Pattern 2 — Group all log lines by level."""
    if not parsed_logs:
        return {}
    groups = defaultdict(list)
    for log in parsed_logs:
        groups[log['level']].append(log['raw'])
    return dict(groups)


def top_error_services(parsed_logs, k=3):
    """Pattern 3 — Return the k services with the most errors."""
    if not parsed_logs:
        return []
    counts = error_count_per_service(parsed_logs)
    return sorted(counts, key=counts.get, reverse=True)[:k]


def new_error_types(baseline_errors, current_errors):
    """Pattern 5 — Error types in current that were not in baseline."""
    return sorted(set(current_errors) - set(baseline_errors))


# ── STEP 3: REPORT ────────────────────────────────────────────────────────────

def generate_report(lines, baseline_errors=None):
    """Full analysis report for a batch of log lines."""
    parsed   = parse_logs(lines)
    by_level = group_by_level(parsed)
    err_svc  = error_count_per_service(parsed)
    top_svcs = top_error_services(parsed, k=3)

    current_error_msgs = [
        log['message'] for log in parsed if log['level'] == 'ERROR'
    ]
    new_errors = new_error_types(baseline_errors or [], current_error_msgs)

    print("=" * 55)
    print("  LOG ANALYSIS REPORT")
    print("=" * 55)
    print(f"\n  Total lines parsed:  {len(parsed)}")
    print(f"\n  Lines by level:")
    for level in ['ERROR', 'WARN', 'INFO', 'DEBUG']:
        n = len(by_level.get(level, []))
        if n:
            bar = '▓' * n
            print(f"    {level:<8} {n:>4}  {bar}")

    print(f"\n  Errors per service:")
    for svc, n in sorted(err_svc.items(), key=lambda x: -x[1]):
        print(f"    {svc:<20} {n}")

    print(f"\n  Top 3 error services:  {top_svcs}")

    if new_errors:
        print(f"\n  ⚠️  New error types (not in baseline):")
        for e in new_errors:
            print(f"    - {e}")
    else:
        print(f"\n  ✅  No new error types vs baseline.")

    print("=" * 55)


# ── DEMO ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    SAMPLE_LOGS = [
        "2024-01-15 ERROR everse-api request timeout after 30s",
        "2024-01-15 INFO  auth-service user login successful",
        "2024-01-15 ERROR everse-api connection refused to database",
        "2024-01-15 WARN  worker-1 queue depth exceeding threshold",
        "2024-01-15 ERROR everse-api oom killed pod restarting",
        "2024-01-15 INFO  scheduler next run in 60s",
        "2024-01-15 ERROR auth-service token verification failed",
        "2024-01-15 ERROR worker-1 job processing failed max retries",
        "2024-01-15 DEBUG everse-api processing request id 8472",
        "2024-01-15 WARN  cache-service eviction rate high",
        "2024-01-15 ERROR everse-api disk write error",
        "2024-01-15 INFO  worker-1 job completed successfully",
    ]

    BASELINE = [
        "connection refused to database",
        "token verification failed",
    ]

    generate_report(SAMPLE_LOGS, BASELINE)
