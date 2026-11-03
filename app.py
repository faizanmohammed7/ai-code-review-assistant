import os
import re
import requests
from database import init_db, save_finding, get_recent_scans
from flask import render_template
from flask import Flask, request
from github import GithubIntegration, AppAuth
from scanner import scan_files
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
init_db()

APP_ID = os.getenv("GITHUB_APP_ID")
PRIVATE_KEY_PATH = os.getenv("GITHUB_PRIVATE_KEY_PATH")
WEBHOOK_SECRET = os.getenv("GITHUB_WEBHOOK_SECRET")


def get_installation_token(installation_id):
    with open(PRIVATE_KEY_PATH, "r") as f:
        private_key = f.read()
    auth = AppAuth(int(APP_ID), private_key)
    integration = GithubIntegration(auth=auth)
    token = integration.get_access_token(installation_id)
    return token.token


def fetch_pr_files(repo_full_name, pr_number, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{repo_full_name}/pulls/{pr_number}/files"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def fetch_file_content(repo_full_name, filename, token, ref):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{repo_full_name}/contents/{filename}?ref={ref}"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    if "content" not in data:
        return None
    import base64
    return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")


def post_comment(repo_full_name, pr_number, token, body):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{repo_full_name}/issues/{pr_number}/comments"
    response = requests.post(url, headers=headers, json={"body": body})
    response.raise_for_status()
    return response.json()


@app.route("/")
def home():
    return "AI Code Review Assistant is running."


@app.route("/dashboard")
def dashboard():
    scans = get_recent_scans()
    return render_template("dashboard.html", scans=scans)


@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.json
    action = payload.get("action")

    if action not in ("opened", "synchronize"):
        return "ignored", 200

    repo_full_name = payload["repository"]["full_name"]
    pr_number = payload["pull_request"]["number"]
    installation_id = payload["installation"]["id"]
    head_sha = payload["pull_request"]["head"]["sha"]

    token = get_installation_token(installation_id)

    files = fetch_pr_files(repo_full_name, pr_number, token)

    file_list = []
    for f in files:
        filename = f["filename"]
        if not (filename.endswith(".py") or filename.endswith(".js")):
            continue
        content = fetch_file_content(repo_full_name, filename, token, head_sha)
        if content:
            file_list.append((filename, content))

        findings = scan_files(file_list)

    for f in findings:
        save_finding(repo_full_name, pr_number, f)

    if not findings:
        body = "### AI Code Review Assistant\n\nNo security issues found in this pull request."
    else:
        lines = ["### AI Code Review Assistant\n", f"Found **{len(findings)}** issue(s):\n"]
        for f in findings:
            lines.append(f"- **{f['rule']}** in `{f['file']}` line {f['line']}: `{f['matched']}`")
            lines.append(f"  - Suggestion: {f['suggestion']}")
        body = "\n".join(lines)

    post_comment(repo_full_name, pr_number, token, body)

    return "ok", 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)