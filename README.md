# Automated File Processing Workflow

This repository provides a **GitHub Actions workflow** that automatically processes files uploaded to the `input/` folder, generates processed output files, and sends them via email to multiple recipients. After processing, the input files are deleted, and commits containing uploaded files are cleaned up.

---

## Features

- Runs automatically when files are uploaded to the `input/` folder or on a schedule.
- Processes each file individually with `script.py`.
- Sends all processed files via email to multiple recipients.
- Deletes input files after processing.
- Resets the repository state to remove commits containing uploaded files.
- Supports multiple recipients for emails.
- Works entirely on GitHub without manual intervention.

---  
## Setup Instructions

### 1. Python Script

- `script.py` should contain the logic to process files from `input/` and save to `output/`.
- Each input file generates a corresponding output file.

### 2. Email Script

- `send_email.py` sends all files in `output/` via email.
- Supports multiple recipients by separating them with commas in `EMAIL_TO`.

### 3. GitHub Actions Workflow

- The workflow `.github/workflows/process-upload.yml`:
  - Triggers on file upload to `input/` or on a scheduled run.
  - Runs `script.py` to process files.
  - Sends processed files using `send_email.py`.
  - Deletes uploaded input files.
  - Resets commits to remove traces of uploaded files.

### 4. Secrets Setup

Add the following secrets in your repository settings:

| Secret Name       | Description |
|------------------|-------------|
| SMTP_SERVER       | SMTP server (e.g., `smtp.gmail.com`) |
| SMTP_PORT         | SMTP port (e.g., `587`) |
| SMTP_USERNAME     | SMTP username (email address) |
| SMTP_PASSWORD     | SMTP app password or email password |
| EMAIL_TO          | Comma-separated list of recipients (e.g., `person1@example.com,person2@example.com`) |
| REPO_PAT          | Personal Access Token with repo permissions for committing/reset |

> **Note:** For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your main password.

---

## Usage

1. Upload files to the `input/` folder via the GitHub Web UI.
2. Workflow will automatically:
   - Process the files.
   - Send them via email.
   - Delete input files.
   - Clean up the repository history for uploaded files.
3. Output files can be downloaded from the email attachment.

---

## Notes

- Ensure your `script.py` handles all file types you plan to upload.
- Workflow runs on Ubuntu-latest and Python 3.12.
- Multiple emails are supported via a comma-separated `EMAIL_TO` secret.
