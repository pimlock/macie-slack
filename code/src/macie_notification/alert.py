class AlertEvent:
    """
    Wraps raw event from CloudWatch Events.
    """
    def __init__(self, raw_event):
        self.raw_event = raw_event

        self._detail = self.raw_event.get('detail', {})
        self._alert_name = self._detail.get('name')

    @property
    def alert_name(self):
        return self._alert_name

    @property
    def url(self):
        return self._detail.get('url', '')

    @property
    def risk_score(self):
        return self._detail.get('risk-score', '')

    @property
    def created_at(self):
        return self._detail.get('created-at', '')

    @property
    def actor(self):
        return self._detail.get('actor', '')
