import binascii
from ecdsa import SigningKey, SECP256k1

def sign_tx(private_key:str,tx_hash:str):
    private_key_bytes = binascii.unhexlify(private_key)

    sk = SigningKey.from_string(
        private_key_bytes,
        curve=SECP256k1
    )

    hash_bytes = binascii.unhexlify(tx_hash)

    signature = sk.sign(hash_bytes)

    return binascii.hexlify(signature).decode()