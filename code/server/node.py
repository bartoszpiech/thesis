# Tutaj mialem problemy przy tworzeniu connection status jako enuma, zamiast
# tego dalem int, 0 -> otwarte polaczenia, 1 -> zamkniete polaczenia.
class Node:
    def __init__(self, device_id, connection_status):
        self.device_id = device_id
        self.connection_status = connection_status  # 1 -- open, 0 -- closed

    def to_json(self):
        return {'device_id': self.device_id, 'connection_status': self.connection_status}
