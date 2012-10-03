class ActivityPresenter:
    def __init__(self, connections):
        self._connections = connections

    def active_connections(self):
        return filter(lambda c: c.current_query != "<IDLE>", self._connections)

    def connections(self):
        return self._connections
