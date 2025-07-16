class EventSystem:
    def __init__(self):
        self.listeners = {}

    def on(self, event_name, callback):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    def raise_event(self, event_name, data=None):
        if event_name not in self.listeners:
            raise Exception(f"No listeners registered for event '{event_name}'")
        results = []
        for callback in self.listeners[event_name]:
            if data is not None:
                results.append(callback(data))
            else:
                results.append(callback())
        return results
event_system = EventSystem()
