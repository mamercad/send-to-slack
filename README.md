# Send to Slack

Simple Python script to send stuff to Slack.

## Installation

```shell
$ chmod +x send-to-slack.py
$ cp send-to-slack.py /some/directory/in/your/path/
```

## Usage

Create an `Incoming Webhook` in Slack and then:

```shell
command | SLACK_WEBHOOK_URL='https://hooks.slack.com/services/XX/XXXX' ./send-to-slack.py
```

That should do it.
