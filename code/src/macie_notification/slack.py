import requests

from macie_notification.notifier import Notifier


class SlackNotifier(Notifier):
    def __init__(self, webhook_url, channel_name=None, user_name=None):
        self.webhook_url = webhook_url
        self.channel_name = channel_name
        self.user_name = user_name

    def notify(self, alert_event):
        """
        :type alert_event: macie_notification.alert.AlertEvent
        """
        color = 'good'
        if alert_event.risk_score >= 5:
            color = 'warning'
        if alert_event.risk_score >= 8:
            color = 'danger'

        payload = {
            'text': 'You have new Macie Alert! {}'.format(alert_event.url),
            'link_names': 1,
            'attachments': [{
                'text': ' ',
                'color': color,
                'fields': [
                    {'title': 'Risk', 'value': alert_event.risk_score, 'short': True},
                    {'title': 'Name', 'value': alert_event.alert_name, 'short': False},
                    {'title': 'Actor', 'value': alert_event.actor, 'short': False},
                    {'title': 'Created', 'value': alert_event.created_at, 'short': True},
                ]
            }]
        }
        if self.user_name:
            payload['username'] = self.user_name
        if self.channel_name:
            payload['channel'] = self.channel_name

        requests.post(self.webhook_url, json=payload)
