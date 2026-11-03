from rules import check_hardcoded_password, check_sql_injection, check_weak_hashing

def scan_file(filename, content):
    findings = []
    findings.extend(check_hardcoded_password(filename, content))
    findings.extend(check_sql_injection(filename, content))
    findings.extend(check_weak_hashing(filename, content))
    return findings

def scan_files(file_list):
    all_findings = []
    for filename, content in file_list:
        all_findings.extend(scan_file(filename, content))
    return all_findings