import secrets

class KeyManager:
    def __init__(self):
        pass
    
    def __generate_aes_key(self):
        return secrets.token_bytes(32) # 256 bits
    
    def __encrypt_aes(self, aes_key, public_asymmetric_key):
        """Encrypt the AES key using a public key."""
        pass
    
    def generate_and_encrypt_new_aes_key(self, public_asymmetric_key):
        """Generate and encrypt the AES key."""
        aes_key = self.__generate_aes_key()
        encrypted_aes_key = self.__encrypt_aes(aes_key, public_asymmetric_key)
        return encrypted_aes_key
    
    def encrypt_existing_aes_key(self, aes_key, public_asymmetric_key):
        """Generate and encrypt the AES key."""
        return self.__encrypt_aes(aes_key, public_asymmetric_key)