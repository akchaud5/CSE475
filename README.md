# Email Automation Script

A Python script that sends automated emails at specified intervals using the Gmail API.

## Features
- Configurable email recipient and interval
- OAuth2 authentication with Gmail
- Clean exit with Ctrl+C

## Setup
1. Install required packages:
```python
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client

Enable Gmail API in Google Cloud Console
Download credentials.json
Run the script:

pythonCopypython test.py
Warning
Do not commit credentials.json to version control!
