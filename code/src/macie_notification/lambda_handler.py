import json
import logging
import os

from macie_notification.alert import AlertEvent
from macie_notification.slack import SlackNotifier
from macie_notification.util.log import setup_lambda_logging

logger = logging.getLogger(__name__)


class Handler:
    def __init__(self, context):
        self.context = context

    def handle(self, event):
        if event.get('detail-type') != 'Macie Alert':
            logger.error('Unknown detail-type: %s', event.get('detail-type'))
            return

        logger.info(json.dumps(event, indent=2))
        alert_event = AlertEvent(event)

        notifier = self._create_notifier()
        notifier.notify(alert_event)

    def _create_notifier(self):
        """
        :rtype: macie_notification.notifier.Notifier
        """
        webhook_url = os.environ.get('SLACK_WEBHOOK_URL')
        channel_name = os.environ.get('SLACK_CHANNEL_NAME')
        user_name = os.environ.get('SLACK_USER_NAME')

        if not webhook_url:
            raise Exception('You must provide Slack webhook URL!')

        kwargs = {
            'webhook_url': webhook_url
        }
        if channel_name:
            kwargs['channel_name'] = channel_name
        if user_name:
            kwargs['user_name'] = user_name

        return SlackNotifier(**kwargs)


def main(event, context):
    setup_lambda_logging()

    handler = Handler(context)
    handler.handle(event)
