from abc import abstractmethod


class Notifier(object):
    @abstractmethod
    def notify(self, alert_event):
        raise NotImplementedError()
