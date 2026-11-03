\# AI Code Review Assistant — Product Guide



\## What This Tool Does



This tool automatically scans GitHub pull requests for common security vulnerabilities before code is merged. It detects hardcoded credentials, SQL injection patterns, and weak hashing algorithms in Python and JavaScript files. When issues are found, the tool posts a comment on the pull request explaining each problem and how to fix it. A dashboard tracks all findings over time.



\## How to Set It Up



1\. Install Python 3.12 and uv (see setup notes).

2\. Clone or download this project folder.

3\. Run `uv add flask pygithub python-dotenv requests`.

4\. Create a GitHub App with pull request read/write and contents read permissions.

5\. Download the private key and save it as `private-key.pem` in this folder.

6\. Fill in `.env` with GITHUB\_APP\_ID, GITHUB\_PRIVATE\_KEY\_PATH, and GITHUB\_WEBHOOK\_SECRET.

7\. Install the GitHub App on your test repository.

8\. Start the webhook forwarder: `npx smee-client -u YOUR\_SMEE\_URL -t http://localhost:5000/webhook`

9\. Start the server: `uv run python app.py`

10\. Open a pull request in the test repository.



\## Rules Detected



| Rule | What It Finds | Example |

|------|---------------|---------|

| Hardcoded Credential | Passwords, API keys, tokens stored directly in code | `password = "admin123"` |

| SQL Injection Risk | SQL queries built with string concatenation | `"SELECT \* FROM users WHERE name = '" + user + "'"` |

| Weak Hashing Algorithm | Use of MD5 or SHA-1 | `hashlib.md5(...)` |



\## How to View Results



\- \*\*On the pull request:\*\* The tool posts a comment listing all findings.

\- \*\*On the dashboard:\*\* Open `http://localhost:5000/dashboard` to see all findings saved in the database.



\## Known Limitations



\- Only scans `.py` and `.js` files

\- Only checks the three rules listed above

\- Requires the pull request to be opened or updated (does not scan existing code)

\- Uses simple pattern matching, not full code analysis

