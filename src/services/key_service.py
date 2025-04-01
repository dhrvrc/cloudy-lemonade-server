from crypt.key_manager import KeyManager

class KeyService(object):
    def __init__(self, key: str):
        self.key = key

    def get_key(self) -> str:
        return self.key