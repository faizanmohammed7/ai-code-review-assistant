\# Presentation Draft — AI Code Review Assistant



\## Slide 1: The Problem (Speaker: Faizan)

\- Many security breaches start with small coding mistakes

\- Manual code review misses these because reviewers focus on features, not security

\- Security checks usually happen late, when fixes are expensive

\- Verizon DBIR identifies coding errors and credential misuse as leading causes of breaches



\## Slide 2: What Our Tool Does (Speaker: Asrin)

\- Automatically scans GitHub pull requests before code is merged

\- Detects three vulnerability types: hardcoded credentials, SQL injection, weak hashing

\- Posts a comment on the pull request explaining each issue and how to fix it

\- Dashboard tracks all findings over time



\## Slide 3: How the Rules Work (Speaker: Amnah)

\- Hardcoded Credential: pattern matches variable names like password, api\_key, token assigned to string values

\- SQL Injection: detects SQL keywords combined with string concatenation

\- Weak Hashing: flags use of MD5 and SHA-1

\- All rules skip comment lines to reduce false positives



\## Slide 4: Live Demo (Speaker: Faizan)

\- Open a new pull request with a vulnerable file

\- Show the comment appearing on the PR

\- Show the dashboard updating

\- (If live demo fails, play the backup video)



\## Slide 5: Testing and Results (Speaker: Fatima)

\- 7 functional tests, 3 nonfunctional, 2 systemic

\- All passed

\- Tool scans a small file in under 2 seconds

\- GitHub comment renders correctly



\## Slide 6: Limitations and Next Steps (Speaker: Fatima)

\- Only scans Python and JavaScript

\- Only three rules

\- Uses pattern matching, not full code analysis

\- Next: add more rules, support more languages, integrate with CI/CD pipelines



\## Slide 7: Conclusion (Speaker: Asrin)

\- Catches security problems earlier

\- Fits into existing GitHub workflow

\- No cost, no extra tools for the developer

\- Thank you

