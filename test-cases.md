\# Test Cases — AI Code Review Assistant



\## Functional Tests (F)



| ID | Description | Expected Result | Actual Result | Status | Tester |

|----|-------------|-----------------|---------------|--------|--------|

| F1.1 | Detect hardcoded password in Python file | Finding reported on correct line | Finding reported on line 1 | Pass | Faizan |

| F1.2 | Detect hardcoded API key in Python file | Finding reported on correct line | Finding reported on line 2 | Pass | Faizan |

| F1.3 | Do not flag password pattern inside a comment | No finding for comment line | Comment line skipped | Pass | Faizan |

| F1.4 | Detect SQL injection using string concatenation | Finding reported on correct line | Finding reported on line 5 | Pass | Faizan |

| F1.5 | Detect weak hashing (md5) | Finding reported on correct line | Finding reported on line 9 | Pass | Faizan |

| F1.6 | Post comment on GitHub pull request | Comment appears on PR page | Comment appeared | Pass | Faizan |

| F1.7 | Save findings to database | Rows appear in dashboard table | 4 rows visible | Pass | Faizan |



\## Nonfunctional Tests (N)



| ID | Description | Expected Result | Actual Result | Status | Tester |

|----|-------------|-----------------|---------------|--------|--------|

| N1.1 | Scan a small file within 10 seconds | Completes under 10 seconds | Completed in under 2 seconds | Pass | Faizan |

| N1.2 | Dashboard loads quickly | Page loads under 3 seconds | Loaded instantly | Pass | Faizan |

| N1.3 | GitHub comment is readable | Markdown formatting renders correctly | Formatted correctly | Pass | Faizan |



\## Systemic Tests (S)



| ID | Description | Expected Result | Actual Result | Status | Tester |

|----|-------------|-----------------|---------------|--------|--------|

| S1.1 | Tool runs without GitHub App configuration | Shows clear error | Error shown when .env missing | Pass | Faizan |

| S1.2 | Tool handles unsupported file types | Skips non-Python/JS files | Files ignored correctly | Pass | Faizan |

