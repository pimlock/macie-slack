#!/usr/bin/env bash

aws cloudformation deploy \
    --template-file ./packaged-template.yaml \
    --stack-name MacieSlackNotificationStack \
    --capabilities CAPABILITY_IAM \
    --parameter-overrides SlackWebhookUrl=$SLACK_WEBHOOK_URL