#!/usr/bin/env python2.7

# Usage: command | SLACK_WEBHOOK_URL='https://hooks.slack.com/services/XX/XXXX' ./send-to-slack.py

import json
import os
import requests
import socket
import subprocess
import sys

class UsageException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

try:

    SLACK_WEBHOOK_URL = os.getenv('SLACK_WEBHOOK_URL')
    if SLACK_WEBHOOK_URL == None:
        raise UsageException("export SLACK_WEBHOOK_URL='https://hooks.slack.com/...'")

    payload = {
        'attachments': [
            {
                'title': socket.gethostname(),
                'pretext': '',
                'text': '```{}```'.format(''.join(sys.stdin.readlines())),
                'mrkdwn_in': ['text', 'pretext']
            }
        ]
    }
    r = requests.post(SLACK_WEBHOOK_URL, json=payload)
    print '{} {}'.format(r.status_code, r.text)

except UsageException as e:
    print e
    sys.exit(1)

except Exception as e:
    print e
    sys.exit(1)
