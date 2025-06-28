class EventSystem:
    def __init__(self):
        self.listeners = {}

    def on(self, event_name, callback=None):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)

    # def raise_event(self, event_name, data=None):
    #     if event_name in self.listeners:
    #         for callback in self.listeners[event_name]:
    #             callback(data)
    def raise_event(self, event_name, data=None):
        if event_name not in self.listeners:
            raise Exception(f"No listeners registered for event '{event_name}'")
        results = []
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                results.append(callback(data))
        return results
