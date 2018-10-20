from threading import Thread


class NotificationCenter(object):

    def __init__(self):
        self.observers = {}

    _default = None

    @classmethod
    def default(cls):
        if cls._default is not None:
            return cls._default
        cls._default = cls()
        return cls._default

    def add_observer(self, key, method):
        """
        add a new observer function to the
        notification center. the observer
        will be called whenever a new notification
        is posted on with the matching key
        :param key: notification key
        :param method: targeted method
        :return: None
        """
        if key not in self.observers:
            self.observers[key] = []
        if method in self.observers[key]:
            print("duplicate")
            return
        self.observers[key].append(method)

    def post_notification(self, key, threaded=False, *args, **kwargs):
        """
        push a notification and call all the observers
        with the same key.
        :param key: notification key
        :param async: if true methods will be async
        :return:
        """
        if key not in self.observers:
            return

        for method in self.observers[key]:
            print('posting to', key, method)
            try:

                if threaded:
                    Thread(target=method, args=args, kwargs=kwargs).start()
                else:
                    method(*args, **kwargs)
            except Exception as err:
                # todo log error
                pass

    @staticmethod
    def notify_on(key):
        """
        notification center decorator
        :param key: notification key
        :return: decorator inner function
        """
        def inner(callable):
            NotificationCenter.default().add_observer(key, callable)
            return callable

        return inner
