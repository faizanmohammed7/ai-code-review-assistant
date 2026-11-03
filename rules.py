import re

def check_hardcoded_password(filename, content):
    findings = []
    lines = content.splitlines()
    pattern = re.compile(
        r'(password|passwd|pwd|secret|api_key|apikey|token)\s*=\s*["\']([^"\']{3,})["\']',
        re.IGNORECASE
    )
    for line_number, line in enumerate(lines, start=1):
        if line.strip().startswith("#") or line.strip().startswith("//"):
            continue
        match = pattern.search(line)
        if match:
            findings.append({
                "rule": "Hardcoded Credential",
                "file": filename,
                "line": line_number,
                "matched": match.group(0),
                "suggestion": "Do not store secrets in source code. Use environment variables or a secrets manager."
            })
    return findings


def check_sql_injection(filename, content):
    findings = []
    lines = content.splitlines()
    # Detect SQL keyword followed by string concatenation anywhere in the line
    sql_keywords = re.compile(r'(SELECT|INSERT|UPDATE|DELETE)', re.IGNORECASE)
    concat_pattern = re.compile(r'["\'].*\+.*["\']|["\'].*["\']\s*\+')
    for line_number, line in enumerate(lines, start=1):
        if line.strip().startswith("#") or line.strip().startswith("//"):
            continue
        if sql_keywords.search(line) and concat_pattern.search(line):
            findings.append({
                "rule": "SQL Injection Risk",
                "file": filename,
                "line": line_number,
                "matched": line.strip(),
                "suggestion": "Use parameterized queries instead of string concatenation in SQL."
            })
    return findings


def check_weak_hashing(filename, content):
    findings = []
    lines = content.splitlines()
    pattern = re.compile(r'\b(md5|sha1)\s*\(', re.IGNORECASE)
    for line_number, line in enumerate(lines, start=1):
        if line.strip().startswith("#") or line.strip().startswith("//"):
            continue
        match = pattern.search(line)
        if match:
            findings.append({
                "rule": "Weak Hashing Algorithm",
                "file": filename,
                "line": line_number,
                "matched": match.group(0),
                "suggestion": "Use SHA-256 or stronger hashing algorithms. MD5 and SHA-1 are considered insecure."
            })
    return findings